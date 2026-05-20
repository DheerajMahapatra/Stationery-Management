# # billing_module/billing_page.py
# # PROFESSIONAL POS BILLING UI - FINAL UPGRADED VERSION WITH AUTO STOCK UPDATE

# import tkinter as tk
# from tkinter import messagebox, ttk
# from datetime import datetime

# from assets.theme import get as T, FONTS

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

#     def __init__(
#         self,
#         master,
#         root_ref=None,
#         on_bill_created=None,
#         **kwargs
#     ):

#         self.t = T()

#         super().__init__(
#             master,
#             bg=self.t["bg"],
#             **kwargs
#         )

#         self.root_ref = root_ref
#         self.on_bill_created = on_bill_created

#         self._cart = []
#         self._selected_prod = None
#         self._bill_counter = 1  # Bill number counter

#         self._build()
        
#         # Start auto-refresh for product list
#         self._auto_refresh_products()

#     # =========================================================
#     # BUILD UI
#     # =========================================================
#     def _build(self):

#         t = self.t

#         main = tk.Frame(self, bg=t["bg"])
#         main.pack(fill="both", expand=True, padx=18, pady=15)

#         # HEADER
#         header = tk.Frame(main, bg=t["bg"])
#         header.pack(fill="x", pady=(0, 15))

#         tk.Label(
#             header,
#             text="🧾 Billing / Point Of Sale",
#             font=("Segoe UI", 26, "bold"),
#             bg=t["bg"],
#             fg=t["text"]
#         ).pack(anchor="w")

#         tk.Label(
#             header,
#             text="Professional Billing Management System",
#             font=("Segoe UI", 11),
#             bg=t["bg"],
#             fg=t["text2"]
#         ).pack(anchor="w")

#         # BODY
#         body = tk.Frame(main, bg=t["bg"])
#         body.pack(fill="both", expand=True)

#         body.grid_columnconfigure(0, weight=4)
#         body.grid_columnconfigure(1, weight=3)
#         body.grid_rowconfigure(0, weight=1)

#         # LEFT PANEL
#         left = tk.Frame(
#             body,
#             bg=t["card"],
#             bd=0,
#             highlightthickness=1,
#             highlightbackground=t["border"]
#         )

#         left.grid(
#             row=0,
#             column=0,
#             sticky="nsew",
#             padx=(0, 12)
#         )

#         # RIGHT PANEL
#         right = tk.Frame(
#             body,
#             bg=t["card"],
#             bd=0,
#             highlightthickness=1,
#             highlightbackground=t["border"]
#         )

#         right.grid(
#             row=0,
#             column=1,
#             sticky="nsew"
#         )

#         self._build_left(left)
#         self._build_right(right)

#     # =========================================================
#     # LEFT PANEL
#     # =========================================================
#     def _build_left(self, panel):

#         t = self.t

#         inner = tk.Frame(panel, bg=t["card"])
#         inner.pack(fill="both", expand=True, padx=18, pady=18)

#         # =====================================================
#         # CUSTOMER SECTION
#         # =====================================================

#         tk.Label(
#             inner,
#             text="👤 Customer Information",
#             font=("Segoe UI", 18, "bold"),
#             bg=t["card"],
#             fg=t["accent"]
#         ).pack(anchor="w", pady=(0, 14))

#         customer_grid = tk.Frame(inner, bg=t["card"])
#         customer_grid.pack(fill="x")

#         customer_grid.grid_columnconfigure(0, weight=1)
#         customer_grid.grid_columnconfigure(1, weight=1)

#         # CUSTOMER NAME
#         tk.Label(
#             customer_grid,
#             text="Customer Name *",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10, "bold")
#         ).grid(row=0, column=0, sticky="w", pady=(0, 4))

#         self.f_cust = tk.Entry(
#             customer_grid,
#             font=("Segoe UI", 12),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat",
#             insertbackground=t["text"]
#         )

#         self.f_cust.grid(
#             row=1,
#             column=0,
#             sticky="ew",
#             padx=(0, 8),
#             ipady=8
#         )

#         # PHONE
#         tk.Label(
#             customer_grid,
#             text="Phone Number",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10, "bold")
#         ).grid(row=0, column=1, sticky="w", pady=(0, 4))

#         self.f_phone = tk.Entry(
#             customer_grid,
#             font=("Segoe UI", 12),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat",
#             insertbackground=t["text"]
#         )

#         self.f_phone.grid(
#             row=1,
#             column=1,
#             sticky="ew",
#             ipady=8
#         )

#         # ADDRESS
#         tk.Label(
#             customer_grid,
#             text="Address",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10, "bold")
#         ).grid(
#             row=2,
#             column=0,
#             sticky="w",
#             pady=(12, 4)
#         )

#         self.f_addr = tk.Entry(
#             customer_grid,
#             font=("Segoe UI", 12),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat",
#             insertbackground=t["text"]
#         )

#         self.f_addr.grid(
#             row=3,
#             column=0,
#             columnspan=2,
#             sticky="ew",
#             ipady=8
#         )

#         # SEPARATOR
#         tk.Frame(
#             inner,
#             bg=t["border"],
#             height=1
#         ).pack(fill="x", pady=20)

#         # =====================================================
#         # PRODUCT SECTION
#         # =====================================================

#         tk.Label(
#             inner,
#             text="📦 Add Product",
#             font=("Segoe UI", 18, "bold"),
#             bg=t["card"],
#             fg=t["accent"]
#         ).pack(anchor="w", pady=(0, 12))

#         action_row = tk.Frame(inner, bg=t["card"])
#         action_row.pack(fill="x", pady=(0, 12))

#         # SEARCH
#         search_frame = tk.Frame(action_row, bg=t["card"])
#         search_frame.pack(side="left", fill="x", expand=True)

#         tk.Label(
#             search_frame,
#             text="Search Product",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10, "bold")
#         ).pack(anchor="w", pady=(0, 4))

#         self.prod_search = tk.Entry(
#             search_frame,
#             font=("Segoe UI", 12),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat",
#             insertbackground=t["text"]
#         )

#         self.prod_search.pack(
#             fill="x",
#             ipady=8,
#             padx=(0, 10)
#         )

#         self.prod_search.bind("<KeyRelease>", self._search_products)

#         # QUANTITY
#         qty_frame = tk.Frame(action_row, bg=t["card"])
#         qty_frame.pack(side="left", padx=(0, 10))

#         tk.Label(
#             qty_frame,
#             text="Qty",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10, "bold")
#         ).pack(anchor="w", pady=(0, 4))

#         self.qty_var = tk.IntVar(value=1)

#         self.qty_spinbox = tk.Spinbox(
#             qty_frame,
#             from_=1,
#             to=999,
#             width=6,
#             textvariable=self.qty_var,
#             font=("Segoe UI", 12),
#             bg=t["entry_bg"],
#             fg=t["entry_fg"],
#             relief="flat",
#             justify="center"
#         )

#         self.qty_spinbox.pack(ipady=6)

#         # ADD BUTTON
#         add_btn_frame = tk.Frame(action_row, bg=t["card"])
#         add_btn_frame.pack(side="left")

#         tk.Label(
#             add_btn_frame,
#             text="",
#             bg=t["card"]
#         ).pack(pady=(0, 4))

#         self.add_btn = tk.Button(
#             add_btn_frame,
#             text="➕ Add",
#             bg="#16a34a",
#             fg="white",
#             activebackground="#15803d",
#             activeforeground="white",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 11, "bold"),
#             padx=18,
#             pady=9,
#             command=self._add_to_cart
#         )

#         self.add_btn.pack()

#         # PRODUCT INFO
#         self.sel_info = tk.Label(
#             inner,
#             text="Double-click product to select",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 10)
#         )

#         self.sel_info.pack(anchor="w", pady=(8, 10))

#         # =====================================================
#         # PRODUCT TABLE
#         # =====================================================

#         table_frame = tk.Frame(inner, bg=t["card"])
#         table_frame.pack(fill="both", expand=True)

#         columns = (
#             "id",
#             "product",
#             "stock",
#             "price"
#         )

#         style = ttk.Style()

#         style.theme_use("default")

#         style.configure(
#             "Custom.Treeview",
#             background="#ffffff",
#             foreground="#111827",
#             rowheight=32,
#             fieldbackground="#ffffff",
#             borderwidth=0,
#             font=("Segoe UI", 10)
#         )

#         style.configure(
#             "Custom.Treeview.Heading",
#             background="#374151",
#             foreground="white",
#             relief="flat",
#             font=("Segoe UI", 10, "bold")
#         )

#         style.map(
#             "Custom.Treeview",
#             background=[("selected", "#2563eb")],
#             foreground=[("selected", "white")]
#         )

#         self.prod_tree = ttk.Treeview(
#             table_frame,
#             columns=columns,
#             show="headings",
#             height=12,
#             style="Custom.Treeview"
#         )

#         self.prod_tree.heading("id", text="ID")
#         self.prod_tree.heading("product", text="Product Name")
#         self.prod_tree.heading("stock", text="Stock")
#         self.prod_tree.heading("price", text="Price")

#         self.prod_tree.column("id", width=60, anchor="center")
#         self.prod_tree.column("product", width=280)
#         self.prod_tree.column("stock", width=90, anchor="center")
#         self.prod_tree.column("price", width=120, anchor="center")

#         scrollbar = ttk.Scrollbar(
#             table_frame,
#             orient="vertical",
#             command=self.prod_tree.yview
#         )

#         self.prod_tree.configure(
#             yscrollcommand=scrollbar.set
#         )

#         self.prod_tree.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         scrollbar.pack(
#             side="right",
#             fill="y"
#         )

#         self.prod_tree.bind(
#             "<Double-1>",
#             self._select_product
#         )

#         self._refresh_prod_list()

#     # =========================================================
#     # RIGHT PANEL
#     # =========================================================
#     def _build_right(self, panel):

#         t = self.t

#         inner = tk.Frame(panel, bg=t["card"])
#         inner.pack(fill="both", expand=True, padx=18, pady=18)

#         # HEADER
#         top = tk.Frame(inner, bg=t["card"])
#         top.pack(fill="x", pady=(0, 12))

#         tk.Label(
#             top,
#             text="🛒 Shopping Cart",
#             font=("Segoe UI", 18, "bold"),
#             bg=t["card"],
#             fg=t["accent"]
#         ).pack(side="left")

#         # Clear Cart Button
#         tk.Button(
#             top,
#             text="🗑 Clear Cart",
#             bg="#dc2626",
#             fg="white",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 10, "bold"),
#             padx=14,
#             pady=6,
#             command=self._clear_cart
#         ).pack(side="right")

#         # CART TABLE
#         cart_frame = tk.Frame(inner, bg=t["card"])
#         cart_frame.pack(fill="both", expand=True)

#         cart_columns = (
#             "product",
#             "qty",
#             "price",
#             "total"
#         )

#         self.cart_tree = ttk.Treeview(
#             cart_frame,
#             columns=cart_columns,
#             show="headings",
#             height=12,
#             style="Custom.Treeview"
#         )

#         self.cart_tree.heading("product", text="Product")
#         self.cart_tree.heading("qty", text="Qty")
#         self.cart_tree.heading("price", text="Price")
#         self.cart_tree.heading("total", text="Total")

#         self.cart_tree.column("product", width=230)
#         self.cart_tree.column("qty", width=60, anchor="center")
#         self.cart_tree.column("price", width=100, anchor="center")
#         self.cart_tree.column("total", width=120, anchor="center")

#         cart_scroll = ttk.Scrollbar(
#             cart_frame,
#             orient="vertical",
#             command=self.cart_tree.yview
#         )

#         self.cart_tree.configure(
#             yscrollcommand=cart_scroll.set
#         )

#         self.cart_tree.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         cart_scroll.pack(
#             side="right",
#             fill="y"
#         )

#         self.cart_tree.bind(
#             "<Delete>",
#             self._remove_cart_item
#         )

#         # Add right-click menu for cart items
#         self.cart_menu = tk.Menu(self, tearoff=0)
#         self.cart_menu.add_command(label="Remove Item", command=self._remove_cart_item)
#         self.cart_menu.add_command(label="Edit Quantity", command=self._edit_cart_quantity)
        
#         self.cart_tree.bind("<Button-3>", self._show_cart_menu)

#         # TOTAL CARD
#         total_card = tk.Frame(
#             inner,
#             bg="#f3f4f6",
#             bd=0
#         )

#         total_card.pack(
#             fill="x",
#             pady=15
#         )

#         total_inner = tk.Frame(
#             total_card,
#             bg="#f3f4f6"
#         )

#         total_inner.pack(
#             fill="x",
#             padx=20,
#             pady=18
#         )

#         # Item count
#         self.item_count_label = tk.Label(
#             total_inner,
#             text="Items: 0",
#             font=("Segoe UI", 11),
#             bg="#f3f4f6",
#             fg="#6b7280"
#         )
#         self.item_count_label.pack(side="left")

#         # Total amount
#         tk.Label(
#             total_inner,
#             text="GRAND TOTAL",
#             font=("Segoe UI", 15, "bold"),
#             bg="#f3f4f6",
#             fg="#111827"
#         ).pack(side="left", padx=(30, 10))

#         self.total_label = tk.Label(
#             total_inner,
#             text="₹ 0.00",
#             font=("Segoe UI", 24, "bold"),
#             bg="#f3f4f6",
#             fg="#16a34a"
#         )

#         self.total_label.pack(side="right")

#         # BUTTONS
#         btn_frame = tk.Frame(inner, bg=t["card"])
#         btn_frame.pack(fill="x")

#         self.generate_btn = tk.Button(
#             btn_frame,
#             text="🖨 Generate Bill",
#             bg="#2563eb",
#             fg="white",
#             activebackground="#1d4ed8",
#             activeforeground="white",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 12, "bold"),
#             padx=25,
#             pady=12,
#             command=self._generate_bill
#         )

#         self.generate_btn.pack(
#             side="left",
#             fill="x",
#             expand=True,
#             padx=(0, 6)
#         )

#         self.new_btn = tk.Button(
#             btn_frame,
#             text="📝 New Bill",
#             bg="#4b5563",
#             fg="white",
#             activebackground="#374151",
#             activeforeground="white",
#             relief="flat",
#             cursor="hand2",
#             font=("Segoe UI", 12, "bold"),
#             padx=25,
#             pady=12,
#             command=self._new_bill
#         )

#         self.new_btn.pack(
#             side="left",
#             fill="x",
#             expand=True,
#             padx=(6, 0)
#         )

#         # Keyboard shortcuts
#         self.bind_all("<F5>", lambda e: self._generate_bill())
#         self.bind_all("<Control-n>", lambda e: self._new_bill())
#         self.bind_all("<Control-f>", lambda e: self.prod_search.focus_set())

#     # =========================================================
#     # AUTO REFRESH PRODUCTS
#     # =========================================================
#     def _auto_refresh_products(self):
#         """Auto refresh product list every 30 seconds"""
#         self._refresh_prod_list()
#         self.after(30000, self._auto_refresh_products)  # Refresh every 30 seconds

#     # =========================================================
#     # SEARCH PRODUCTS
#     # =========================================================
#     def _search_products(self, event=None):

#         q = self.prod_search.get().strip()

#         if q:
#             rows = search_products(q)
#         else:
#             rows = get_all_products()

#         self._load_prod_tree(rows)

#     # =========================================================
#     # LOAD PRODUCT TABLE
#     # =========================================================
#     def _load_prod_tree(self, rows):

#         self.prod_tree.delete(*self.prod_tree.get_children())

#         for r in rows:
#             # Color code low stock items
#             tags = ()
#             if r["quantity"] == 0:
#                 tags = ("out_of_stock",)
#             elif r["quantity"] <= 5:
#                 tags = ("low_stock",)

#             self.prod_tree.insert(
#                 "",
#                 "end",
#                 values=(
#                     r["product_id"],
#                     r["product_name"],
#                     r["quantity"],
#                     f"₹ {r['price']:.2f}"
#                 ),
#                 tags=tags
#             )

#         # Configure tags for visual indicators
#         self.prod_tree.tag_configure("out_of_stock", foreground="red")
#         self.prod_tree.tag_configure("low_stock", foreground="orange")

#     # =========================================================
#     # REFRESH PRODUCTS
#     # =========================================================
#     def _refresh_prod_list(self):

#         rows = get_all_products()
#         self._load_prod_tree(rows)

#     # =========================================================
#     # SELECT PRODUCT
#     # =========================================================
#     def _select_product(self, event=None):

#         selected = self.prod_tree.selection()

#         if not selected:
#             return

#         vals = self.prod_tree.item(selected[0], "values")

#         pid = int(vals[0])

#         prod = get_product_by_id(pid)

#         if not prod:
#             messagebox.showerror("Error", "Product not found in database")
#             return

#         self._selected_prod = prod

#         # AUTO SHOW IN SEARCH BAR
#         self.prod_search.delete(0, tk.END)
#         self.prod_search.insert(0, prod["product_name"])

#         # Show detailed product info
#         stock_status = ""
#         if prod["quantity"] == 0:
#             stock_status = " | ⚠️ OUT OF STOCK"
#         elif prod["quantity"] <= 5:
#             stock_status = " | ⚠️ LOW STOCK"
            
#         self.sel_info.config(
#             text=f"✅ Selected: {prod['product_name']} | Stock: {prod['quantity']}{stock_status} | Price: ₹ {prod['price']:.2f}",
#             fg="#16a34a"
#         )

#         self.qty_spinbox.focus_set()
        
#         # Highlight the add button
#         self.add_btn.config(bg="#15803d")

#     # =========================================================
#     # ADD TO CART
#     # =========================================================
#     def _add_to_cart(self):

#         if not self._selected_prod:

#             messagebox.showwarning(
#                 "Warning",
#                 "⚠️ Please select a product first!\n\nDouble-click on a product from the list."
#             )

#             return

#         qty = self.qty_var.get()

#         if qty <= 0:
#             messagebox.showwarning("Warning", "Quantity must be greater than 0")
#             return

#         # Check if product is in stock
#         if self._selected_prod["quantity"] == 0:
#             messagebox.showwarning(
#                 "Out of Stock",
#                 f"❌ {self._selected_prod['product_name']} is out of stock!"
#             )
#             return

#         # Calculate already added quantity
#         already_added = 0

#         for item in self._cart:

#             if item["product_id"] == self._selected_prod["product_id"]:
#                 already_added += item["quantity"]

#         remaining_stock = self._selected_prod["quantity"] - already_added

#         if qty > remaining_stock:

#             messagebox.showwarning(
#                 "Insufficient Stock",
#                 f"⚠️ Only {remaining_stock} unit(s) remaining for:\n\n{self._selected_prod['product_name']}\n\nCurrent stock: {self._selected_prod['quantity']}\nAlready in cart: {already_added}"
#             )

#             return

#         # UPDATE EXISTING ITEM IN CART
#         for item in self._cart:

#             if item["product_id"] == self._selected_prod["product_id"]:

#                 item["quantity"] += qty
#                 item["subtotal"] = (
#                     item["quantity"] * item["price"]
#                 )

#                 self._refresh_cart()

#                 self.qty_var.set(1)
                
#                 # Reset button color
#                 self.add_btn.config(bg="#16a34a")
                
#                 # Flash effect on cart
#                 self._flash_cart()

#                 return

#         # Add new item to cart
#         subtotal = qty * self._selected_prod["price"]

#         self._cart.append({
#             "product_id": self._selected_prod["product_id"],
#             "product_name": self._selected_prod["product_name"],
#             "quantity": qty,
#             "price": self._selected_prod["price"],
#             "subtotal": subtotal
#         })

#         self._refresh_cart()

#         self.qty_var.set(1)
        
#         # Reset button color
#         self.add_btn.config(bg="#16a34a")
        
#         # Flash effect on cart
#         self._flash_cart()

#     # =========================================================
#     # FLASH CART (Visual feedback)
#     # =========================================================
#     def _flash_cart(self):
#         """Brief visual feedback when item is added to cart"""
#         original_bg = self.total_label.cget("bg")
#         self.total_label.config(bg="#10b981")
#         self.after(200, lambda: self.total_label.config(bg=original_bg))

#     # =========================================================
#     # REFRESH CART
#     # =========================================================
#     def _refresh_cart(self):

#         self.cart_tree.delete(*self.cart_tree.get_children())

#         total = 0
#         total_items = 0

#         for item in self._cart:

#             total += item["subtotal"]
#             total_items += item["quantity"]

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
        
#         # Update item count
#         self.item_count_label.config(
#             text=f"Items: {total_items}"
#         )
        
#         # Enable/disable generate button based on cart
#         if self._cart:
#             self.generate_btn.config(state="normal")
#         else:
#             self.generate_btn.config(state="disabled")

#     # =========================================================
#     # SHOW CART MENU (Right-click)
#     # =========================================================
#     def _show_cart_menu(self, event):
#         """Show right-click context menu for cart items"""
#         item = self.cart_tree.identify_row(event.y)
#         if item:
#             self.cart_tree.selection_set(item)
#             self.cart_menu.post(event.x_root, event.y_root)

#     # =========================================================
#     # REMOVE CART ITEM
#     # =========================================================
#     def _remove_cart_item(self, event=None):

#         selected = self.cart_tree.selection()

#         if not selected:
#             messagebox.showinfo("Info", "Please select an item to remove")
#             return

#         # Get item name for confirmation
#         item_values = self.cart_tree.item(selected[0], "values")
#         item_name = item_values[0]
        
#         confirm = messagebox.askyesno(
#             "Confirm Remove",
#             f"Remove '{item_name}' from cart?"
#         )
        
#         if not confirm:
#             return

#         idx = self.cart_tree.index(selected[0])

#         self._cart.pop(idx)

#         self._refresh_cart()

#     # =========================================================
#     # EDIT CART QUANTITY
#     # =========================================================
#     def _edit_cart_quantity(self):
#         """Edit quantity of selected cart item"""
#         selected = self.cart_tree.selection()
        
#         if not selected:
#             messagebox.showinfo("Info", "Please select an item to edit")
#             return
        
#         idx = self.cart_tree.index(selected[0])
#         item = self._cart[idx]
        
#         # Create edit dialog
#         dialog = tk.Toplevel(self)
#         dialog.title("Edit Quantity")
#         dialog.geometry("300x150")
#         dialog.configure(bg=self.t["bg"])
#         dialog.resizable(False, False)
        
#         tk.Label(
#             dialog,
#             text=f"Product: {item['product_name']}",
#             font=("Segoe UI", 11, "bold"),
#             bg=self.t["bg"],
#             fg=self.t["text"]
#         ).pack(pady=10)
        
#         tk.Label(
#             dialog,
#             text="New Quantity:",
#             bg=self.t["bg"],
#             fg=self.t["text"]
#         ).pack()
        
#         qty_var = tk.IntVar(value=item['quantity'])
#         qty_spin = tk.Spinbox(
#             dialog,
#             from_=1,
#             to=999,
#             textvariable=qty_var,
#             font=("Segoe UI", 11),
#             width=10
#         )
#         qty_spin.pack(pady=5)
        
#         def save_quantity():
#             new_qty = qty_var.get()
            
#             # Check stock availability
#             product = get_product_by_id(item['product_id'])
#             if product and new_qty > product['quantity']:
#                 messagebox.showwarning(
#                     "Insufficient Stock",
#                     f"Only {product['quantity']} units available in stock!"
#                 )
#                 return
            
#             item['quantity'] = new_qty
#             item['subtotal'] = new_qty * item['price']
#             self._refresh_cart()
#             dialog.destroy()
        
#         tk.Button(
#             dialog,
#             text="Save",
#             bg="#2563eb",
#             fg="white",
#             command=save_quantity,
#             font=("Segoe UI", 10, "bold"),
#             padx=20,
#             pady=5
#         ).pack(pady=10)

#     # =========================================================
#     # CLEAR CART
#     # =========================================================
#     def _clear_cart(self):
        
#         if not self._cart:
#             return
            
#         confirm = messagebox.askyesno(
#             "Clear Cart",
#             "Are you sure you want to clear all items from cart?"
#         )
        
#         if not confirm:
#             return

#         self._cart.clear()

#         self._refresh_cart()
        
#         self._refresh_prod_list()

#     # =========================================================
#     # GENERATE BILL
#     # =========================================================
#     def _generate_bill(self):

#         customer = self.f_cust.get().strip()

#         if not customer:

#             messagebox.showwarning(
#                 "Missing Information",
#                 "⚠️ Please enter customer name to generate bill."
#             )

#             self.f_cust.focus_set()
#             return

#         if not self._cart:

#             messagebox.showwarning(
#                 "Empty Cart",
#                 "⚠️ Cart is empty! Please add products first."
#             )

#             return

#         # Final stock validation before bill generation
#         for item in self._cart:
#             product = get_product_by_id(item['product_id'])
#             if product and item['quantity'] > product['quantity']:
#                 messagebox.showerror(
#                     "Stock Error",
#                     f"❌ Insufficient stock for {item['product_name']}!\n"
#                     f"Available: {product['quantity']}, Requested: {item['quantity']}\n\n"
#                     f"Please update your cart and try again."
#                 )
#                 return

#         items = []

#         for item in self._cart:

#             items.append({
#                 "product_id": item["product_id"],
#                 "quantity": item["quantity"]
#             })

#         try:
#             # Disable generate button during processing
#             self.generate_btn.config(state="disabled", text="⏳ Processing...")
#             self.update()

#             bill_data = create_bill(
#                 customer_name=customer,
#                 phone=self.f_phone.get(),
#                 address=self.f_addr.get(),
#                 items=items
#             )

#             # ============================================
#             # UPDATE PRODUCT STOCKS AFTER BILL GENERATION
#             # ============================================
#             stock_update_success = self._update_product_stocks()
            
#             if not stock_update_success:
#                 # If stock update fails, show warning but continue
#                 messagebox.showwarning(
#                     "Stock Update Warning",
#                     "Bill was generated successfully, but there was an issue updating product stocks.\n"
#                     "Please check product quantities manually."
#                 )

#             messagebox.showinfo(
#                 "Success",
#                 f"✅ Bill Generated Successfully!\n\n"
#                 f"Bill Number: {bill_data.get('bill_number', 'N/A')}\n"
#                 f"Customer: {customer}\n"
#                 f"Total Items: {sum(item['quantity'] for item in self._cart)}\n"
#                 f"Grand Total: ₹ {bill_data.get('grand_total', 0):,.2f}"
#             )

#             self._show_bill_popup(bill_data)

#             # Increment bill counter
#             self._bill_counter += 1

#             # Reset for new bill
#             self._new_bill()

#             self._refresh_prod_list()

#             # Callback to notify main application
#             if self.on_bill_created:
#                 self.on_bill_created()

#         except Exception as e:

#             messagebox.showerror(
#                 "Bill Generation Failed",
#                 f"❌ Error generating bill:\n\n{str(e)}\n\n"
#                 f"Please try again or contact support."
#             )
            
#         finally:
#             # Re-enable generate button
#             self.generate_btn.config(state="normal", text="🖨 Generate Bill")

#     # =========================================================
#     # UPDATE PRODUCT STOCKS
#     # =========================================================
#     def _update_product_stocks(self):
#         """
#         Update product stocks after successful bill generation.
#         Connects to ProductsPage to update quantities in real-time.
        
#         Returns:
#             bool: True if all stocks updated successfully, False otherwise
#         """
#         try:
#             # Get reference to ProductsPage through root_ref
#             if not self.root_ref:
#                 print("⚠️ No root reference found for stock update")
#                 return False
            
#             products_page = self.root_ref.pages.get("products")
            
#             if not products_page:
#                 print("⚠️ Products page not found for stock update")
#                 return False
            
#             success_count = 0
#             fail_count = 0
            
#             # Update stock for each item in cart
#             for item in self._cart:
#                 product_id = item["product_id"]
#                 quantity_sold = item["quantity"]
                
#                 # Call the ProductsPage method to update stock
#                 update_success = products_page.update_stock_after_purchase(
#                     product_id, 
#                     quantity_sold
#                 )
                
#                 if update_success:
#                     success_count += 1
#                     print(f"✅ Stock updated: Product {product_id} - Sold {quantity_sold}")
#                 else:
#                     fail_count += 1
#                     print(f"❌ Failed to update stock: Product {product_id}")
            
#             # Also try to refresh billing page product list
#             self._refresh_prod_list()
            
#             if fail_count > 0:
#                 print(f"⚠️ {fail_count} product(s) failed to update stock")
#                 return False
            
#             print(f"✅ All {success_count} products updated successfully")
#             return True
            
#         except Exception as e:
#             print(f"❌ Error updating stocks: {e}")
#             return False

#     # =========================================================
#     # SHOW BILL POPUP
#     # =========================================================
#     def _show_bill_popup(self, bill_data):

#         popup = tk.Toplevel(self)

#         popup.title(f"Bill Preview - {bill_data.get('bill_number', 'N/A')}")
#         popup.geometry("550x700")

#         popup.configure(bg=self.t["bg"])
        
#         # Make popup modal
#         popup.transient(self)
#         popup.grab_set()

#         # Header
#         tk.Label(
#             popup,
#             text="📚 BINOD BOOK BINDING",
#             bg=self.t["bg"],
#             fg=self.t["text"],
#             font=("Segoe UI", 22, "bold")
#         ).pack(pady=12)

#         tk.Label(
#             popup,
#             text="Professional Book Binding Services",
#             bg=self.t["bg"],
#             fg=self.t["text2"],
#             font=("Segoe UI", 10)
#         ).pack()

#         # Separator
#         tk.Frame(popup, bg=self.t["border"], height=2).pack(fill="x", padx=20, pady=10)

#         # Bill Details Frame
#         details_frame = tk.Frame(popup, bg=self.t["bg"])
#         details_frame.pack(fill="x", padx=30, pady=5)

#         tk.Label(
#             details_frame,
#             text=f"Bill No: {bill_data.get('bill_number', 'N/A')}",
#             bg=self.t["bg"],
#             fg=self.t["text"],
#             font=("Segoe UI", 11, "bold")
#         ).pack(anchor="w")

#         tk.Label(
#             details_frame,
#             text=f"Date: {bill_data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}",
#             bg=self.t["bg"],
#             fg=self.t["text2"],
#             font=("Segoe UI", 10)
#         ).pack(anchor="w")

#         tk.Label(
#             details_frame,
#             text=f"Customer: {bill_data.get('customer_name', 'N/A')}",
#             bg=self.t["bg"],
#             fg=self.t["text"],
#             font=("Segoe UI", 11)
#         ).pack(anchor="w")

#         if bill_data.get('phone'):
#             tk.Label(
#                 details_frame,
#                 text=f"Phone: {bill_data.get('phone', '')}",
#                 bg=self.t["bg"],
#                 fg=self.t["text2"],
#                 font=("Segoe UI", 10)
#             ).pack(anchor="w")

#         if bill_data.get('address'):
#             tk.Label(
#                 details_frame,
#                 text=f"Address: {bill_data.get('address', '')}",
#                 bg=self.t["bg"],
#                 fg=self.t["text2"],
#                 font=("Segoe UI", 10)
#             ).pack(anchor="w")

#         # Separator
#         tk.Frame(popup, bg=self.t["border"], height=1).pack(fill="x", padx=20, pady=10)

#         # Items List
#         text = tk.Text(
#             popup,
#             font=("Consolas", 11),
#             bg="white",
#             fg="black",
#             wrap=tk.WORD
#         )

#         text.pack(
#             fill="both",
#             expand=True,
#             padx=25,
#             pady=10
#         )

#         # Format bill text
#         bill_text = "ITEMS:\n"
#         bill_text += "=" * 50 + "\n\n"

#         for i, item in enumerate(bill_data.get("items", []), 1):
#             bill_text += f"{i}. {item['product_name']}\n"
#             bill_text += f"   {item['quantity']} x ₹ {item.get('price', 0):,.2f}"
#             bill_text += f" = ₹ {item['subtotal']:,.2f}\n\n"

#         bill_text += "=" * 50 + "\n"
#         bill_text += f"GRAND TOTAL: ₹ {bill_data.get('grand_total', 0):,.2f}\n"
#         bill_text += "=" * 50 + "\n\n"
#         bill_text += "Thank you for your business! 🙏\n"
#         bill_text += "Visit again!"

#         text.insert("1.0", bill_text)
#         text.config(state="disabled")  # Make read-only

#         # Buttons Frame
#         button_frame = tk.Frame(popup, bg=self.t["bg"])
#         button_frame.pack(pady=15)

#         def export_pdf():
#             try:
#                 path = generate_pdf_bill(bill_data)
#                 if path:
#                     open_file(path)
#                     messagebox.showinfo("Success", f"PDF exported successfully!\n\nLocation: {path}")
#                 else:
#                     messagebox.showerror("Error", "Failed to generate PDF")
#             except Exception as e:
#                 messagebox.showerror("PDF Error", f"Failed to export PDF:\n{str(e)}")

#         # Export PDF Button
#         tk.Button(
#             button_frame,
#             text="📄 Export PDF",
#             bg="#2563eb",
#             fg="white",
#             activebackground="#1d4ed8",
#             font=("Segoe UI", 11, "bold"),
#             relief="flat",
#             padx=20,
#             pady=10,
#             cursor="hand2",
#             command=export_pdf
#         ).pack(side="left", padx=5)

#         # Print Button (if printer available)
#         tk.Button(
#             button_frame,
#             text="🖨 Print",
#             bg="#059669",
#             fg="white",
#             activebackground="#047857",
#             font=("Segoe UI", 11, "bold"),
#             relief="flat",
#             padx=20,
#             pady=10,
#             cursor="hand2",
#             command=lambda: messagebox.showinfo("Print", "Print functionality coming soon!")
#         ).pack(side="left", padx=5)

#         # Close Button
#         tk.Button(
#             button_frame,
#             text="✖ Close",
#             bg="#6b7280",
#             fg="white",
#             activebackground="#4b5563",
#             font=("Segoe UI", 11, "bold"),
#             relief="flat",
#             padx=20,
#             pady=10,
#             cursor="hand2",
#             command=popup.destroy
#         ).pack(side="left", padx=5)

#     # =========================================================
#     # NEW BILL
#     # =========================================================
#     def _new_bill(self):

#         self._cart.clear()

#         self._refresh_cart()

#         self.f_cust.delete(0, tk.END)
#         self.f_phone.delete(0, tk.END)
#         self.f_addr.delete(0, tk.END)

#         self.prod_search.delete(0, tk.END)

#         self.sel_info.config(
#             text="Double-click product to select",
#             fg=self.t["text2"]
#         )

#         self._selected_prod = None
        
#         # Reset button color
#         self.add_btn.config(bg="#16a34a")

#         self._refresh_prod_list()
        
#         # Focus on customer name
#         self.f_cust.focus_set()

#     # =========================================================
#     # REFRESH (Called externally)
#     # =========================================================
#     def refresh(self):

#         self._refresh_prod_list()
        
#         # Also refresh cart if any products were updated
#         if self._cart:
#             self._refresh_cart()




















# billing_module/billing_page.py
# PROFESSIONAL POS BILLING UI - FINAL UPGRADED VERSION WITH AUTO STOCK UPDATE (FIXED)

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from assets.theme import get as T, FONTS

from product_module.product_ops import (
    get_all_products,
    search_products,
    get_product_by_id,
    update_product          # <-- ADDED for direct stock update
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
        self._selected_prod = None
        self._bill_counter = 1  # Bill number counter

        self._build()
        
        # Start auto-refresh for product list
        self._auto_refresh_products()

    # =========================================================
    # BUILD UI  (unchanged, kept exactly as your last version)
    # =========================================================
    def _build(self):
        t = self.t
        main = tk.Frame(self, bg=t["bg"])
        main.pack(fill="both", expand=True, padx=18, pady=15)

        # HEADER
        header = tk.Frame(main, bg=t["bg"])
        header.pack(fill="x", pady=(0, 15))
        tk.Label(header, text="🧾 Billing / Point Of Sale", font=("Segoe UI", 26, "bold"), bg=t["bg"], fg=t["text"]).pack(anchor="w")
        tk.Label(header, text="Professional Billing Management System", font=("Segoe UI", 11), bg=t["bg"], fg=t["text2"]).pack(anchor="w")

        # BODY
        body = tk.Frame(main, bg=t["bg"])
        body.pack(fill="both", expand=True)
        body.grid_columnconfigure(0, weight=4)
        body.grid_columnconfigure(1, weight=3)
        body.grid_rowconfigure(0, weight=1)

        # LEFT PANEL
        left = tk.Frame(body, bg=t["card"], bd=0, highlightthickness=1, highlightbackground=t["border"])
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        # RIGHT PANEL
        right = tk.Frame(body, bg=t["card"], bd=0, highlightthickness=1, highlightbackground=t["border"])
        right.grid(row=0, column=1, sticky="nsew")

        self._build_left(left)
        self._build_right(right)

    # =========================================================
    # LEFT PANEL
    # =========================================================
    def _build_left(self, panel):
        t = self.t
        inner = tk.Frame(panel, bg=t["card"])
        inner.pack(fill="both", expand=True, padx=18, pady=18)

        # CUSTOMER SECTION
        tk.Label(inner, text="👤 Customer Information", font=("Segoe UI", 18, "bold"), bg=t["card"], fg=t["accent"]).pack(anchor="w", pady=(0, 14))
        customer_grid = tk.Frame(inner, bg=t["card"])
        customer_grid.pack(fill="x")
        customer_grid.grid_columnconfigure(0, weight=1)
        customer_grid.grid_columnconfigure(1, weight=1)

        tk.Label(customer_grid, text="Customer Name *", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.f_cust = tk.Entry(customer_grid, font=("Segoe UI", 12), bg=t["entry_bg"], fg=t["entry_fg"], relief="flat", insertbackground=t["text"])
        self.f_cust.grid(row=1, column=0, sticky="ew", padx=(0, 8), ipady=8)

        tk.Label(customer_grid, text="Phone Number", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10, "bold")).grid(row=0, column=1, sticky="w", pady=(0, 4))
        self.f_phone = tk.Entry(customer_grid, font=("Segoe UI", 12), bg=t["entry_bg"], fg=t["entry_fg"], relief="flat", insertbackground=t["text"])
        self.f_phone.grid(row=1, column=1, sticky="ew", ipady=8)

        tk.Label(customer_grid, text="Address", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w", pady=(12, 4))
        self.f_addr = tk.Entry(customer_grid, font=("Segoe UI", 12), bg=t["entry_bg"], fg=t["entry_fg"], relief="flat", insertbackground=t["text"])
        self.f_addr.grid(row=3, column=0, columnspan=2, sticky="ew", ipady=8)

        tk.Frame(inner, bg=t["border"], height=1).pack(fill="x", pady=20)

        # PRODUCT SECTION
        tk.Label(inner, text="📦 Add Product", font=("Segoe UI", 18, "bold"), bg=t["card"], fg=t["accent"]).pack(anchor="w", pady=(0, 12))
        action_row = tk.Frame(inner, bg=t["card"])
        action_row.pack(fill="x", pady=(0, 12))

        # SEARCH
        search_frame = tk.Frame(action_row, bg=t["card"])
        search_frame.pack(side="left", fill="x", expand=True)
        tk.Label(search_frame, text="Search Product", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 4))
        self.prod_search = tk.Entry(search_frame, font=("Segoe UI", 12), bg=t["entry_bg"], fg=t["entry_fg"], relief="flat", insertbackground=t["text"])
        self.prod_search.pack(fill="x", ipady=8, padx=(0, 10))
        self.prod_search.bind("<KeyRelease>", self._search_products)

        # QUANTITY
        qty_frame = tk.Frame(action_row, bg=t["card"])
        qty_frame.pack(side="left", padx=(0, 10))
        tk.Label(qty_frame, text="Qty", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 4))
        self.qty_var = tk.IntVar(value=1)
        self.qty_spinbox = tk.Spinbox(qty_frame, from_=1, to=999, width=6, textvariable=self.qty_var, font=("Segoe UI", 12), bg=t["entry_bg"], fg=t["entry_fg"], relief="flat", justify="center")
        self.qty_spinbox.pack(ipady=6)

        # ADD BUTTON
        add_btn_frame = tk.Frame(action_row, bg=t["card"])
        add_btn_frame.pack(side="left")
        tk.Label(add_btn_frame, text="", bg=t["card"]).pack(pady=(0, 4))
        self.add_btn = tk.Button(add_btn_frame, text="➕ Add", bg="#16a34a", fg="white", activebackground="#15803d", activeforeground="white", relief="flat", cursor="hand2", font=("Segoe UI", 11, "bold"), padx=18, pady=9, command=self._add_to_cart)
        self.add_btn.pack()

        self.sel_info = tk.Label(inner, text="Double-click product to select", bg=t["card"], fg=t["text2"], font=("Segoe UI", 10))
        self.sel_info.pack(anchor="w", pady=(8, 10))

        # PRODUCT TABLE
        table_frame = tk.Frame(inner, bg=t["card"])
        table_frame.pack(fill="both", expand=True)

        columns = ("id", "product", "stock", "price")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview", background="#ffffff", foreground="#111827", rowheight=32, fieldbackground="#ffffff", borderwidth=0, font=("Segoe UI", 10))
        style.configure("Custom.Treeview.Heading", background="#374151", foreground="white", relief="flat", font=("Segoe UI", 10, "bold"))
        style.map("Custom.Treeview", background=[("selected", "#2563eb")], foreground=[("selected", "white")])

        self.prod_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12, style="Custom.Treeview")
        self.prod_tree.heading("id", text="ID")
        self.prod_tree.heading("product", text="Product Name")
        self.prod_tree.heading("stock", text="Stock")
        self.prod_tree.heading("price", text="Price")
        self.prod_tree.column("id", width=60, anchor="center")
        self.prod_tree.column("product", width=280)
        self.prod_tree.column("stock", width=90, anchor="center")
        self.prod_tree.column("price", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.prod_tree.yview)
        self.prod_tree.configure(yscrollcommand=scrollbar.set)
        self.prod_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.prod_tree.bind("<Double-1>", self._select_product)

        self._refresh_prod_list()

    # =========================================================
    # RIGHT PANEL
    # =========================================================
    def _build_right(self, panel):
        t = self.t
        inner = tk.Frame(panel, bg=t["card"])
        inner.pack(fill="both", expand=True, padx=18, pady=18)

        # HEADER
        top = tk.Frame(inner, bg=t["card"])
        top.pack(fill="x", pady=(0, 12))
        tk.Label(top, text="🛒 Shopping Cart", font=("Segoe UI", 18, "bold"), bg=t["card"], fg=t["accent"]).pack(side="left")
        tk.Button(top, text="🗑 Clear Cart", bg="#dc2626", fg="white", relief="flat", cursor="hand2", font=("Segoe UI", 10, "bold"), padx=14, pady=6, command=self._clear_cart).pack(side="right")

        # CART TABLE
        cart_frame = tk.Frame(inner, bg=t["card"])
        cart_frame.pack(fill="both", expand=True)

        cart_columns = ("product", "qty", "price", "total")
        self.cart_tree = ttk.Treeview(cart_frame, columns=cart_columns, show="headings", height=12, style="Custom.Treeview")
        self.cart_tree.heading("product", text="Product")
        self.cart_tree.heading("qty", text="Qty")
        self.cart_tree.heading("price", text="Price")
        self.cart_tree.heading("total", text="Total")
        self.cart_tree.column("product", width=230)
        self.cart_tree.column("qty", width=60, anchor="center")
        self.cart_tree.column("price", width=100, anchor="center")
        self.cart_tree.column("total", width=120, anchor="center")

        cart_scroll = ttk.Scrollbar(cart_frame, orient="vertical", command=self.cart_tree.yview)
        self.cart_tree.configure(yscrollcommand=cart_scroll.set)
        self.cart_tree.pack(side="left", fill="both", expand=True)
        cart_scroll.pack(side="right", fill="y")
        self.cart_tree.bind("<Delete>", self._remove_cart_item)

        # Right-click menu
        self.cart_menu = tk.Menu(self, tearoff=0)
        self.cart_menu.add_command(label="Remove Item", command=self._remove_cart_item)
        self.cart_menu.add_command(label="Edit Quantity", command=self._edit_cart_quantity)
        self.cart_tree.bind("<Button-3>", self._show_cart_menu)

        # TOTAL CARD
        total_card = tk.Frame(inner, bg="#f3f4f6", bd=0)
        total_card.pack(fill="x", pady=15)
        total_inner = tk.Frame(total_card, bg="#f3f4f6")
        total_inner.pack(fill="x", padx=20, pady=18)
        self.item_count_label = tk.Label(total_inner, text="Items: 0", font=("Segoe UI", 11), bg="#f3f4f6", fg="#6b7280")
        self.item_count_label.pack(side="left")
        tk.Label(total_inner, text="GRAND TOTAL", font=("Segoe UI", 15, "bold"), bg="#f3f4f6", fg="#111827").pack(side="left", padx=(30, 10))
        self.total_label = tk.Label(total_inner, text="₹ 0.00", font=("Segoe UI", 24, "bold"), bg="#f3f4f6", fg="#16a34a")
        self.total_label.pack(side="right")

        # BUTTONS
        btn_frame = tk.Frame(inner, bg=t["card"])
        btn_frame.pack(fill="x")
        self.generate_btn = tk.Button(btn_frame, text="🖨 Generate Bill", bg="#2563eb", fg="white", activebackground="#1d4ed8", activeforeground="white", relief="flat", cursor="hand2", font=("Segoe UI", 12, "bold"), padx=25, pady=12, command=self._generate_bill)
        self.generate_btn.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.new_btn = tk.Button(btn_frame, text="📝 New Bill", bg="#4b5563", fg="white", activebackground="#374151", activeforeground="white", relief="flat", cursor="hand2", font=("Segoe UI", 12, "bold"), padx=25, pady=12, command=self._new_bill)
        self.new_btn.pack(side="left", fill="x", expand=True, padx=(6, 0))

        # Keyboard shortcuts
        self.bind_all("<F5>", lambda e: self._generate_bill())
        self.bind_all("<Control-n>", lambda e: self._new_bill())
        self.bind_all("<Control-f>", lambda e: self.prod_search.focus_set())

    # =========================================================
    # AUTO REFRESH PRODUCTS
    # =========================================================
    def _auto_refresh_products(self):
        self._refresh_prod_list()
        self.after(30000, self._auto_refresh_products)

    # =========================================================
    # SEARCH PRODUCTS
    # =========================================================
    def _search_products(self, event=None):
        q = self.prod_search.get().strip()
        rows = search_products(q) if q else get_all_products()
        self._load_prod_tree(rows)

    # =========================================================
    # LOAD PRODUCT TABLE
    # =========================================================
    def _load_prod_tree(self, rows):
        self.prod_tree.delete(*self.prod_tree.get_children())
        for r in rows:
            tags = ()
            if r["quantity"] == 0:
                tags = ("out_of_stock",)
            elif r["quantity"] <= 5:
                tags = ("low_stock",)
            self.prod_tree.insert("", "end", values=(r["product_id"], r["product_name"], r["quantity"], f"₹ {r['price']:.2f}"), tags=tags)
        self.prod_tree.tag_configure("out_of_stock", foreground="red")
        self.prod_tree.tag_configure("low_stock", foreground="orange")

    # =========================================================
    # REFRESH PRODUCTS
    # =========================================================
    def _refresh_prod_list(self):
        rows = get_all_products()
        self._load_prod_tree(rows)

    # =========================================================
    # SELECT PRODUCT
    # =========================================================
    def _select_product(self, event=None):
        selected = self.prod_tree.selection()
        if not selected:
            return
        vals = self.prod_tree.item(selected[0], "values")
        pid = int(vals[0])
        prod = get_product_by_id(pid)
        if not prod:
            messagebox.showerror("Error", "Product not found in database")
            return
        self._selected_prod = prod
        self.prod_search.delete(0, tk.END)
        self.prod_search.insert(0, prod["product_name"])
        stock_status = ""
        if prod["quantity"] == 0:
            stock_status = " | ⚠️ OUT OF STOCK"
        elif prod["quantity"] <= 5:
            stock_status = " | ⚠️ LOW STOCK"
        self.sel_info.config(text=f"✅ Selected: {prod['product_name']} | Stock: {prod['quantity']}{stock_status} | Price: ₹ {prod['price']:.2f}", fg="#16a34a")
        self.qty_spinbox.focus_set()
        self.add_btn.config(bg="#15803d")

    # =========================================================
    # ADD TO CART
    # =========================================================
    def _add_to_cart(self):
        if not self._selected_prod:
            messagebox.showwarning("Warning", "⚠️ Please select a product first!\n\nDouble-click on a product from the list.")
            return
        qty = self.qty_var.get()
        if qty <= 0:
            messagebox.showwarning("Warning", "Quantity must be greater than 0")
            return
        if self._selected_prod["quantity"] == 0:
            messagebox.showwarning("Out of Stock", f"❌ {self._selected_prod['product_name']} is out of stock!")
            return
        already_added = sum(item["quantity"] for item in self._cart if item["product_id"] == self._selected_prod["product_id"])
        remaining_stock = self._selected_prod["quantity"] - already_added
        if qty > remaining_stock:
            messagebox.showwarning("Insufficient Stock", f"⚠️ Only {remaining_stock} unit(s) remaining for:\n\n{self._selected_prod['product_name']}\n\nCurrent stock: {self._selected_prod['quantity']}\nAlready in cart: {already_added}")
            return

        for item in self._cart:
            if item["product_id"] == self._selected_prod["product_id"]:
                item["quantity"] += qty
                item["subtotal"] = item["quantity"] * item["price"]
                self._refresh_cart()
                self.qty_var.set(1)
                self.add_btn.config(bg="#16a34a")
                self._flash_cart()
                return

        subtotal = qty * self._selected_prod["price"]
        self._cart.append({
            "product_id": self._selected_prod["product_id"],
            "product_name": self._selected_prod["product_name"],
            "quantity": qty,
            "price": self._selected_prod["price"],
            "subtotal": subtotal
        })
        self._refresh_cart()
        self.qty_var.set(1)
        self.add_btn.config(bg="#16a34a")
        self._flash_cart()

    def _flash_cart(self):
        original_bg = self.total_label.cget("bg")
        self.total_label.config(bg="#10b981")
        self.after(200, lambda: self.total_label.config(bg=original_bg))

    # =========================================================
    # REFRESH CART
    # =========================================================
    def _refresh_cart(self):
        self.cart_tree.delete(*self.cart_tree.get_children())
        total = 0
        total_items = 0
        for item in self._cart:
            total += item["subtotal"]
            total_items += item["quantity"]
            self.cart_tree.insert("", "end", values=(item["product_name"], item["quantity"], f"₹ {item['price']:.2f}", f"₹ {item['subtotal']:.2f}"))
        self.total_label.config(text=f"₹ {total:,.2f}")
        self.item_count_label.config(text=f"Items: {total_items}")
        self.generate_btn.config(state="normal" if self._cart else "disabled")

    def _show_cart_menu(self, event):
        item = self.cart_tree.identify_row(event.y)
        if item:
            self.cart_tree.selection_set(item)
            self.cart_menu.post(event.x_root, event.y_root)

    def _remove_cart_item(self, event=None):
        selected = self.cart_tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Please select an item to remove")
            return
        item_values = self.cart_tree.item(selected[0], "values")
        item_name = item_values[0]
        if not messagebox.askyesno("Confirm Remove", f"Remove '{item_name}' from cart?"):
            return
        idx = self.cart_tree.index(selected[0])
        self._cart.pop(idx)
        self._refresh_cart()

    def _edit_cart_quantity(self):
        selected = self.cart_tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Please select an item to edit")
            return
        idx = self.cart_tree.index(selected[0])
        item = self._cart[idx]
        dialog = tk.Toplevel(self)
        dialog.title("Edit Quantity")
        dialog.geometry("300x150")
        dialog.configure(bg=self.t["bg"])
        dialog.resizable(False, False)
        tk.Label(dialog, text=f"Product: {item['product_name']}", font=("Segoe UI", 11, "bold"), bg=self.t["bg"], fg=self.t["text"]).pack(pady=10)
        tk.Label(dialog, text="New Quantity:", bg=self.t["bg"], fg=self.t["text"]).pack()
        qty_var = tk.IntVar(value=item['quantity'])
        tk.Spinbox(dialog, from_=1, to=999, textvariable=qty_var, font=("Segoe UI", 11), width=10).pack(pady=5)
        def save():
            new_qty = qty_var.get()
            product = get_product_by_id(item['product_id'])
            if product and new_qty > product['quantity']:
                messagebox.showwarning("Insufficient Stock", f"Only {product['quantity']} units available in stock!")
                return
            item['quantity'] = new_qty
            item['subtotal'] = new_qty * item['price']
            self._refresh_cart()
            dialog.destroy()
        tk.Button(dialog, text="Save", bg="#2563eb", fg="white", command=save, font=("Segoe UI", 10, "bold"), padx=20, pady=5).pack(pady=10)

    def _clear_cart(self):
        if not self._cart:
            return
        if not messagebox.askyesno("Clear Cart", "Are you sure you want to clear all items from cart?"):
            return
        self._cart.clear()
        self._refresh_cart()
        self._refresh_prod_list()

    # =========================================================
    # GENERATE BILL
    # =========================================================
    def _generate_bill(self):
        customer = self.f_cust.get().strip()
        if not customer:
            messagebox.showwarning("Missing Information", "⚠️ Please enter customer name to generate bill.")
            self.f_cust.focus_set()
            return
        if not self._cart:
            messagebox.showwarning("Empty Cart", "⚠️ Cart is empty! Please add products first.")
            return

        # Final stock validation
        for item in self._cart:
            product = get_product_by_id(item['product_id'])
            if product and item['quantity'] > product['quantity']:
                messagebox.showerror("Stock Error", f"❌ Insufficient stock for {item['product_name']}!\nAvailable: {product['quantity']}, Requested: {item['quantity']}\n\nPlease update your cart and try again.")
                return

        items = [{"product_id": item["product_id"], "quantity": item["quantity"]} for item in self._cart]

        try:
            self.generate_btn.config(state="disabled", text="⏳ Processing...")
            self.update()

            bill_data = create_bill(
                customer_name=customer,
                phone=self.f_phone.get(),
                address=self.f_addr.get(),
                items=items
            )

            # UPDATE PRODUCT STOCKS DIRECTLY (FIXED)
            self._update_product_stocks()

            messagebox.showinfo("Success", f"✅ Bill Generated Successfully!\n\nBill Number: {bill_data.get('bill_number', 'N/A')}\nCustomer: {customer}\nTotal Items: {sum(item['quantity'] for item in self._cart)}\nGrand Total: ₹ {bill_data.get('grand_total', 0):,.2f}")
            self._show_bill_popup(bill_data)

            self._bill_counter += 1
            self._new_bill()
            self._refresh_prod_list()

            if self.on_bill_created:
                self.on_bill_created()

        except Exception as e:
            messagebox.showerror("Bill Generation Failed", f"❌ Error generating bill:\n\n{str(e)}\n\nPlease try again or contact support.")
        finally:
            self.generate_btn.config(state="normal", text="🖨 Generate Bill")

    # =========================================================
    # UPDATE PRODUCT STOCKS (FIXED – NO root_ref.pages NEEDED)
    # =========================================================
    def _update_product_stocks(self):
        """
        Directly deduct stock from the database using product_ops.
        Does NOT require any reference to the ProductsPage UI.
        """
        try:
            for item in self._cart:
                product_id = item["product_id"]
                qty_sold = item["quantity"]

                # Fetch current product info
                results = search_products(str(product_id))
                if not results:
                    print(f"⚠️ Product ID {product_id} not found in DB")
                    continue

                prod = results[0]
                current_qty = int(prod["quantity"])
                new_qty = current_qty - qty_sold

                if new_qty < 0:
                    print(f"❌ Negative stock prevented for {prod['product_name']}")
                    continue

                # Update directly via product_ops
                update_product(
                    product_id,
                    prod["product_name"],
                    prod["category"],
                    new_qty,
                    float(prod["price"])
                )
                print(f"✅ Stock updated: {prod['product_name']} ({current_qty} -> {new_qty})")

        except Exception as e:
            print(f"❌ Stock update error: {e}")
            # Not raising exception to avoid breaking bill generation

    # =========================================================
    # SHOW BILL POPUP (unchanged)
    # =========================================================
    def _show_bill_popup(self, bill_data):
        popup = tk.Toplevel(self)
        popup.title(f"Bill Preview - {bill_data.get('bill_number', 'N/A')}")
        popup.geometry("550x700")
        popup.configure(bg=self.t["bg"])
        popup.transient(self)
        popup.grab_set()

        tk.Label(popup, text="📚 BINOD BOOK BINDING", bg=self.t["bg"], fg=self.t["text"], font=("Segoe UI", 22, "bold")).pack(pady=12)
        tk.Label(popup, text="Professional Book Binding Services", bg=self.t["bg"], fg=self.t["text2"], font=("Segoe UI", 10)).pack()
        tk.Frame(popup, bg=self.t["border"], height=2).pack(fill="x", padx=20, pady=10)

        details_frame = tk.Frame(popup, bg=self.t["bg"])
        details_frame.pack(fill="x", padx=30, pady=5)
        tk.Label(details_frame, text=f"Bill No: {bill_data.get('bill_number', 'N/A')}", bg=self.t["bg"], fg=self.t["text"], font=("Segoe UI", 11, "bold")).pack(anchor="w")
        tk.Label(details_frame, text=f"Date: {bill_data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}", bg=self.t["bg"], fg=self.t["text2"], font=("Segoe UI", 10)).pack(anchor="w")
        tk.Label(details_frame, text=f"Customer: {bill_data.get('customer_name', 'N/A')}", bg=self.t["bg"], fg=self.t["text"], font=("Segoe UI", 11)).pack(anchor="w")
        if bill_data.get('phone'):
            tk.Label(details_frame, text=f"Phone: {bill_data.get('phone', '')}", bg=self.t["bg"], fg=self.t["text2"], font=("Segoe UI", 10)).pack(anchor="w")
        if bill_data.get('address'):
            tk.Label(details_frame, text=f"Address: {bill_data.get('address', '')}", bg=self.t["bg"], fg=self.t["text2"], font=("Segoe UI", 10)).pack(anchor="w")

        tk.Frame(popup, bg=self.t["border"], height=1).pack(fill="x", padx=20, pady=10)

        text = tk.Text(popup, font=("Consolas", 11), bg="white", fg="black", wrap=tk.WORD)
        text.pack(fill="both", expand=True, padx=25, pady=10)

        bill_text = "ITEMS:\n" + "="*50 + "\n\n"
        for i, item in enumerate(bill_data.get("items", []), 1):
            bill_text += f"{i}. {item['product_name']}\n   {item['quantity']} x ₹ {item.get('price', 0):,.2f} = ₹ {item['subtotal']:,.2f}\n\n"
        bill_text += "="*50 + f"\nGRAND TOTAL: ₹ {bill_data.get('grand_total', 0):,.2f}\n" + "="*50 + "\n\nThank you for your business! 🙏\nVisit again!"
        text.insert("1.0", bill_text)
        text.config(state="disabled")

        button_frame = tk.Frame(popup, bg=self.t["bg"])
        button_frame.pack(pady=15)

        def export_pdf():
            try:
                path = generate_pdf_bill(bill_data)
                if path:
                    open_file(path)
                    messagebox.showinfo("Success", f"PDF exported successfully!\n\nLocation: {path}")
                else:
                    messagebox.showerror("Error", "Failed to generate PDF")
            except Exception as e:
                messagebox.showerror("PDF Error", f"Failed to export PDF:\n{str(e)}")

        tk.Button(button_frame, text="📄 Export PDF", bg="#2563eb", fg="white", activebackground="#1d4ed8", font=("Segoe UI", 11, "bold"), relief="flat", padx=20, pady=10, cursor="hand2", command=export_pdf).pack(side="left", padx=5)
        tk.Button(button_frame, text="🖨 Print", bg="#059669", fg="white", activebackground="#047857", font=("Segoe UI", 11, "bold"), relief="flat", padx=20, pady=10, cursor="hand2", command=lambda: messagebox.showinfo("Print", "Print functionality coming soon!")).pack(side="left", padx=5)
        tk.Button(button_frame, text="✖ Close", bg="#6b7280", fg="white", activebackground="#4b5563", font=("Segoe UI", 11, "bold"), relief="flat", padx=20, pady=10, cursor="hand2", command=popup.destroy).pack(side="left", padx=5)

    # =========================================================
    # NEW BILL
    # =========================================================
    def _new_bill(self):
        self._cart.clear()
        self._refresh_cart()
        self.f_cust.delete(0, tk.END)
        self.f_phone.delete(0, tk.END)
        self.f_addr.delete(0, tk.END)
        self.prod_search.delete(0, tk.END)
        self.sel_info.config(text="Double-click product to select", fg=self.t["text2"])
        self._selected_prod = None
        self.add_btn.config(bg="#16a34a")
        self._refresh_prod_list()
        self.f_cust.focus_set()

    # =========================================================
    # REFRESH (Called externally)
    # =========================================================
    def refresh(self):
        self._refresh_prod_list()
        if self._cart:
            self._refresh_cart()