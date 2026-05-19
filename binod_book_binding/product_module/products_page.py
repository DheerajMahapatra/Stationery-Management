
"""
Professional Product Management
Binod Book Binding
"""

import tkinter as tk
from tkinter import ttk, messagebox

from assets.theme import get as T
from product_module.product_ops import *


class ProductsPage(tk.Frame):

    def __init__(self, master, root_ref=None):

        self.root_ref = root_ref

        self.t = T()

        super().__init__(
            master,
            bg=self.t["bg"]
        )

        self.selected_id = None

        self.build_ui()

    # =========================================================
    # UI
    # =========================================================
    def build_ui(self):

        t = self.t

        # ================= HEADER =================
        header = tk.Frame(self, bg=t["bg"])

        header.pack(
            fill="x",
            padx=20,
            pady=15
        )

        tk.Label(
            header,
            text="📦 Product Management",
            bg=t["bg"],
            fg=t["text"],
            font=("Segoe UI", 26, "bold")
        ).pack(side="left")

        # =========================================================
        # FORM
        # =========================================================
        form = tk.Frame(
            self,
            bg=t["card"],
            padx=20,
            pady=20
        )

        form.pack(
            fill="x",
            padx=20
        )

        # ================= NAME =================
        tk.Label(
            form,
            text="Product Name",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=0, sticky="w")

        self.name_entry = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=25,
            relief="flat"
        )

        self.name_entry.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            ipady=6
        )

        # ================= CATEGORY =================
        tk.Label(
            form,
            text="Category",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=1, sticky="w")

        self.cat_entry = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=20,
            relief="flat"
        )

        self.cat_entry.grid(
            row=1,
            column=1,
            padx=5,
            ipady=6
        )

        # ================= QUANTITY =================
        tk.Label(
            form,
            text="Quantity",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=2, sticky="w")

        self.qty_entry = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=10,
            relief="flat"
        )

        self.qty_entry.grid(
            row=1,
            column=2,
            padx=5,
            ipady=6
        )

        # ================= PRICE =================
        tk.Label(
            form,
            text="Price",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=3, sticky="w")

        self.price_entry = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=10,
            relief="flat"
        )

        self.price_entry.grid(
            row=1,
            column=3,
            padx=5,
            ipady=6
        )

        # =========================================================
        # BUTTONS
        # =========================================================
        btn_frame = tk.Frame(
            form,
            bg=t["card"]
        )

        btn_frame.grid(
            row=1,
            column=4,
            columnspan=4,
            padx=10
        )

        # ADD BUTTON
        tk.Button(
            btn_frame,
            text="➕ Add",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            relief="flat",
            padx=14,
            pady=8,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            command=self.add_product_ui
        ).pack(side="left", padx=5)

        # UPDATE BUTTON
        tk.Button(
            btn_frame,
            text="✏ Update",
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            relief="flat",
            padx=14,
            pady=8,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            command=self.update_product_ui
        ).pack(side="left", padx=5)

        # DELETE BUTTON
        tk.Button(
            btn_frame,
            text="🗑 Delete",
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            relief="flat",
            padx=14,
            pady=8,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            command=self.delete_product_ui
        ).pack(side="left", padx=5)

        # CLEAR BUTTON
        tk.Button(
            btn_frame,
            text="🔄 Clear",
            bg="#6b7280",
            fg="white",
            relief="flat",
            padx=14,
            pady=8,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            command=self.clear_form
        ).pack(side="left", padx=5)

        # =========================================================
        # SEARCH
        # =========================================================
        search_frame = tk.Frame(
            self,
            bg=t["bg"]
        )

        search_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        tk.Label(
            search_frame,
            text="🔍 Search Product:",
            bg=t["bg"],
            fg=t["text"],
            font=("Segoe UI", 11, "bold")
        ).pack(side="left")

        self.search_var = tk.StringVar()

        self.search_var.trace_add(
            "write",
            lambda *args: self.search_ui()
        )

        tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Segoe UI", 11),
            width=35,
            relief="flat"
        ).pack(side="left", padx=10, ipady=5)

        # =========================================================
        # TABLE
        # =========================================================
        table_frame = tk.Frame(
            self,
            bg=t["card"]
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "ID",
            "Product",
            "Category",
            "Stock",
            "Price",
            "Date"
        )

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#1e293b",
            foreground="white",
            fieldbackground="#1e293b",
            rowheight=35,
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#2563eb",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#2563eb")]
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                anchor="center",
                width=150
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_product
        )

        self.load_products()

    # =========================================================
    # LOAD PRODUCTS
    # =========================================================
    def load_products(self):

        self.tree.delete(*self.tree.get_children())

        rows = get_all_products()

        for row in rows:

            tag = ""

            if row["quantity"] == 0:
                tag = "out"

            elif row["quantity"] <= 5:
                tag = "low"

            self.tree.insert(
                "",
                "end",
                values=(
                    row["product_id"],
                    row["product_name"],
                    row["category"],
                    row["quantity"],
                    f"₹ {row['price']}",
                    row["date_added"]
                ),
                tags=(tag,)
            )

        self.tree.tag_configure(
            "low",
            foreground="#f59e0b"
        )

        self.tree.tag_configure(
            "out",
            foreground="#ef4444"
        )

    # =========================================================
    # ADD PRODUCT
    # =========================================================
    def add_product_ui(self):

        try:

            name = self.name_entry.get()
            category = self.cat_entry.get()
            quantity = int(self.qty_entry.get())
            price = float(self.price_entry.get())

            if not name or not category:

                messagebox.showwarning(
                    "Warning",
                    "Please fill all fields."
                )

                return

            add_product(
                name,
                category,
                quantity,
                price
            )

            self.load_products()

            self.clear_form()

            messagebox.showinfo(
                "Success",
                "Product Added Successfully"
            )

            self.refresh_dashboard()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # UPDATE PRODUCT
    # =========================================================
    def update_product_ui(self):

        if not self.selected_id:

            messagebox.showwarning(
                "Warning",
                "Please select a product first."
            )

            return

        try:

            update_product(
                self.selected_id,
                self.name_entry.get(),
                self.cat_entry.get(),
                int(self.qty_entry.get()),
                float(self.price_entry.get())
            )

            self.load_products()

            self.clear_form()

            messagebox.showinfo(
                "Success",
                "Product Updated Successfully"
            )

            self.refresh_dashboard()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # DELETE PRODUCT
    # =========================================================
    def delete_product_ui(self):

        if not self.selected_id:

            messagebox.showwarning(
                "Warning",
                "Please select a product first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this product?"
        )

        if not confirm:
            return

        try:

            result = delete_product(self.selected_id)

            if isinstance(result, dict):

                if result.get("success"):

                    messagebox.showinfo(
                        "Success",
                        "Product Deleted Successfully"
                    )

                else:

                    messagebox.showerror(
                        "Delete Failed",
                        result.get(
                            "message",
                            "Unable to delete product."
                        )
                    )

                    return

            else:

                messagebox.showinfo(
                    "Success",
                    "Product Deleted Successfully"
                )

            self.load_products()

            self.clear_form()

            self.refresh_dashboard()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================================
    # SEARCH
    # =========================================================
    def search_ui(self):

        q = self.search_var.get()

        rows = search_products(q)

        self.tree.delete(*self.tree.get_children())

        for row in rows:

            self.tree.insert(
                "",
                "end",
                values=(
                    row["product_id"],
                    row["product_name"],
                    row["category"],
                    row["quantity"],
                    f"₹ {row['price']}",
                    row["date_added"]
                )
            )

    # =========================================================
    # SELECT PRODUCT
    # =========================================================
    def select_product(self, event):

        selected = self.tree.selection()

        if not selected:
            return

        vals = self.tree.item(selected[0], "values")

        self.selected_id = vals[0]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, vals[1])

        self.cat_entry.delete(0, tk.END)
        self.cat_entry.insert(0, vals[2])

        self.qty_entry.delete(0, tk.END)
        self.qty_entry.insert(0, vals[3])

        price = str(vals[4]).replace("₹", "").strip()

        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, price)

    # =========================================================
    # CLEAR FORM
    # =========================================================
    def clear_form(self):

        self.name_entry.delete(0, tk.END)
        self.cat_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

        self.selected_id = None

    # =========================================================
    # REFRESH DASHBOARD
    # =========================================================
    def refresh_dashboard(self):

        try:

            if self.root_ref:

                dashboard = self.root_ref.pages.get("dashboard")

                if dashboard:
                    dashboard.refresh()

        except:
            pass