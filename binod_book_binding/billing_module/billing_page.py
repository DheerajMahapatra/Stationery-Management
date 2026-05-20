
# billing_module/billing_page.py
# PROFESSIONAL POS BILLING UI - FINAL CLEAN VERSION

import tkinter as tk
from tkinter import messagebox, ttk

from assets.theme import get as T, FONTS

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
        self._selected_prod = None

        self._build()

    # =========================================================
    # BUILD UI
    # =========================================================
    def _build(self):

        t = self.t

        main = tk.Frame(self, bg=t["bg"])
        main.pack(fill="both", expand=True, padx=18, pady=15)

        # HEADER
        header = tk.Frame(main, bg=t["bg"])
        header.pack(fill="x", pady=(0, 15))

        tk.Label(
            header,
            text="🧾 Billing / Point Of Sale",
            font=("Segoe UI", 26, "bold"),
            bg=t["bg"],
            fg=t["text"]
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Professional Billing Management System",
            font=("Segoe UI", 11),
            bg=t["bg"],
            fg=t["text2"]
        ).pack(anchor="w")

        # BODY
        body = tk.Frame(main, bg=t["bg"])
        body.pack(fill="both", expand=True)

        body.grid_columnconfigure(0, weight=4)
        body.grid_columnconfigure(1, weight=3)
        body.grid_rowconfigure(0, weight=1)

        # LEFT PANEL
        left = tk.Frame(
            body,
            bg=t["card"],
            bd=0,
            highlightthickness=1,
            highlightbackground=t["border"]
        )

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 12)
        )

        # RIGHT PANEL
        right = tk.Frame(
            body,
            bg=t["card"],
            bd=0,
            highlightthickness=1,
            highlightbackground=t["border"]
        )

        right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self._build_left(left)
        self._build_right(right)

    # =========================================================
    # LEFT PANEL
    # =========================================================
    def _build_left(self, panel):

        t = self.t

        inner = tk.Frame(panel, bg=t["card"])
        inner.pack(fill="both", expand=True, padx=18, pady=18)

        # =====================================================
        # CUSTOMER SECTION
        # =====================================================

        tk.Label(
            inner,
            text="👤 Customer Information",
            font=("Segoe UI", 18, "bold"),
            bg=t["card"],
            fg=t["accent"]
        ).pack(anchor="w", pady=(0, 14))

        customer_grid = tk.Frame(inner, bg=t["card"])
        customer_grid.pack(fill="x")

        customer_grid.grid_columnconfigure(0, weight=1)
        customer_grid.grid_columnconfigure(1, weight=1)

        # CUSTOMER NAME
        tk.Label(
            customer_grid,
            text="Customer Name *",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 4))

        self.f_cust = tk.Entry(
            customer_grid,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat",
            insertbackground=t["text"]
        )

        self.f_cust.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(0, 8),
            ipady=8
        )

        # PHONE
        tk.Label(
            customer_grid,
            text="Phone Number",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=1, sticky="w", pady=(0, 4))

        self.f_phone = tk.Entry(
            customer_grid,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat",
            insertbackground=t["text"]
        )

        self.f_phone.grid(
            row=1,
            column=1,
            sticky="ew",
            ipady=8
        )

        # ADDRESS
        tk.Label(
            customer_grid,
            text="Address",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=(12, 4)
        )

        self.f_addr = tk.Entry(
            customer_grid,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat",
            insertbackground=t["text"]
        )

        self.f_addr.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            ipady=8
        )

        # SEPARATOR
        tk.Frame(
            inner,
            bg=t["border"],
            height=1
        ).pack(fill="x", pady=20)

        # =====================================================
        # PRODUCT SECTION
        # =====================================================

        tk.Label(
            inner,
            text="📦 Add Product",
            font=("Segoe UI", 18, "bold"),
            bg=t["card"],
            fg=t["accent"]
        ).pack(anchor="w", pady=(0, 12))

        action_row = tk.Frame(inner, bg=t["card"])
        action_row.pack(fill="x", pady=(0, 12))

        # SEARCH
        search_frame = tk.Frame(action_row, bg=t["card"])
        search_frame.pack(side="left", fill="x", expand=True)

        tk.Label(
            search_frame,
            text="Search Product",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 4))

        self.prod_search = tk.Entry(
            search_frame,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat",
            insertbackground=t["text"]
        )

        self.prod_search.pack(
            fill="x",
            ipady=8,
            padx=(0, 10)
        )

        self.prod_search.bind("<KeyRelease>", self._search_products)

        # QUANTITY
        qty_frame = tk.Frame(action_row, bg=t["card"])
        qty_frame.pack(side="left", padx=(0, 10))

        tk.Label(
            qty_frame,
            text="Qty",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 4))

        self.qty_var = tk.IntVar(value=1)

        self.qty_spinbox = tk.Spinbox(
            qty_frame,
            from_=1,
            to=999,
            width=6,
            textvariable=self.qty_var,
            font=("Segoe UI", 12),
            bg=t["entry_bg"],
            fg=t["entry_fg"],
            relief="flat",
            justify="center"
        )

        self.qty_spinbox.pack(ipady=6)

        # ADD BUTTON
        add_btn_frame = tk.Frame(action_row, bg=t["card"])
        add_btn_frame.pack(side="left")

        tk.Label(
            add_btn_frame,
            text="",
            bg=t["card"]
        ).pack(pady=(0, 4))

        self.add_btn = tk.Button(
            add_btn_frame,
            text="➕ Add",
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 11, "bold"),
            padx=18,
            pady=9,
            command=self._add_to_cart
        )

        self.add_btn.pack()

        # PRODUCT INFO
        self.sel_info = tk.Label(
            inner,
            text="Double-click product to select",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 10)
        )

        self.sel_info.pack(anchor="w", pady=(8, 10))

        # =====================================================
        # PRODUCT TABLE
        # =====================================================

        table_frame = tk.Frame(inner, bg=t["card"])
        table_frame.pack(fill="both", expand=True)

        columns = (
            "id",
            "product",
            "stock",
            "price"
        )

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Custom.Treeview",
            background="#ffffff",
            foreground="#111827",
            rowheight=32,
            fieldbackground="#ffffff",
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Custom.Treeview.Heading",
            background="#374151",
            foreground="white",
            relief="flat",
            font=("Segoe UI", 10, "bold")
        )

        style.map(
            "Custom.Treeview",
            background=[("selected", "#2563eb")],
            foreground=[("selected", "white")]
        )

        self.prod_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12,
            style="Custom.Treeview"
        )

        self.prod_tree.heading("id", text="ID")
        self.prod_tree.heading("product", text="Product Name")
        self.prod_tree.heading("stock", text="Stock")
        self.prod_tree.heading("price", text="Price")

        self.prod_tree.column("id", width=60, anchor="center")
        self.prod_tree.column("product", width=280)
        self.prod_tree.column("stock", width=90, anchor="center")
        self.prod_tree.column("price", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.prod_tree.yview
        )

        self.prod_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.prod_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.prod_tree.bind(
            "<Double-1>",
            self._select_product
        )

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

        tk.Label(
            top,
            text="🛒 Shopping Cart",
            font=("Segoe UI", 18, "bold"),
            bg=t["card"],
            fg=t["accent"]
        ).pack(side="left")

        tk.Button(
            top,
            text="Clear Cart",
            bg="#dc2626",
            fg="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            padx=14,
            pady=6,
            command=self._clear_cart
        ).pack(side="right")

        # CART TABLE
        cart_frame = tk.Frame(inner, bg=t["card"])
        cart_frame.pack(fill="both", expand=True)

        cart_columns = (
            "product",
            "qty",
            "price",
            "total"
        )

        self.cart_tree = ttk.Treeview(
            cart_frame,
            columns=cart_columns,
            show="headings",
            height=12,
            style="Custom.Treeview"
        )

        self.cart_tree.heading("product", text="Product")
        self.cart_tree.heading("qty", text="Qty")
        self.cart_tree.heading("price", text="Price")
        self.cart_tree.heading("total", text="Total")

        self.cart_tree.column("product", width=230)
        self.cart_tree.column("qty", width=60, anchor="center")
        self.cart_tree.column("price", width=100, anchor="center")
        self.cart_tree.column("total", width=120, anchor="center")

        cart_scroll = ttk.Scrollbar(
            cart_frame,
            orient="vertical",
            command=self.cart_tree.yview
        )

        self.cart_tree.configure(
            yscrollcommand=cart_scroll.set
        )

        self.cart_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        cart_scroll.pack(
            side="right",
            fill="y"
        )

        self.cart_tree.bind(
            "<Delete>",
            self._remove_cart_item
        )

        # TOTAL CARD
        total_card = tk.Frame(
            inner,
            bg="#f3f4f6",
            bd=0
        )

        total_card.pack(
            fill="x",
            pady=15
        )

        total_inner = tk.Frame(
            total_card,
            bg="#f3f4f6"
        )

        total_inner.pack(
            fill="x",
            padx=20,
            pady=18
        )

        tk.Label(
            total_inner,
            text="GRAND TOTAL",
            font=("Segoe UI", 15, "bold"),
            bg="#f3f4f6",
            fg="#111827"
        ).pack(side="left")

        self.total_label = tk.Label(
            total_inner,
            text="₹ 0.00",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f4f6",
            fg="#16a34a"
        )

        self.total_label.pack(side="right")

        # BUTTONS
        btn_frame = tk.Frame(inner, bg=t["card"])
        btn_frame.pack(fill="x")

        self.generate_btn = tk.Button(
            btn_frame,
            text="🖨 Generate Bill",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 12, "bold"),
            padx=25,
            pady=12,
            command=self._generate_bill
        )

        self.generate_btn.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 6)
        )

        self.new_btn = tk.Button(
            btn_frame,
            text="📝 New Bill",
            bg="#4b5563",
            fg="white",
            activebackground="#374151",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 12, "bold"),
            padx=25,
            pady=12,
            command=self._new_bill
        )

        self.new_btn.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(6, 0)
        )

    # =========================================================
    # SEARCH PRODUCTS
    # =========================================================
    def _search_products(self, event=None):

        q = self.prod_search.get().strip()

        if q:
            rows = search_products(q)
        else:
            rows = get_all_products()

        self._load_prod_tree(rows)

    # =========================================================
    # LOAD PRODUCT TABLE
    # =========================================================
    def _load_prod_tree(self, rows):

        self.prod_tree.delete(*self.prod_tree.get_children())

        for r in rows:

            self.prod_tree.insert(
                "",
                "end",
                values=(
                    r["product_id"],
                    r["product_name"],
                    r["quantity"],
                    f"₹ {r['price']:.2f}"
                )
            )

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
            return

        self._selected_prod = prod

        # AUTO SHOW IN SEARCH BAR
        self.prod_search.delete(0, tk.END)
        self.prod_search.insert(0, prod["product_name"])

        self.sel_info.config(
            text=f"Selected: {prod['product_name']} | Stock: {prod['quantity']} | Price: ₹ {prod['price']}",
            fg="#16a34a"
        )

        self.qty_spinbox.focus_set()

    # =========================================================
    # ADD TO CART
    # =========================================================
    def _add_to_cart(self):

        if not self._selected_prod:

            messagebox.showwarning(
                "Warning",
                "Select Product First"
            )

            return

        qty = self.qty_var.get()

        if qty <= 0:
            return

        # FIXED STOCK BUG
        already_added = 0

        for item in self._cart:

            if item["product_id"] == self._selected_prod["product_id"]:
                already_added += item["quantity"]

        remaining_stock = self._selected_prod["quantity"] - already_added

        if qty > remaining_stock:

            messagebox.showwarning(
                "Stock Error",
                f"Only {remaining_stock} item(s) remaining"
            )

            return

        # UPDATE EXISTING
        for item in self._cart:

            if item["product_id"] == self._selected_prod["product_id"]:

                item["quantity"] += qty
                item["subtotal"] = (
                    item["quantity"] * item["price"]
                )

                self._refresh_cart()

                self.qty_var.set(1)

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

        customer = self.f_cust.get().strip()

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
    # SHOW BILL
    # =========================================================
    def _show_bill_popup(self, bill_data):

        popup = tk.Toplevel(self)

        popup.title("Bill Preview")
        popup.geometry("500x600")

        popup.configure(bg=self.t["bg"])

        tk.Label(
            popup,
            text="📚 BINOD BOOK BINDING",
            bg=self.t["bg"],
            fg=self.t["text"],
            font=("Segoe UI", 22, "bold")
        ).pack(pady=12)

        text = tk.Text(
            popup,
            font=("Consolas", 11),
            bg="white",
            fg="black"
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
            relief="flat",
            padx=20,
            pady=8,
            command=export_pdf
        ).pack(pady=10)

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

        self.sel_info.config(
            text="Double-click product to select",
            fg=self.t["text2"]
        )

        self._selected_prod = None

    # =========================================================
    # REFRESH
    # =========================================================
    def refresh(self):

        self._refresh_prod_list()