# # # # # """
# # # # # billing_module/billing_page.py
# # # # # New bill / Point-of-Sale UI.
# # # # # """

# # # # # import tkinter as tk
# # # # # from tkinter import messagebox, ttk
# # # # # from datetime import datetime
# # # # # from assets.theme import get as T, FONTS
# # # # # from assets.widgets import (
# # # # #     FlatButton, DangerButton, SuccessButton,
# # # # #     LabeledEntry, make_treeview, section_header, Toast
# # # # # )
# # # # # from product_module.product_ops import get_all_products, search_products, get_product_by_id
# # # # # from customer_module.customer_ops import create_bill
# # # # # from billing_module.bill_printer import generate_pdf_bill, open_file


# # # # # class BillingPage(tk.Frame):
# # # # #     def __init__(self, master, root_ref=None, on_bill_created=None, **kwargs):
# # # # #         t = T()
# # # # #         super().__init__(master, bg=t["bg"], **kwargs)
# # # # #         self.root_ref = root_ref
# # # # #         self.on_bill_created = on_bill_created  # callback to refresh dashboard
# # # # #         self._cart = []   # list of {product_id, product_name, price, quantity, subtotal}
# # # # #         self._build()

# # # # #     def _build(self):
# # # # #         t = T()
# # # # #         section_header(self, "🧾 New Bill / Point of Sale")

# # # # #         main = tk.Frame(self, bg=t["bg"])
# # # # #         main.pack(fill="both", expand=True, padx=24)
# # # # #         main.grid_columnconfigure(0, weight=2)
# # # # #         main.grid_columnconfigure(1, weight=3)
# # # # #         main.grid_rowconfigure(0, weight=1)

# # # # #         # Left: Customer + product search
# # # # #         left = tk.Frame(main, bg=t["card"], padx=20, pady=16)
# # # # #         left.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=4)
# # # # #         self._build_left(left)

# # # # #         # Right: Cart + totals
# # # # #         right = tk.Frame(main, bg=t["bg"])
# # # # #         right.grid(row=0, column=1, sticky="nsew", pady=4)
# # # # #         self._build_right(right)

# # # # #     # ── Left Panel ─────────────────────────────────────────────────────────────
# # # # #     def _build_left(self, panel):
# # # # #         t = T()

# # # # #         # Customer details
# # # # #         tk.Label(panel, text="👤 Customer Details", bg=t["card"], fg=t["accent"],
# # # # #                  font=FONTS["subhead"]).pack(anchor="w", pady=(0, 8))

# # # # #         self.f_cust = LabeledEntry(panel, label="Customer Name *", width=28)
# # # # #         self.f_cust.pack(fill="x", pady=4)
# # # # #         self.f_phone = LabeledEntry(panel, label="Phone Number", width=28)
# # # # #         self.f_phone.pack(fill="x", pady=4)
# # # # #         self.f_addr = LabeledEntry(panel, label="Address", width=28)
# # # # #         self.f_addr.pack(fill="x", pady=4)

# # # # #         tk.Frame(panel, bg=T()["border"], height=1).pack(fill="x", pady=10)

# # # # #         # Product search
# # # # #         tk.Label(panel, text="📦 Add Product to Cart", bg=t["card"], fg=t["accent"],
# # # # #                  font=FONTS["subhead"]).pack(anchor="w", pady=(0, 6))

# # # # #         self.prod_search = LabeledEntry(panel, label="Search Product by Name or ID", width=28)
# # # # #         self.prod_search.pack(fill="x", pady=4)
# # # # #         self.prod_search.entry.bind("<KeyRelease>", self._search_products)

# # # # #         # Product list
# # # # #         prod_list_frame = tk.Frame(panel, bg=t["card"])
# # # # #         prod_list_frame.pack(fill="x", pady=4)
# # # # #         cols = [
# # # # #             ("product_id",   "ID",    40),
# # # # #             ("product_name", "Name", 150),
# # # # #             ("quantity",     "Stock", 55),
# # # # #             ("price",        "Price", 70),
# # # # #         ]
# # # # #         self.prod_tree = make_treeview(prod_list_frame, cols, height=7)
# # # # #         self.prod_tree.bind("<Double-1>", self._select_product)

# # # # #         tk.Label(panel, text="↑ Double-click product to select",
# # # # #                  bg=t["card"], fg=t["text2"], font=FONTS["small"]).pack(anchor="w")

# # # # #         # Selected product info
# # # # #         self.sel_info = tk.Label(panel, text="", bg=t["card"], fg=t["accent3"],
# # # # #                                   font=FONTS["small"], wraplength=240)
# # # # #         self.sel_info.pack(anchor="w", pady=4)

# # # # #         # Quantity
# # # # #         qty_row = tk.Frame(panel, bg=t["card"])
# # # # #         qty_row.pack(fill="x", pady=4)
# # # # #         tk.Label(qty_row, text="Qty:", bg=t["card"], fg=t["text"],
# # # # #                  font=FONTS["body"]).pack(side="left")
# # # # #         self.qty_var = tk.IntVar(value=1)
# # # # #         tk.Spinbox(qty_row, from_=1, to=9999, textvariable=self.qty_var,
# # # # #                    bg=t["entry_bg"], fg=t["entry_fg"],
# # # # #                    buttonbackground=t["border"],
# # # # #                    relief="flat", width=6,
# # # # #                    font=FONTS["body"]).pack(side="left", padx=8)

# # # # #         SuccessButton(panel, text="Add to Cart", icon="🛒",
# # # # #                       command=self._add_to_cart).pack(fill="x", pady=8)

# # # # #         self._selected_prod = None
# # # # #         self._refresh_prod_list()

# # # # #     # ── Right Panel ────────────────────────────────────────────────────────────
# # # # #     def _build_right(self, panel):
# # # # #         t = T()

# # # # #         # Cart header
# # # # #         hdr = tk.Frame(panel, bg=t["bg"])
# # # # #         hdr.pack(fill="x", pady=(0, 4))
# # # # #         tk.Label(hdr, text="🛒 Cart", bg=t["bg"], fg=t["text"],
# # # # #                  font=FONTS["subhead"]).pack(side="left")
# # # # #         DangerButton(hdr, text="Clear Cart", icon="🗑️",
# # # # #                      command=self._clear_cart).pack(side="right")

# # # # #         cols = [
# # # # #             ("product_name", "Product",  190),
# # # # #             ("quantity",     "Qty",       50),
# # # # #             ("price",        "Unit (₹)",  90),
# # # # #             ("subtotal",     "Total (₹)", 90),
# # # # #         ]
# # # # #         cart_frame = tk.Frame(panel, bg=t["bg"])
# # # # #         cart_frame.pack(fill="both", expand=True)
# # # # #         self.cart_tree = make_treeview(cart_frame, cols, height=14)
# # # # #         self.cart_tree.bind("<Delete>", self._remove_cart_item)

# # # # #         # Total row
# # # # #         total_card = tk.Frame(panel, bg=t["card2"], padx=16, pady=12)
# # # # #         total_card.pack(fill="x", pady=6)
# # # # #         tk.Label(total_card, text="GRAND TOTAL", bg=t["card2"], fg=t["text2"],
# # # # #                  font=FONTS["subhead"]).pack(side="left")
# # # # #         self.total_label = tk.Label(total_card, text="₹ 0.00",
# # # # #                                      bg=t["card2"], fg=t["accent2"],
# # # # #                                      font=("Segoe UI", 20, "bold"))
# # # # #         self.total_label.pack(side="right")

# # # # #         # Action buttons
# # # # #         btn_row = tk.Frame(panel, bg=t["bg"])
# # # # #         btn_row.pack(fill="x", pady=4)
# # # # #         SuccessButton(btn_row, text="Generate Bill", icon="🖨️",
# # # # #                       command=self._generate_bill).pack(side="left", padx=(0,6))
# # # # #         FlatButton(btn_row, text="New Bill", icon="📝",
# # # # #                    color=T()["card2"], fg=T()["text"], hover=T()["hover"],
# # # # #                    command=self._new_bill).pack(side="left")

# # # # #         tk.Label(panel, text="Press Delete key to remove item from cart",
# # # # #                  bg=t["bg"], fg=t["text2"], font=FONTS["small"]).pack(anchor="w", pady=2)

# # # # #     # ── Logic ──────────────────────────────────────────────────────────────────
# # # # #     def _search_products(self, event=None):
# # # # #         q = self.prod_search.get()
# # # # #         if q:
# # # # #             rows = search_products(q)
# # # # #         else:
# # # # #             rows = get_all_products()
# # # # #         self._load_prod_tree(rows)

# # # # #     def _refresh_prod_list(self):
# # # # #         rows = get_all_products()
# # # # #         self._load_prod_tree(rows)

# # # # #     def _load_prod_tree(self, rows):
# # # # #         self.prod_tree.delete(*self.prod_tree.get_children())
# # # # #         for r in rows:
# # # # #             tag = "out" if r["quantity"] == 0 else ("low" if r["quantity"] <= 5 else "")
# # # # #             self.prod_tree.insert("", "end", values=(
# # # # #                 r["product_id"], r["product_name"],
# # # # #                 r["quantity"], f"₹ {r['price']:.2f}"
# # # # #             ), tags=(tag,))
# # # # #         self.prod_tree.tag_configure("out", foreground=T()["danger"])
# # # # #         self.prod_tree.tag_configure("low", foreground=T()["warn"])

# # # # #     def _select_product(self, event=None):
# # # # #         sel = self.prod_tree.selection()
# # # # #         if not sel:
# # # # #             return
# # # # #         vals = self.prod_tree.item(sel[0], "values")
# # # # #         pid  = int(vals[0])
# # # # #         prod = get_product_by_id(pid)
# # # # #         if not prod:
# # # # #             return
# # # # #         if prod["quantity"] == 0:
# # # # #             messagebox.showwarning("Out of Stock", f"'{prod['product_name']}' is OUT OF STOCK.")
# # # # #             return
# # # # #         self._selected_prod = prod
# # # # #         self.sel_info.config(
# # # # #             text=f"✅ {prod['product_name']} | Stock: {prod['quantity']} | ₹{prod['price']:.2f}/unit"
# # # # #         )

# # # # #     def _add_to_cart(self):
# # # # #         if not self._selected_prod:
# # # # #             messagebox.showwarning("Select Product", "Please double-click a product first.")
# # # # #             return
# # # # #         qty = self.qty_var.get()
# # # # #         if qty <= 0:
# # # # #             messagebox.showwarning("Invalid Qty", "Quantity must be ≥ 1.")
# # # # #             return
# # # # #         if qty > self._selected_prod["quantity"]:
# # # # #             messagebox.showwarning(
# # # # #                 "Insufficient Stock",
# # # # #                 f"Only {self._selected_prod['quantity']} units available."
# # # # #             )
# # # # #             return

# # # # #         # Check if already in cart → update qty
# # # # #         for item in self._cart:
# # # # #             if item["product_id"] == self._selected_prod["product_id"]:
# # # # #                 new_qty = item["quantity"] + qty
# # # # #                 if new_qty > self._selected_prod["quantity"]:
# # # # #                     messagebox.showwarning("Insufficient Stock",
# # # # #                                            f"Max available: {self._selected_prod['quantity']}")
# # # # #                     return
# # # # #                 item["quantity"] = new_qty
# # # # #                 item["subtotal"] = round(item["price"] * new_qty, 2)
# # # # #                 self._refresh_cart()
# # # # #                 return

# # # # #         self._cart.append({
# # # # #             "product_id":   self._selected_prod["product_id"],
# # # # #             "product_name": self._selected_prod["product_name"],
# # # # #             "price":        self._selected_prod["price"],
# # # # #             "quantity":     qty,
# # # # #             "subtotal":     round(self._selected_prod["price"] * qty, 2),
# # # # #         })
# # # # #         self._refresh_cart()
# # # # #         self._selected_prod = None
# # # # #         self.sel_info.config(text="")

# # # # #     def _refresh_cart(self):
# # # # #         self.cart_tree.delete(*self.cart_tree.get_children())
# # # # #         total = 0.0
# # # # #         for i, item in enumerate(self._cart):
# # # # #             tag = "alt" if i % 2 == 1 else ""
# # # # #             self.cart_tree.insert("", "end", values=(
# # # # #                 item["product_name"], item["quantity"],
# # # # #                 f"₹ {item['price']:.2f}", f"₹ {item['subtotal']:.2f}"
# # # # #             ), tags=(tag,))
# # # # #             total += item["subtotal"]
# # # # #         self.total_label.config(text=f"₹ {total:,.2f}")

# # # # #     def _remove_cart_item(self, event=None):
# # # # #         sel = self.cart_tree.selection()
# # # # #         if not sel:
# # # # #             return
# # # # #         idx = self.cart_tree.index(sel[0])
# # # # #         if 0 <= idx < len(self._cart):
# # # # #             self._cart.pop(idx)
# # # # #         self._refresh_cart()

# # # # #     def _clear_cart(self):
# # # # #         self._cart.clear()
# # # # #         self._refresh_cart()

# # # # #     def _generate_bill(self):
# # # # #         cust_name = self.f_cust.get()
# # # # #         if not cust_name:
# # # # #             messagebox.showwarning("Missing Info", "Please enter customer name.")
# # # # #             return
# # # # #         if not self._cart:
# # # # #             messagebox.showwarning("Empty Cart", "Please add at least one product.")
# # # # #             return

# # # # #         items = [{"product_id": i["product_id"], "quantity": i["quantity"]}
# # # # #                  for i in self._cart]
# # # # #         try:
# # # # #             bill_data = create_bill(
# # # # #                 customer_name=cust_name,
# # # # #                 phone=self.f_phone.get(),
# # # # #                 address=self.f_addr.get(),
# # # # #                 items=items,
# # # # #             )
# # # # #         except ValueError as e:
# # # # #             messagebox.showerror("Error", str(e))
# # # # #             return

# # # # #         # Show bill preview popup
# # # # #         self._show_bill_popup(bill_data)

# # # # #         if self.on_bill_created:
# # # # #             self.on_bill_created()

# # # # #     def _show_bill_popup(self, bill_data: dict):
# # # # #         t = T()
# # # # #         popup = tk.Toplevel(self)
# # # # #         popup.title(f"Bill — {bill_data['bill_number']}")
# # # # #         popup.configure(bg=t["bg"])
# # # # #         popup.geometry("500x600")
# # # # #         popup.grab_set()

# # # # #         # Header
# # # # #         hdr = tk.Frame(popup, bg=t["accent"], pady=14)
# # # # #         hdr.pack(fill="x")
# # # # #         tk.Label(hdr, text="📚 Binod Book Binding", bg=t["accent"], fg="#fff",
# # # # #                  font=FONTS["heading"]).pack()
# # # # #         tk.Label(hdr, text="Stationery & Book Binding Shop", bg=t["accent"],
# # # # #                  fg="#c5cae9", font=FONTS["small"]).pack()

# # # # #         # Info
# # # # #         info_frame = tk.Frame(popup, bg=t["card"], padx=20, pady=10)
# # # # #         info_frame.pack(fill="x")
# # # # #         def info_row(lbl, val):
# # # # #             r = tk.Frame(info_frame, bg=t["card"])
# # # # #             r.pack(fill="x", pady=2)
# # # # #             tk.Label(r, text=lbl, bg=t["card"], fg=t["text2"],
# # # # #                      width=14, anchor="w", font=FONTS["small"]).pack(side="left")
# # # # #             tk.Label(r, text=val, bg=t["card"], fg=t["text"],
# # # # #                      font=FONTS["body"], anchor="w").pack(side="left")

# # # # #         info_row("Bill No:", bill_data["bill_number"])
# # # # #         info_row("Date:", bill_data["bill_date"])
# # # # #         info_row("Customer:", bill_data["customer_name"])
# # # # #         info_row("Phone:", bill_data.get("phone", "—"))
# # # # #         info_row("Address:", bill_data.get("address", "—"))

# # # # #         # Items table
# # # # #         tk.Frame(popup, bg=t["border"], height=1).pack(fill="x", padx=16, pady=6)
# # # # #         cols = [
# # # # #             ("product_name", "Product",   190),
# # # # #             ("quantity",     "Qty",        50),
# # # # #             ("price",        "Unit (₹)",   80),
# # # # #             ("subtotal",     "Total (₹)", 80),
# # # # #         ]
# # # # #         tree_f = tk.Frame(popup, bg=t["bg"])
# # # # #         tree_f.pack(fill="x", padx=16)
# # # # #         tree = make_treeview(tree_f, cols, height=7)
# # # # #         for item in bill_data["items"]:
# # # # #             tree.insert("", "end", values=(
# # # # #                 item["product_name"], item["quantity"],
# # # # #                 f"₹ {item['price']:.2f}", f"₹ {item['subtotal']:.2f}"
# # # # #             ))

# # # # #         # Total
# # # # #         total_f = tk.Frame(popup, bg=t["card2"], padx=16, pady=10)
# # # # #         total_f.pack(fill="x", padx=16, pady=6)
# # # # #         tk.Label(total_f, text="GRAND TOTAL", bg=t["card2"], fg=t["text2"],
# # # # #                  font=FONTS["subhead"]).pack(side="left")
# # # # #         tk.Label(total_f, text=f"₹ {bill_data['grand_total']:,.2f}",
# # # # #                  bg=t["card2"], fg=t["accent2"],
# # # # #                  font=("Segoe UI", 18, "bold")).pack(side="right")

# # # # #         # Buttons
# # # # #         btn_f = tk.Frame(popup, bg=t["bg"], pady=10)
# # # # #         btn_f.pack()

# # # # #         def export_pdf():
# # # # #             path = generate_pdf_bill(bill_data)
# # # # #             open_file(path)
# # # # #             Toast(self.root_ref or self, f"Bill saved: {path}", "success", 4000)

# # # # #         FlatButton(btn_f, text="Export PDF", icon="📄",
# # # # #                    command=export_pdf).pack(side="left", padx=6)
# # # # #         FlatButton(btn_f, text="Print", icon="🖨️",
# # # # #                    color=t["card2"], fg=t["text"], hover=t["hover"],
# # # # #                    command=export_pdf).pack(side="left", padx=6)
# # # # #         FlatButton(btn_f, text="Close", icon="✖",
# # # # #                    color=t["danger"], hover="#b71c1c",
# # # # #                    command=lambda: [popup.destroy(), self._new_bill()]
# # # # #                    ).pack(side="left", padx=6)

# # # # #     def _new_bill(self):
# # # # #         self._cart.clear()
# # # # #         self._refresh_cart()
# # # # #         for f in (self.f_cust, self.f_phone, self.f_addr):
# # # # #             f.clear()
# # # # #         self._selected_prod = None
# # # # #         self.sel_info.config(text="")
# # # # #         self._refresh_prod_list()

# # # # #     def refresh(self):
# # # # #         self._refresh_prod_list()












# """
# billing_module/billing_page.py
# FINAL Professional POS Billing UI
# """

# import tkinter as tk
# from tkinter import messagebox, ttk

# from assets.theme import get as T
# from assets.widgets import (
#     FlatButton,
#     DangerButton,
#     SuccessButton,
#     LabeledEntry,
#     make_treeview,
#     section_header,
# )

# from product_module.product_ops import (
#     get_all_products,
#     search_products,
#     get_product_by_id
# )

# from customer_module.customer_ops import create_bill

# from billing_module.bill_printer import (
#     generate_pdf_bill,
#     open_file
# )


# class BillingPage(tk.Frame):

#     def __init__(self, master, root_ref=None, on_bill_created=None, **kwargs):

#         self.t = T()

#         super().__init__(
#             master,
#             bg=self.t["bg"],
#             **kwargs
#         )

#         self.root_ref = root_ref
#         self.on_bill_created = on_bill_created

#         self._cart = []

#         self._build()

#     # =========================================================
#     # BUILD UI
#     # =========================================================
#     def _build(self):

#         t = self.t

#         section_header(
#             self,
#             "🧾 Billing / Point Of Sale"
#         )

#         # =====================================================
#         # MAIN CONTAINER
#         # =====================================================
#         main = tk.Frame(
#             self,
#             bg=t["bg"]
#         )

#         main.pack(
#             fill="both",
#             expand=True,
#             padx=15,
#             pady=10
#         )

#         # LEFT SIDE BIGGER
#         main.grid_columnconfigure(0, weight=4)
#         main.grid_columnconfigure(1, weight=2)

#         main.grid_rowconfigure(0, weight=1)

#         # =====================================================
#         # LEFT PANEL
#         # =====================================================
#         left = tk.Frame(
#             main,
#             bg=t["card"],
#             padx=20,
#             pady=18
#         )

#         left.grid(
#             row=0,
#             column=0,
#             sticky="nsew",
#             padx=(0, 10)
#         )

#         self._build_left(left)

#         # =====================================================
#         # RIGHT PANEL
#         # =====================================================
#         right = tk.Frame(
#             main,
#             bg=t["bg"]
#         )

#         right.grid(
#             row=0,
#             column=1,
#             sticky="nsew"
#         )

#         self._build_right(right)

#     # =========================================================
#     # LEFT PANEL
#     # =========================================================
#     def _build_left(self, panel):

#         t = self.t

#         # =====================================================
#         # CUSTOMER DETAILS
#         # =====================================================
#         tk.Label(
#             panel,
#             text="👤 Customer Details",
#             bg=t["card"],
#             fg=t["accent"],
#             font=("Segoe UI", 18, "bold")
#         ).pack(
#             anchor="w",
#             pady=(0, 12)
#         )

#         self.f_cust = LabeledEntry(
#             panel,
#             label="Customer Name *",
#             width=42
#         )

#         self.f_cust.pack(
#             fill="x",
#             pady=6
#         )

#         self.f_cust.entry.config(
#             font=("Segoe UI", 13)
#         )

#         self.f_phone = LabeledEntry(
#             panel,
#             label="Phone Number",
#             width=42
#         )

#         self.f_phone.pack(
#             fill="x",
#             pady=6
#         )

#         self.f_phone.entry.config(
#             font=("Segoe UI", 13)
#         )

#         self.f_addr = LabeledEntry(
#             panel,
#             label="Address",
#             width=42
#         )

#         self.f_addr.pack(
#             fill="x",
#             pady=6
#         )

#         self.f_addr.entry.config(
#             font=("Segoe UI", 13)
#         )

#         # =====================================================
#         # DIVIDER
#         # =====================================================
#         tk.Frame(
#             panel,
#             bg=t["border"],
#             height=2
#         ).pack(
#             fill="x",
#             pady=18
#         )

#         # =====================================================
#         # PRODUCT SECTION
#         # =====================================================
#         tk.Label(
#             panel,
#             text="📦 Add Product",
#             bg=t["card"],
#             fg=t["accent"],
#             font=("Segoe UI", 17, "bold")
#         ).pack(
#             anchor="w",
#             pady=(0, 10)
#         )

#         # =====================================================
#         # TOP CONTROL ROW
#         # =====================================================
#         top_row = tk.Frame(
#             panel,
#             bg=t["card"]
#         )

#         top_row.pack(
#             fill="x",
#             pady=5
#         )

#         # SEARCH
#         self.prod_search = LabeledEntry(
#             top_row,
#             label="Search Product",
#             width=28
#         )

#         self.prod_search.pack(
#             side="left",
#             padx=(0, 10)
#         )

#         self.prod_search.entry.config(
#             font=("Segoe UI", 12)
#         )

#         self.prod_search.entry.bind(
#             "<KeyRelease>",
#             self._search_products
#         )

#         # QUANTITY
#         qty_box = tk.Frame(
#             top_row,
#             bg=t["card"]
#         )

#         qty_box.pack(side="left")

#         tk.Label(
#             qty_box,
#             text="Qty",
#             bg=t["card"],
#             fg=t["text"],
#             font=("Segoe UI", 12, "bold")
#         ).pack()

#         self.qty_var = tk.IntVar(value=1)

#         qty_spin = tk.Spinbox(
#             qty_box,
#             from_=1,
#             to=9999,
#             textvariable=self.qty_var,
#             width=5,
#             font=("Segoe UI", 12, "bold"),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat"
#         )

#         qty_spin.pack(
#             pady=(3, 0)
#         )

#         # ADD TO CART BUTTON
#         add_btn = tk.Button(
#             top_row,
#             text="🛒 Add",
#             bg="#16a34a",
#             fg="white",
#             activebackground="#15803d",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 11, "bold"),
#             padx=16,
#             pady=8,
#             command=self._add_to_cart
#         )

#         add_btn.pack(
#             side="left",
#             padx=(12, 0),
#             pady=(18, 0)
#         )

#         # =====================================================
#         # PRODUCT TABLE FRAME
#         # =====================================================
#         table_outer = tk.Frame(
#             panel,
#             bg=t["card"]
#         )

#         table_outer.pack(
#             fill="both",
#             expand=True,
#             pady=10
#         )

#         # TABLE SCROLLBAR
#         y_scroll = ttk.Scrollbar(
#             table_outer,
#             orient="vertical"
#         )

#         y_scroll.pack(
#             side="right",
#             fill="y"
#         )

#         cols = [
#             ("product_id", "ID", 70),
#             ("product_name", "Product Name", 320),
#             ("quantity", "Stock", 100),
#             ("price", "Price", 120),
#         ]

#         self.prod_tree = ttk.Treeview(
#             table_outer,
#             columns=[c[0] for c in cols],
#             show="headings",
#             height=13,
#             yscrollcommand=y_scroll.set
#         )

#         y_scroll.config(
#             command=self.prod_tree.yview
#         )

#         # STYLE
#         style = ttk.Style()

#         style.configure(
#             "Treeview",
#             rowheight=34,
#             font=("Segoe UI", 11),
#             background=t["card"],
#             foreground=t["text"],
#             fieldbackground=t["card"]
#         )

#         style.configure(
#             "Treeview.Heading",
#             font=("Segoe UI", 11, "bold")
#         )

#         # HEADINGS
#         for col_id, title, width in cols:

#             self.prod_tree.heading(
#                 col_id,
#                 text=title
#             )

#             self.prod_tree.column(
#                 col_id,
#                 width=width,
#                 anchor="center"
#             )

#         self.prod_tree.pack(
#             fill="both",
#             expand=True
#         )

#         self.prod_tree.bind(
#             "<Double-1>",
#             self._select_product
#         )

#         # =====================================================
#         # SELECTED PRODUCT INFO
#         # =====================================================
#         self.sel_info = tk.Label(
#             panel,
#             text="",
#             bg=t["card"],
#             fg=t["accent3"],
#             font=("Segoe UI", 12, "bold"),
#             wraplength=650
#         )

#         self.sel_info.pack(
#             anchor="w",
#             pady=8
#         )

#         self._selected_prod = None

#         self._refresh_prod_list()

#     # =========================================================
#     # RIGHT PANEL
#     # =========================================================
#     def _build_right(self, panel):

#         t = self.t

#         # HEADER
#         header = tk.Frame(
#             panel,
#             bg=t["bg"]
#         )

#         header.pack(
#             fill="x",
#             pady=(0, 8)
#         )

#         tk.Label(
#             header,
#             text="🛒 Cart",
#             bg=t["bg"],
#             fg=t["text"],
#             font=("Segoe UI", 17, "bold")
#         ).pack(side="left")

#         DangerButton(
#             header,
#             text="Clear",
#             command=self._clear_cart
#         ).pack(side="right")

#         # =====================================================
#         # CART TABLE
#         # =====================================================
#         cart_frame = tk.Frame(
#             panel,
#             bg=t["card"]
#         )

#         cart_frame.pack(
#             fill="both",
#             expand=True
#         )

#         cols = [
#             ("product_name", "Product", 180),
#             ("quantity", "Qty", 60),
#             ("price", "Price", 80),
#             ("subtotal", "Total", 90),
#         ]

#         self.cart_tree = make_treeview(
#             cart_frame,
#             cols,
#             height=11
#         )

#         self.cart_tree.bind(
#             "<Delete>",
#             self._remove_cart_item
#         )

#         # =====================================================
#         # TOTAL
#         # =====================================================
#         total_card = tk.Frame(
#             panel,
#             bg=t["card2"],
#             padx=18,
#             pady=14
#         )

#         total_card.pack(
#             fill="x",
#             pady=10
#         )

#         tk.Label(
#             total_card,
#             text="GRAND TOTAL",
#             bg=t["card2"],
#             fg=t["text2"],
#             font=("Segoe UI", 13, "bold")
#         ).pack(side="left")

#         self.total_label = tk.Label(
#             total_card,
#             text="₹ 0.00",
#             bg=t["card2"],
#             fg=t["accent2"],
#             font=("Segoe UI", 20, "bold")
#         )

#         self.total_label.pack(side="right")

#         # =====================================================
#         # BUTTONS
#         # =====================================================
#         btn_frame = tk.Frame(
#             panel,
#             bg=t["bg"]
#         )

#         btn_frame.pack(
#             fill="x",
#             pady=8
#         )

#         generate_btn = tk.Button(
#             btn_frame,
#             text="🖨 Generate Bill",
#             bg="#2563eb",
#             fg="white",
#             activebackground="#1d4ed8",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 12, "bold"),
#             padx=24,
#             pady=12,
#             command=self._generate_bill
#         )

#         generate_btn.pack(
#             side="left",
#             padx=(0, 8)
#         )

#         new_btn = tk.Button(
#             btn_frame,
#             text="📝 New Bill",
#             bg="#374151",
#             fg="white",
#             activebackground="#1f2937",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 12, "bold"),
#             padx=18,
#             pady=12,
#             command=self._new_bill
#         )

#         new_btn.pack(side="left")

#     # =========================================================
#     # SEARCH PRODUCTS
#     # =========================================================
#     def _search_products(self, event=None):

#         q = self.prod_search.get()

#         if q:
#             rows = search_products(q)
#         else:
#             rows = get_all_products()

#         self._load_prod_tree(rows)

#     # =========================================================
#     # REFRESH PRODUCT LIST
#     # =========================================================
#     def _refresh_prod_list(self):

#         rows = get_all_products()

#         self._load_prod_tree(rows)

#     # =========================================================
#     # LOAD PRODUCT TABLE
#     # =========================================================
#     def _load_prod_tree(self, rows):

#         self.prod_tree.delete(*self.prod_tree.get_children())

#         for r in rows:

#             tag = ""

#             if r["quantity"] == 0:
#                 tag = "out"

#             elif r["quantity"] <= 5:
#                 tag = "low"

#             self.prod_tree.insert(
#                 "",
#                 "end",
#                 values=(
#                     r["product_id"],
#                     r["product_name"],
#                     r["quantity"],
#                     f"₹ {r['price']:.2f}"
#                 ),
#                 tags=(tag,)
#             )

#         self.prod_tree.tag_configure(
#             "out",
#             foreground="red"
#         )

#         self.prod_tree.tag_configure(
#             "low",
#             foreground="#f59e0b"
#         )

#     # =========================================================
#     # SELECT PRODUCT
#     # =========================================================
#     def _select_product(self, event=None):

#         selected = self.prod_tree.selection()

#         if not selected:
#             return

#         vals = self.prod_tree.item(
#             selected[0],
#             "values"
#         )

#         pid = int(vals[0])

#         prod = get_product_by_id(pid)

#         if not prod:
#             return

#         self._selected_prod = prod

#         self.sel_info.config(
#             text=f"Selected Product: {prod['product_name']}   |   Stock: {prod['quantity']}   |   Price: ₹ {prod['price']}"
#         )

#     # =========================================================
#     # ADD TO CART
#     # =========================================================
#     def _add_to_cart(self):

#         if not self._selected_prod:

#             messagebox.showwarning(
#                 "Warning",
#                 "Select Product First"
#             )

#             return

#         qty = self.qty_var.get()

#         if qty > self._selected_prod["quantity"]:

#             messagebox.showwarning(
#                 "Stock Error",
#                 f"Only {self._selected_prod['quantity']} items available"
#             )

#             return

#         subtotal = qty * self._selected_prod["price"]

#         self._cart.append({
#             "product_id": self._selected_prod["product_id"],
#             "product_name": self._selected_prod["product_name"],
#             "quantity": qty,
#             "price": self._selected_prod["price"],
#             "subtotal": subtotal
#         })

#         self._refresh_cart()

#     # =========================================================
#     # REFRESH CART
#     # =========================================================
#     def _refresh_cart(self):

#         self.cart_tree.delete(*self.cart_tree.get_children())

#         total = 0

#         for item in self._cart:

#             total += item["subtotal"]

#             self.cart_tree.insert(
#                 "",
#                 "end",
#                 values=(
#                     item["product_name"],
#                     item["quantity"],
#                     f"₹ {item['price']:.2f}",
#                     f"₹ {item['subtotal']:.2f}"
#                 )
#             )

#         self.total_label.config(
#             text=f"₹ {total:,.2f}"
#         )

#     # =========================================================
#     # REMOVE ITEM
#     # =========================================================
#     def _remove_cart_item(self, event=None):

#         selected = self.cart_tree.selection()

#         if not selected:
#             return

#         idx = self.cart_tree.index(selected[0])

#         self._cart.pop(idx)

#         self._refresh_cart()

#     # =========================================================
#     # CLEAR CART
#     # =========================================================
#     def _clear_cart(self):

#         self._cart.clear()

#         self._refresh_cart()

#     # =========================================================
#     # GENERATE BILL
#     # =========================================================
#     def _generate_bill(self):

#         customer = self.f_cust.get()

#         if not customer:

#             messagebox.showwarning(
#                 "Warning",
#                 "Enter Customer Name"
#             )

#             return

#         if not self._cart:

#             messagebox.showwarning(
#                 "Warning",
#                 "Cart is Empty"
#             )

#             return

#         items = []

#         for item in self._cart:

#             items.append({
#                 "product_id": item["product_id"],
#                 "quantity": item["quantity"]
#             })

#         try:

#             bill_data = create_bill(
#                 customer_name=customer,
#                 phone=self.f_phone.get(),
#                 address=self.f_addr.get(),
#                 items=items
#             )

#             messagebox.showinfo(
#                 "Success",
#                 "Bill Generated Successfully"
#             )

#             self._show_bill_popup(bill_data)

#             self._new_bill()

#             self._refresh_prod_list()

#             if self.on_bill_created:
#                 self.on_bill_created()

#         except Exception as e:

#             messagebox.showerror(
#                 "Error",
#                 str(e)
#             )

#     # =========================================================
#     # BILL POPUP
#     # =========================================================
#     def _show_bill_popup(self, bill_data):

#         popup = tk.Toplevel(self)

#         popup.title("Bill Preview")

#         popup.geometry("500x600")

#         popup.configure(bg=self.t["bg"])

#         tk.Label(
#             popup,
#             text="📚 Binod Book Binding",
#             bg=self.t["bg"],
#             fg=self.t["text"],
#             font=("Segoe UI", 20, "bold")
#         ).pack(pady=10)

#         text = tk.Text(
#             popup,
#             font=("Consolas", 11),
#             bg=self.t["card"],
#             fg=self.t["text"]
#         )

#         text.pack(
#             fill="both",
#             expand=True,
#             padx=15,
#             pady=10
#         )

#         bill_text = ""

#         bill_text += f"Bill No: {bill_data['bill_number']}\n"
#         bill_text += f"Customer: {bill_data['customer_name']}\n\n"

#         for item in bill_data["items"]:

#             bill_text += (
#                 f"{item['product_name']} "
#                 f"x {item['quantity']} = "
#                 f"₹ {item['subtotal']}\n"
#             )

#         bill_text += "\n"
#         bill_text += f"Grand Total: ₹ {bill_data['grand_total']}"

#         text.insert("1.0", bill_text)

#         def export_pdf():

#             path = generate_pdf_bill(bill_data)

#             open_file(path)

#         tk.Button(
#             popup,
#             text="Export PDF",
#             bg="#2563eb",
#             fg="white",
#             font=("Segoe UI", 11, "bold"),
#             command=export_pdf
#         ).pack(pady=10)

#     # =========================================================
#     # NEW BILL
#     # =========================================================
#     def _new_bill(self):

#         self._cart.clear()

#         self._refresh_cart()

#         self.f_cust.clear()
#         self.f_phone.clear()
#         self.f_addr.clear()

#         self.sel_info.config(text="")

#     # =========================================================
#     # REFRESH
#     # =========================================================
#     def refresh(self):

#         self._refresh_prod_list()
















"""
billing_module/billing_page.py
Ultra Professional POS Billing UI
FINAL UPDATED VERSION
"""

import tkinter as tk
from tkinter import messagebox, ttk

from assets.theme import get as T, FONTS
from assets.widgets import (
    FlatButton,
    DangerButton,
    SuccessButton,
    LabeledEntry,
    make_treeview,
    section_header,
    Toast
)

from product_module.product_ops import (
    get_all_products,
    search_products,
    get_product_by_id
)

from customer_module.customer_ops import create_bill

from billing_module.bill_printer import (
    generate_pdf_bill,
    open_file
)


class BillingPage(tk.Frame):

    def __init__(
        self,
        master,
        root_ref=None,
        on_bill_created=None,
        **kwargs
    ):

        self.t = T()

        super().__init__(
            master,
            bg=self.t["bg"],
            **kwargs
        )

        self.root_ref = root_ref
        self.on_bill_created = on_bill_created

        self._cart = []

        self._build()

    # =========================================================
    # BUILD UI
    # =========================================================
    def _build(self):

        t = self.t

        section_header(
            self,
            "🧾 Billing / Point Of Sale"
        )

        main = tk.Frame(
            self,
            bg=t["bg"]
        )

        main.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=10
        )

        main.grid_columnconfigure(0, weight=4)
        main.grid_columnconfigure(1, weight=3)

        main.grid_rowconfigure(0, weight=1)

        # =====================================================
        # LEFT PANEL
        # =====================================================
        left = tk.Frame(
            main,
            bg=t["card"],
            padx=25,
            pady=20
        )

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self._build_left(left)

        # =====================================================
        # RIGHT PANEL
        # =====================================================
        right = tk.Frame(
            main,
            bg=t["bg"]
        )

        right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self._build_right(right)

    # =========================================================
    # LEFT PANEL
    # =========================================================
    def _build_left(self, panel):

        t = self.t

        # ================= TITLE =================
        tk.Label(
            panel,
            text="👤 Customer Details",
            bg=t["card"],
            fg=t["accent"],
            font=("Segoe UI", 20, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        # ================= CUSTOMER FIELDS =================
        self.f_cust = LabeledEntry(
            panel,
            label="Customer Name *",
            width=42
        )

        self.f_cust.pack(
            fill="x",
            pady=8
        )

        self.f_cust.entry.config(
            font=("Segoe UI", 14)
        )

        self.f_phone = LabeledEntry(
            panel,
            label="Phone Number",
            width=42
        )

        self.f_phone.pack(
            fill="x",
            pady=8
        )

        self.f_phone.entry.config(
            font=("Segoe UI", 14)
        )

        self.f_addr = LabeledEntry(
            panel,
            label="Address",
            width=42
        )

        self.f_addr.pack(
            fill="x",
            pady=8
        )

        self.f_addr.entry.config(
            font=("Segoe UI", 14)
        )

        # DIVIDER
        tk.Frame(
            panel,
            bg=t["border"],
            height=2
        ).pack(
            fill="x",
            pady=18
        )

        # ================= PRODUCT TITLE =================
        tk.Label(
            panel,
            text="📦 Add Product",
            bg=t["card"],
            fg=t["accent"],
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        # =====================================================
        # SEARCH + QTY + BUTTON SAME ROW
        # =====================================================
        top_row = tk.Frame(
            panel,
            bg=t["card"]
        )

        top_row.pack(
            fill="x",
            pady=5
        )

        # SEARCH
        self.prod_search = LabeledEntry(
            top_row,
            label="Search Product",
            width=28
        )

        self.prod_search.pack(
            side="left",
            padx=(0, 8)
        )

        self.prod_search.entry.config(
            font=("Segoe UI", 12)
        )

        self.prod_search.entry.bind(
            "<KeyRelease>",
            self._search_products
        )

        # QUANTITY
        qty_frame = tk.Frame(
            top_row,
            bg=t["card"]
        )

        qty_frame.pack(
            side="left",
            padx=5
        )

        tk.Label(
            qty_frame,
            text="Qty",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 11, "bold")
        ).pack()

        self.qty_var = tk.IntVar(value=1)

        tk.Spinbox(
            qty_frame,
            from_=1,
            to=9999,
            textvariable=self.qty_var,
            width=5,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat"
        ).pack()

        # ADD BUTTON
        add_btn = tk.Button(
            top_row,
            text="🛒 Add",
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 11, "bold"),
            padx=16,
            pady=9,
            command=self._add_to_cart
        )

        add_btn.pack(
            side="left",
            padx=(10, 0),
            pady=(18, 0)
        )

        # =====================================================
        # PRODUCT TABLE
        # =====================================================
        prod_frame = tk.Frame(
            panel,
            bg=t["card"]
        )

        prod_frame.pack(
            fill="both",
            expand=True,
            pady=12
        )

        cols = [
            ("product_id", "ID", 70),
            ("product_name", "Product Name", 280),
            ("quantity", "Available Stock", 130),
            ("price", "Price (₹)", 130),
        ]

        self.prod_tree = make_treeview(
            prod_frame,
            cols,
            height=13
        )

        self.prod_tree.bind(
            "<Double-1>",
            self._select_product
        )

        # =====================================================
        # PRODUCT INFO
        # =====================================================
        self.sel_info = tk.Label(
            panel,
            text="",
            bg=t["card"],
            fg="#22c55e",
            font=("Segoe UI", 12, "bold"),
            wraplength=500
        )

        self.sel_info.pack(
            anchor="w",
            pady=6
        )

        self._selected_prod = None

        self._refresh_prod_list()

    # =========================================================
    # RIGHT PANEL
    # =========================================================
    def _build_right(self, panel):

        t = self.t

        header = tk.Frame(
            panel,
            bg=t["bg"]
        )

        header.pack(
            fill="x",
            pady=(0, 10)
        )

        tk.Label(
            header,
            text="🛒 Cart",
            bg=t["bg"],
            fg=t["text"],
            font=("Segoe UI", 18, "bold")
        ).pack(side="left")

        DangerButton(
            header,
            text="Clear",
            command=self._clear_cart
        ).pack(side="right")

        # =====================================================
        # CART TABLE
        # =====================================================
        cart_frame = tk.Frame(
            panel,
            bg=t["card"]
        )

        cart_frame.pack(
            fill="both",
            expand=True
        )

        cols = [
            ("product_name", "Product Name", 220),
            ("quantity", "Qty", 70),
            ("price", "Unit Price", 110),
            ("subtotal", "Total Price", 120),
        ]

        self.cart_tree = make_treeview(
            cart_frame,
            cols,
            height=15
        )

        self.cart_tree.bind(
            "<Delete>",
            self._remove_cart_item
        )

        # =====================================================
        # TOTAL
        # =====================================================
        total_card = tk.Frame(
            panel,
            bg="#1e293b",
            padx=20,
            pady=15
        )

        total_card.pack(
            fill="x",
            pady=10
        )

        tk.Label(
            total_card,
            text="GRAND TOTAL",
            bg="#1e293b",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(side="left")

        self.total_label = tk.Label(
            total_card,
            text="₹ 0.00",
            bg="#1e293b",
            fg="#22c55e",
            font=("Segoe UI", 24, "bold")
        )

        self.total_label.pack(side="right")

        # =====================================================
        # BUTTONS
        # =====================================================
        btn_frame = tk.Frame(
            panel,
            bg=t["bg"]
        )

        btn_frame.pack(
            fill="x",
            pady=8
        )

        generate_btn = tk.Button(
            btn_frame,
            text="🖨 Generate Bill",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 13, "bold"),
            padx=22,
            pady=12,
            command=self._generate_bill
        )

        generate_btn.pack(
            side="left",
            padx=(0, 10)
        )

        new_btn = tk.Button(
            btn_frame,
            text="📝 New Bill",
            bg="#475569",
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 12, "bold"),
            padx=20,
            pady=12,
            command=self._new_bill
        )

        new_btn.pack(side="left")

    # =========================================================
    # SEARCH PRODUCTS
    # =========================================================
    def _search_products(self, event=None):

        q = self.prod_search.get()

        if q:
            rows = search_products(q)
        else:
            rows = get_all_products()

        self._load_prod_tree(rows)

    # =========================================================
    # REFRESH PRODUCT LIST
    # =========================================================
    def _refresh_prod_list(self):

        rows = get_all_products()

        self._load_prod_tree(rows)

    # =========================================================
    # LOAD PRODUCT TABLE
    # =========================================================
    def _load_prod_tree(self, rows):

        self.prod_tree.delete(*self.prod_tree.get_children())

        for r in rows:

            tag = ""

            if r["quantity"] == 0:
                tag = "out"

            elif r["quantity"] <= 5:
                tag = "low"

            self.prod_tree.insert(
                "",
                "end",
                values=(
                    r["product_id"],
                    r["product_name"],
                    r["quantity"],
                    f"₹ {r['price']:.2f}"
                ),
                tags=(tag,)
            )

        self.prod_tree.tag_configure(
            "out",
            foreground="#ef4444"
        )

        self.prod_tree.tag_configure(
            "low",
            foreground="#f59e0b"
        )

    # =========================================================
    # SELECT PRODUCT
    # =========================================================
    def _select_product(self, event=None):

        selected = self.prod_tree.selection()

        if not selected:
            return

        vals = self.prod_tree.item(
            selected[0],
            "values"
        )

        pid = int(vals[0])

        prod = get_product_by_id(pid)

        if not prod:
            return

        self._selected_prod = prod

        # AUTO FILL SEARCH
        self.prod_search.clear()

        self.prod_search.entry.insert(
            0,
            prod["product_name"]
        )

        self.sel_info.config(
            text=(
                f"✅ Selected: {prod['product_name']}   |   "
                f"Stock: {prod['quantity']}   |   "
                f"Price: ₹ {prod['price']}"
            )
        )

    # =========================================================
    # ADD TO CART
    # =========================================================
    def _add_to_cart(self):

        if not self._selected_prod:

            messagebox.showwarning(
                "Warning",
                "Please select product first"
            )

            return

        qty = self.qty_var.get()

        if qty <= 0:

            messagebox.showwarning(
                "Warning",
                "Quantity must be greater than 0"
            )

            return

        # CHECK ALREADY ADDED QTY
        already_in_cart = 0

        for item in self._cart:

            if item["product_id"] == self._selected_prod["product_id"]:

                already_in_cart += item["quantity"]

        available_stock = self._selected_prod["quantity"]

        if already_in_cart + qty > available_stock:

            remaining = available_stock - already_in_cart

            messagebox.showwarning(
                "Stock Error",
                f"Only {remaining} item(s) remaining in stock"
            )

            return

        # UPDATE EXISTING ITEM
        for item in self._cart:

            if item["product_id"] == self._selected_prod["product_id"]:

                item["quantity"] += qty

                item["subtotal"] = (
                    item["quantity"] * item["price"]
                )

                self._refresh_cart()

                self.sel_info.config(
                    text=f"✅ Added More: {self._selected_prod['product_name']}"
                )

                return

        # NEW ENTRY
        subtotal = qty * self._selected_prod["price"]

        self._cart.append({

            "product_id": self._selected_prod["product_id"],

            "product_name": self._selected_prod["product_name"],

            "quantity": qty,

            "price": self._selected_prod["price"],

            "subtotal": subtotal
        })

        self._refresh_cart()

        self.sel_info.config(
            text=f"✅ Added: {self._selected_prod['product_name']}"
        )

    # =========================================================
    # REFRESH CART
    # =========================================================
    def _refresh_cart(self):

        self.cart_tree.delete(*self.cart_tree.get_children())

        total = 0

        for item in self._cart:

            total += item["subtotal"]

            self.cart_tree.insert(
                "",
                "end",
                values=(
                    item["product_name"],
                    item["quantity"],
                    f"₹ {item['price']:.2f}",
                    f"₹ {item['subtotal']:.2f}"
                )
            )

        self.total_label.config(
            text=f"₹ {total:,.2f}"
        )

    # =========================================================
    # REMOVE CART ITEM
    # =========================================================
    def _remove_cart_item(self, event=None):

        selected = self.cart_tree.selection()

        if not selected:
            return

        idx = self.cart_tree.index(selected[0])

        self._cart.pop(idx)

        self._refresh_cart()

    # =========================================================
    # CLEAR CART
    # =========================================================
    def _clear_cart(self):

        self._cart.clear()

        self._refresh_cart()

    # =========================================================
    # GENERATE BILL
    # =========================================================
    def _generate_bill(self):

        customer = self.f_cust.get()

        if not customer:

            messagebox.showwarning(
                "Warning",
                "Enter Customer Name"
            )

            return

        if not self._cart:

            messagebox.showwarning(
                "Warning",
                "Cart is Empty"
            )

            return

        items = []

        for item in self._cart:

            items.append({
                "product_id": item["product_id"],
                "quantity": item["quantity"]
            })

        try:

            bill_data = create_bill(
                customer_name=customer,
                phone=self.f_phone.get(),
                address=self.f_addr.get(),
                items=items
            )

            messagebox.showinfo(
                "Success",
                "Bill Generated Successfully"
            )

            self._show_bill_popup(bill_data)

            self._new_bill()

            self._refresh_prod_list()

            if self.on_bill_created:
                self.on_bill_created()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # SHOW BILL POPUP
    # =========================================================
    def _show_bill_popup(self, bill_data):

        popup = tk.Toplevel(self)

        popup.title("Bill Preview")

        popup.geometry("500x600")

        popup.configure(bg=self.t["bg"])

        tk.Label(
            popup,
            text="📚 Binod Book Binding",
            bg=self.t["bg"],
            fg=self.t["text"],
            font=("Segoe UI", 22, "bold")
        ).pack(pady=10)

        text = tk.Text(
            popup,
            font=("Consolas", 11),
            bg=self.t["card"],
            fg=self.t["text"]
        )

        text.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        bill_text = ""

        bill_text += f"Bill No: {bill_data['bill_number']}\n"
        bill_text += f"Customer: {bill_data['customer_name']}\n\n"

        for item in bill_data["items"]:

            bill_text += (
                f"{item['product_name']} "
                f"x {item['quantity']} = "
                f"₹ {item['subtotal']}\n"
            )

        bill_text += "\n"
        bill_text += f"Grand Total: ₹ {bill_data['grand_total']}"

        text.insert("1.0", bill_text)

        def export_pdf():

            path = generate_pdf_bill(bill_data)

            open_file(path)

        tk.Button(
            popup,
            text="Export PDF",
            bg="#2563eb",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=export_pdf
        ).pack(pady=10)

    # =========================================================
    # NEW BILL
    # =========================================================
    def _new_bill(self):

        self._cart.clear()

        self._refresh_cart()

        self.f_cust.clear()
        self.f_phone.clear()
        self.f_addr.clear()

        self.sel_info.config(text="")

    # =========================================================
    # REFRESH
    # =========================================================
    def refresh(self):

        self._refresh_prod_list()