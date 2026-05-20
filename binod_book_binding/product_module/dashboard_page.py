
# """
# Professional Dynamic Dashboard — Focused Metrics Edition
# Binod Book Binding
# """

# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime

# from assets.theme import get as T

# from product_module.product_ops import (
#     get_total_products,
#     get_total_stock_value,
#     get_low_stock_products,
# )

# from customer_module.customer_ops import (
#     get_daily_sales,
# )

# # ── SAFE FALLBACK IMPORT FOR BILL COUNTING ────────────────────────────
# try:
#     from customer_module.customer_ops import get_today_bill_count
# except ImportError:
#     def get_today_bill_count():
#         return 0


# class DashboardPage(tk.Frame):

#     def __init__(self, master, **kwargs):
#         self.t = T()
#         super().__init__(
#             master,
#             bg=self.t["bg"],
#             **kwargs
#         )
#         self.build_ui()

#     # =========================================================
#     # UI COMPOSITION
#     # =========================================================
#     def build_ui(self):
#         t = self.t

#         # ================= HEADER =================
#         header = tk.Frame(self, bg=t["bg"])
#         header.pack(fill="x", padx=25, pady=(20, 10))

#         tk.Label(
#             header,
#             text="📊 Dashboard",
#             bg=t["bg"],
#             fg=t["text"],
#             font=("Segoe UI", 28, "bold")
#         ).pack(side="left")

#         tk.Label(
#             header,
#             text=datetime.now().strftime("%d %B %Y"),
#             bg=t["bg"],
#             fg=t["text2"],
#             font=("Segoe UI", 12)
#         ).pack(side="right")

#         # =========================================================
#         # RECONFIGURED TOP CARDS ROW (3 Columns - Perfectly Proportioned)
#         # =========================================================
#         self.cards_frame = tk.Frame(
#             self,
#             bg=t["bg"]
#         )
#         self.cards_frame.pack(
#             fill="x",
#             padx=20,
#             pady=10
#         )

#         # Card Variables
#         self.total_products_var = tk.StringVar()
#         self.today_sales_var = tk.StringVar()     
#         self.stock_value_var = tk.StringVar()

#         # Card 1: Total Products
#         self.create_card(
#             self.cards_frame,
#             "📦",
#             "Total Products",
#             self.total_products_var,
#             "#2563eb",
#             0
#         )

#         # Card 2: Today's Sales Activity
#         self.create_card(
#             self.cards_frame,
#             "📈",
#             "Today's Sales",
#             self.today_sales_var,
#             "#ef4444",
#             1
#         )

#         # Card 3: Total Stock Value (Moved to top row for maximum visibility)
#         self.create_card(
#             self.cards_frame,
#             "🏪",
#             "Total Stock Value",
#             self.stock_value_var,
#             "#10b981",
#             2
#         )

#         # =========================================================
#         # STOCK CHECK TABLE SECTION
#         # =========================================================
#         stock_container = tk.Frame(
#             self,
#             bg=t["card"],
#             highlightbackground=t["border"],
#             highlightthickness=1
#         )
#         stock_container.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=(15, 20)
#         )

#         top = tk.Frame(stock_container, bg=t["card"])
#         top.pack(fill="x", padx=20, pady=15)

#         tk.Label(
#             top,
#             text="📦 Available Stock",
#             bg=t["card"],
#             fg=t["text"],
#             font=("Segoe UI", 18, "bold")
#         ).pack(side="left")

#         # TABLE COLUMNS
#         columns = (
#             "ID",
#             "Product",
#             "Category",
#             "Stock",
#             "Price"
#         )

#         style = ttk.Style()
#         style.theme_use("default")
#         style.configure(
#             "Treeview",
#             background="#1e293b",
#             foreground="white",
#             fieldbackground="#1e293b",
#             rowheight=38,
#             borderwidth=0,
#             font=("Segoe UI", 10)
#         )
#         style.configure(
#             "Treeview.Heading",
#             background="#2563eb",
#             foreground="white",
#             font=("Segoe UI", 10, "bold")
#         )

#         self.tree = ttk.Treeview(
#             stock_container,
#             columns=columns,
#             show="headings",
#             height=12
#         )

#         for col in columns:
#             self.tree.heading(col, text=col)
#             self.tree.column(
#                 col,
#                 anchor="center",
#                 width=150
#             )

#         self.tree.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=(0, 20)
#         )

#         # LOAD DATA
#         self.refresh()

#     # =========================================================
#     # CARD CREATION FACTORY
#     # =========================================================
#     def create_card(
#         self,
#         parent,
#         icon,
#         title,
#         variable,
#         color,
#         column
#     ):
#         t = self.t

#         card = tk.Frame(
#             parent,
#             bg=t["card"],
#             highlightbackground=t["border"],
#             highlightthickness=1,
#             bd=0
#         )
#         card.grid(
#             row=0,
#             column=column,
#             padx=10,
#             pady=10,
#             sticky="nsew"
#         )

#         parent.grid_columnconfigure(column, weight=1)

#         tk.Label(
#             card,
#             text=icon,
#             bg=t["card"],
#             fg=color,
#             font=("Segoe UI Emoji", 28)
#         ).pack(anchor="w", padx=20, pady=(20, 5))

#         tk.Label(
#             card,
#             text=title,
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 11)
#         ).pack(anchor="w", padx=20)

#         tk.Label(
#             card,
#             textvariable=variable,
#             bg=t["card"],
#             fg=t["text"] if column != 2 else "#10b981",  # Gives the stock value card a vivid green accent color
#             font=("Segoe UI", 22, "bold")  
#         ).pack(anchor="w", padx=20, pady=(5, 20))

#     # =========================================================
#     # LOAD STOCK TABLE
#     # =========================================================
#     def load_stock_table(self):
#         self.tree.delete(*self.tree.get_children())
#         rows = get_low_stock_products(999999)

#         for row in rows:
#             tag = ""
#             if row["quantity"] <= 5:
#                 tag = "low"

#             self.tree.insert(
#                 "",
#                 "end",
#                 values=(
#                     row["product_id"],
#                     row["product_name"],
#                     row["category"],
#                     row["quantity"],
#                     f"₹ {row['price']}"
#                 ),
#                 tags=(tag,)
#             )

#         self.tree.tag_configure(
#             "low",
#             foreground="#ef4444"
#         )

#     # =========================================================
#     # REFRESH LIVE DATA
#     # =========================================================
#     def refresh(self):
#         today_bills = get_today_bill_count()

#         # UI String format calculations
#         today_sales_string = f"₹ {get_daily_sales():,.0f} ({today_bills} Bills)"
#         stock_value_string = f"₹ {get_total_stock_value():,.2f}"

#         # ASSIGN RECONFIGURED DATA FIELDS
#         self.total_products_var.set(str(get_total_products()))
#         self.today_sales_var.set(today_sales_string)
#         self.stock_value_var.set(stock_value_string)

#         self.load_stock_table()















"""
Professional Dynamic Dashboard — Focused Metrics Edition
Binod Book Binding
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime

from assets.theme import get as T

from product_module.product_ops import (
    get_total_products,
    get_total_stock_value,
    get_low_stock_products,
)

from customer_module.customer_ops import (
    get_daily_sales,
)


class DashboardPage(tk.Frame):

    def __init__(self, master, **kwargs):
        self.t = T()
        super().__init__(
            master,
            bg=self.t["bg"],
            **kwargs
        )
        self.build_ui()

    # =========================================================
    # UI COMPOSITION
    # =========================================================
    def build_ui(self):
        t = self.t

        # ================= HEADER =================
        header = tk.Frame(self, bg=t["bg"])
        header.pack(fill="x", padx=25, pady=(20, 10))

        tk.Label(
            header,
            text="📊 Dashboard",
            bg=t["bg"],
            fg=t["text"],
            font=("Segoe UI", 28, "bold")
        ).pack(side="left")

        tk.Label(
            header,
            text=datetime.now().strftime("%d %B %Y"),
            bg=t["bg"],
            fg=t["text2"],
            font=("Segoe UI", 12)
        ).pack(side="right")

        # =========================================================
        # RECONFIGURED TOP CARDS ROW (3 Columns - Perfectly Proportioned)
        # =========================================================
        self.cards_frame = tk.Frame(
            self,
            bg=t["bg"]
        )
        self.cards_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Card Variables
        self.total_products_var = tk.StringVar()
        self.today_sales_var = tk.StringVar()     
        self.stock_value_var = tk.StringVar()

        # Card 1: Total Products
        self.create_card(
            self.cards_frame,
            "📦",
            "Total Products",
            self.total_products_var,
            "#2563eb",
            0
        )

        # Card 2: Today's Sales Activity (Now purely displaying revenue)
        self.create_card(
            self.cards_frame,
            "📈",
            "Today's Sales",
            self.today_sales_var,
            "#ef4444",
            1
        )

        # Card 3: Total Stock Value
        self.create_card(
            self.cards_frame,
            "🏪",
            "Total Stock Value",
            self.stock_value_var,
            "#10b981",
            2
        )

        # =========================================================
        # STOCK CHECK TABLE SECTION
        # =========================================================
        stock_container = tk.Frame(
            self,
            bg=t["card"],
            highlightbackground=t["border"],
            highlightthickness=1
        )
        stock_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(15, 20)
        )

        top = tk.Frame(stock_container, bg=t["card"])
        top.pack(fill="x", padx=20, pady=15)

        tk.Label(
            top,
            text="📦 Available Stock",
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 18, "bold")
        ).pack(side="left")

        # TABLE COLUMNS
        columns = (
            "ID",
            "Product",
            "Category",
            "Stock",
            "Price"
        )

        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#1e293b",
            foreground="white",
            fieldbackground="#1e293b",
            rowheight=38,
            borderwidth=0,
            font=("Segoe UI", 10)
        )
        style.configure(
            "Treeview.Heading",
            background="#2563eb",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

        self.tree = ttk.Treeview(
            stock_container,
            columns=columns,
            show="headings",
            height=12
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
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        # LOAD DATA
        self.refresh()

    # =========================================================
    # CARD CREATION FACTORY
    # =========================================================
    def create_card(
        self,
        parent,
        icon,
        title,
        variable,
        color,
        column
    ):
        t = self.t

        card = tk.Frame(
            parent,
            bg=t["card"],
            highlightbackground=t["border"],
            highlightthickness=1,
            bd=0
        )
        card.grid(
            row=0,
            column=column,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        parent.grid_columnconfigure(column, weight=1)

        tk.Label(
            card,
            text=icon,
            bg=t["card"],
            fg=color,
            font=("Segoe UI Emoji", 28)
        ).pack(anchor="w", padx=20, pady=(20, 5))

        tk.Label(
            card,
            text=title,
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 11)
        ).pack(anchor="w", padx=20)

        tk.Label(
            card,
            textvariable=variable,
            bg=t["card"],
            fg=t["text"] if column != 2 else "#10b981",  
            font=("Segoe UI", 22, "bold")  
        ).pack(anchor="w", padx=20, pady=(5, 20))

    # =========================================================
    # LOAD STOCK TABLE
    # =========================================================
    def load_stock_table(self):
        self.tree.delete(*self.tree.get_children())
        rows = get_low_stock_products(999999)

        for row in rows:
            tag = ""
            if row["quantity"] <= 5:
                tag = "low"

            self.tree.insert(
                "",
                "end",
                values=(
                    row["product_id"],
                    row["product_name"],
                    row["category"],
                    row["quantity"],
                    f"₹ {row['price']}"
                ),
                tags=(tag,)
            )

        self.tree.tag_configure(
            "low",
            foreground="#ef4444"
        )

    # =========================================================
    # REFRESH LIVE DATA
    # =========================================================
    def refresh(self):
        # UI String format calculations without bill elements
        today_sales_string = f"₹ {get_daily_sales():,.0f}"
        stock_value_string = f"₹ {get_total_stock_value():,.2f}"

        # ASSIGN RECONFIGURED DATA FIELDS
        self.total_products_var.set(str(get_total_products()))
        self.today_sales_var.set(today_sales_string)
        self.stock_value_var.set(stock_value_string)

        self.load_stock_table()