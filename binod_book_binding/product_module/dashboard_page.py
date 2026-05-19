# # # """
# # # Dashboard page — shows key stats and recent bills.
# # # """

# # # import tkinter as tk
# # # from assets.theme import get as T, FONTS
# # # from assets.widgets import StatCard, make_treeview, populate_tree, section_header
# # # from product_module.product_ops import (
# # #     get_total_products, get_total_stock_value, get_low_stock_products
# # # )
# # # from customer_module.customer_ops import (
# # #     get_total_sales, get_total_customers, get_daily_sales, get_recent_bills
# # # )


# # # class DashboardPage(tk.Frame):
# # #     def __init__(self, master, **kwargs):
# # #         t = T()
# # #         super().__init__(master, bg=t["bg"], **kwargs)
# # #         self._build()

# # #     def _build(self):
# # #         t = T()

# # #         # ── Top stat cards ─────────────────────────────────────────────────────
# # #         section_header(self, "📊 Dashboard", "Live overview")

# # #         cards_frame = tk.Frame(self, bg=t["bg"])
# # #         cards_frame.pack(fill="x", padx=24, pady=8)
# # #         cards_frame.grid_columnconfigure((0,1,2,3), weight=1, uniform="card")

# # #         stats = [
# # #             ("📦", "Total Products", get_total_products(), t["accent"]),
# # #             ("👤", "Total Customers", get_total_customers(), t["accent3"]),
# # #             ("💰", "Total Sales", f"₹{get_total_sales():,.2f}", t["accent2"]),
# # #             ("📅", "Today's Sales", f"₹{get_daily_sales():,.2f}", "#9c27b0"),
# # #         ]
# # #         self._stat_cards = []
# # #         for col, (icon, label, val, color) in enumerate(stats):
# # #             card = StatCard(cards_frame, icon=icon, label=label,
# # #                             value=val, color=color)
# # #             card.grid(row=0, column=col, padx=8, pady=4, sticky="nsew")
# # #             self._stat_cards.append(card)

# # #         # ── Stock value card ───────────────────────────────────────────────────
# # #         sv_frame = tk.Frame(self, bg=t["bg"])
# # #         sv_frame.pack(fill="x", padx=24, pady=4)
# # #         stock_card = StatCard(sv_frame, icon="🏪", label="Total Stock Value",
# # #                               value=f"₹{get_total_stock_value():,.2f}",
# # #                               color=t["accent"])
# # #         stock_card.pack(side="left", padx=(0, 8), ipadx=20)

# # #         # ── Recent Bills table ─────────────────────────────────────────────────
# # #         section_header(self, "🧾 Recent Bills")

# # #         cols = [
# # #             ("bill_number",   "Bill No",       140),
# # #             ("customer_name", "Customer",      160),
# # #             ("phone_number",  "Phone",         120),
# # #             ("grand_total",   "Amount (₹)",    110),
# # #             ("bill_date",     "Date",          160),
# # #         ]
# # #         tree_frame = tk.Frame(self, bg=t["bg"])
# # #         tree_frame.pack(fill="both", expand=True, padx=24, pady=(0, 12))
# # #         self.tree = make_treeview(tree_frame, cols, height=10)
# # #         self._refresh_bills()

# # #         # ── Low Stock Alerts ───────────────────────────────────────────────────
# # #         low = get_low_stock_products(threshold=5)
# # #         if low:
# # #             section_header(self, "⚠️  Low Stock Alert")
# # #             alert_frame = tk.Frame(self, bg=t["card"], padx=16, pady=10)
# # #             alert_frame.pack(fill="x", padx=24, pady=(0, 12))
# # #             for p in low[:6]:
# # #                 color = t["danger"] if p["quantity"] == 0 else t["warn"]
# # #                 status = "OUT OF STOCK" if p["quantity"] == 0 else f"Only {p['quantity']} left"
# # #                 row = tk.Frame(alert_frame, bg=t["card"])
# # #                 row.pack(fill="x", pady=2)
# # #                 tk.Label(row, text=f"• {p['product_name']}",
# # #                          bg=t["card"], fg=t["text"], font=FONTS["body"],
# # #                          width=28, anchor="w").pack(side="left")
# # #                 tk.Label(row, text=status, bg=t["card"], fg=color,
# # #                          font=FONTS["small"]).pack(side="left")

# # #     def _refresh_bills(self):
# # #         rows = get_recent_bills(10)
# # #         # Format total
# # #         for r in rows:
# # #             r["grand_total"] = f"₹ {r['grand_total']:,.2f}"
# # #         populate_tree(self.tree, rows,
# # #                       ["bill_number", "customer_name", "phone_number",
# # #                        "grand_total", "bill_date"])

# # #     def refresh(self):
# # #         """Called when switching back to this page."""
# # #         self._refresh_bills()












# # """
# # Ultra Professional Dynamic Dashboard
# # Binod Book Binding
# # """

# # import tkinter as tk
# # from tkinter import ttk
# # from datetime import datetime

# # from assets.theme import get as T, FONTS
# # from assets.widgets import (
# #     StatCard,
# #     make_treeview,
# #     populate_tree,
# #     section_header
# # )

# # from product_module.product_ops import (
# #     get_total_products,
# #     get_total_stock_value,
# #     get_low_stock_products,
# # )

# # from customer_module.customer_ops import (
# #     get_total_sales,
# #     get_total_customers,
# #     get_daily_sales,
# #     get_recent_bills
# # )


# # class DashboardPage(tk.Frame):

# #     def __init__(self, master, **kwargs):

# #         self.t = T()

# #         super().__init__(
# #             master,
# #             bg=self.t["bg"],
# #             **kwargs
# #         )

# #         self.build_ui()

# #     # ================= UI =================
# #     def build_ui(self):

# #         t = self.t

# #         # ================= HEADER =================
# #         header = tk.Frame(
# #             self,
# #             bg=t["bg"]
# #         )

# #         header.pack(fill="x", padx=25, pady=(20, 10))

# #         tk.Label(
# #             header,
# #             text="📊 Dashboard",
# #             bg=t["bg"],
# #             fg=t["text"],
# #             font=("Segoe UI", 28, "bold")
# #         ).pack(side="left")

# #         current_date = datetime.now().strftime("%d %B %Y")

# #         tk.Label(
# #             header,
# #             text=current_date,
# #             bg=t["bg"],
# #             fg=t["text2"],
# #             font=("Segoe UI", 12)
# #         ).pack(side="right")

# #         # ================= CARDS =================
# #         cards_frame = tk.Frame(
# #             self,
# #             bg=t["bg"]
# #         )

# #         cards_frame.pack(fill="x", padx=20)

# #         cards = [
# #             (
# #                 "📦",
# #                 "Total Products",
# #                 get_total_products(),
# #                 "#2563eb"
# #             ),

# #             (
# #                 "👥",
# #                 "Customers",
# #                 get_total_customers(),
# #                 "#059669"
# #             ),

# #             (
# #                 "💰",
# #                 "Total Sales",
# #                 f"₹ {get_total_sales():,.0f}",
# #                 "#d97706"
# #             ),

# #             (
# #                 "📈",
# #                 "Today's Sales",
# #                 f"₹ {get_daily_sales():,.0f}",
# #                 "#dc2626"
# #             ),
# #         ]

# #         for i, (icon, title, value, color) in enumerate(cards):

# #             card = tk.Frame(
# #                 cards_frame,
# #                 bg=t["card"],
# #                 highlightthickness=1,
# #                 highlightbackground=t["border"],
# #                 bd=0
# #             )

# #             card.grid(
# #                 row=0,
# #                 column=i,
# #                 padx=10,
# #                 pady=10,
# #                 sticky="nsew"
# #             )

# #             cards_frame.grid_columnconfigure(i, weight=1)

# #             tk.Label(
# #                 card,
# #                 text=icon,
# #                 bg=t["card"],
# #                 fg=color,
# #                 font=("Segoe UI Emoji", 30)
# #             ).pack(anchor="w", padx=20, pady=(20, 5))

# #             tk.Label(
# #                 card,
# #                 text=title,
# #                 bg=t["card"],
# #                 fg=t["text2"],
# #                 font=("Segoe UI", 12)
# #             ).pack(anchor="w", padx=20)

# #             tk.Label(
# #                 card,
# #                 text=value,
# #                 bg=t["card"],
# #                 fg=t["text"],
# #                 font=("Segoe UI", 24, "bold")
# #             ).pack(anchor="w", padx=20, pady=(5, 20))

# #         # ================= STOCK VALUE =================
# #         stock_frame = tk.Frame(
# #             self,
# #             bg=t["bg"]
# #         )

# #         stock_frame.pack(fill="x", padx=20)

# #         stock_card = tk.Frame(
# #             stock_frame,
# #             bg="#111827",
# #             padx=20,
# #             pady=15
# #         )

# #         stock_card.pack(fill="x", pady=10)

# #         tk.Label(
# #             stock_card,
# #             text="🏪 Total Stock Value",
# #             bg="#111827",
# #             fg="#d1d5db",
# #             font=("Segoe UI", 14, "bold")
# #         ).pack(anchor="w")

# #         tk.Label(
# #             stock_card,
# #             text=f"₹ {get_total_stock_value():,.2f}",
# #             bg="#111827",
# #             fg="#10b981",
# #             font=("Segoe UI", 30, "bold")
# #         ).pack(anchor="w", pady=(5, 0))

# #         # ================= RECENT BILLS =================
# #         bills_container = tk.Frame(
# #             self,
# #             bg=t["card"]
# #         )

# #         bills_container.pack(
# #             fill="both",
# #             expand=True,
# #             padx=20,
# #             pady=15
# #         )

# #         tk.Label(
# #             bills_container,
# #             text="🧾 Recent Bills",
# #             bg=t["card"],
# #             fg=t["text"],
# #             font=("Segoe UI", 18, "bold")
# #         ).pack(anchor="w", padx=20, pady=15)

# #         style = ttk.Style()

# #         style.theme_use("default")

# #         style.configure(
# #             "Treeview",
# #             background="#1e293b",
# #             foreground="white",
# #             fieldbackground="#1e293b",
# #             rowheight=38,
# #             borderwidth=0,
# #             font=("Segoe UI", 10)
# #         )

# #         style.configure(
# #             "Treeview.Heading",
# #             background="#2563eb",
# #             foreground="white",
# #             font=("Segoe UI", 10, "bold")
# #         )

# #         columns = (
# #             "Bill No",
# #             "Customer",
# #             "Phone",
# #             "Amount",
# #             "Date"
# #         )

# #         self.tree = ttk.Treeview(
# #             bills_container,
# #             columns=columns,
# #             show="headings",
# #             height=10
# #         )

# #         for col in columns:

# #             self.tree.heading(col, text=col)

# #             self.tree.column(
# #                 col,
# #                 anchor="center",
# #                 width=150
# #             )

# #         self.tree.pack(
# #             fill="both",
# #             expand=True,
# #             padx=20,
# #             pady=(0, 20)
# #         )

# #         self.load_recent_bills()

# #         # ================= LOW STOCK =================
# #         low_products = get_low_stock_products(5)

# #         if low_products:

# #             low_frame = tk.Frame(
# #                 self,
# #                 bg="#2b0b0b",
# #                 padx=20,
# #                 pady=15
# #             )

# #             low_frame.pack(
# #                 fill="x",
# #                 padx=20,
# #                 pady=(0, 20)
# #             )

# #             tk.Label(
# #                 low_frame,
# #                 text="⚠ Low Stock Alerts",
# #                 bg="#2b0b0b",
# #                 fg="#ef4444",
# #                 font=("Segoe UI", 16, "bold")
# #             ).pack(anchor="w")

# #             for p in low_products[:5]:

# #                 msg = f"{p['product_name']} — Only {p['quantity']} left"

# #                 tk.Label(
# #                     low_frame,
# #                     text=msg,
# #                     bg="#2b0b0b",
# #                     fg="white",
# #                     font=("Segoe UI", 11)
# #                 ).pack(anchor="w", pady=3)

# #     # ================= LOAD BILLS =================
# #     def load_recent_bills(self):

# #         self.tree.delete(*self.tree.get_children())

# #         bills = get_recent_bills(10)

# #         for bill in bills:

# #             self.tree.insert(
# #                 "",
# #                 "end",
# #                 values=(
# #                     bill["bill_number"],
# #                     bill["customer_name"],
# #                     bill["phone_number"],
# #                     f"₹ {bill['grand_total']}",
# #                     bill["bill_date"]
# #                 )
# #             )

# #     # ================= REFRESH =================
# #     def refresh(self):

# #         self.load_recent_bills()
















# """
# Ultra Professional Dynamic Dashboard
# Binod Book Binding
# Integrated Live Stock Management Dashboard
# """

# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime

# from assets.theme import get as T

# from product_module.product_ops import (
#     get_total_products,
#     get_total_stock_value,
#     get_low_stock_products,
#     get_all_products
# )

# from customer_module.customer_ops import (
#     get_total_sales,
#     get_total_customers,
#     get_daily_sales
# )


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
#     # UI
#     # =========================================================
#     def build_ui(self):

#         t = self.t

#         # =====================================================
#         # HEADER
#         # =====================================================

#         header = tk.Frame(
#             self,
#             bg=t["bg"]
#         )

#         header.pack(fill="x", padx=25, pady=(20, 10))

#         tk.Label(
#             header,
#             text="📊 Dashboard",
#             bg=t["bg"],
#             fg=t["text"],
#             font=("Segoe UI", 30, "bold")
#         ).pack(side="left")

#         date_text = datetime.now().strftime("%d %B %Y")

#         tk.Label(
#             header,
#             text=date_text,
#             bg=t["bg"],
#             fg=t["text2"],
#             font=("Segoe UI", 12)
#         ).pack(side="right")

#         # =====================================================
#         # STAT CARDS
#         # =====================================================

#         cards_frame = tk.Frame(
#             self,
#             bg=t["bg"]
#         )

#         cards_frame.pack(fill="x", padx=20)

#         cards = [

#             (
#                 "📦",
#                 "Total Products",
#                 get_total_products(),
#                 "#3b82f6"
#             ),

#             (
#                 "👥",
#                 "Customers",
#                 get_total_customers(),
#                 "#10b981"
#             ),

#             (
#                 "💰",
#                 "Total Sales",
#                 f"₹ {get_total_sales():,.0f}",
#                 "#f59e0b"
#             ),

#             (
#                 "📈",
#                 "Today's Sales",
#                 f"₹ {get_daily_sales():,.0f}",
#                 "#ef4444"
#             )
#         ]

#         for i, (icon, title, value, color) in enumerate(cards):

#             card = tk.Frame(
#                 cards_frame,
#                 bg=t["card"],
#                 highlightbackground=t["border"],
#                 highlightthickness=1,
#                 bd=0,
#                 cursor="hand2"
#             )

#             card.grid(
#                 row=0,
#                 column=i,
#                 padx=10,
#                 pady=10,
#                 sticky="nsew"
#             )

#             cards_frame.grid_columnconfigure(i, weight=1)

#             # Hover Effect
#             card.bind(
#                 "<Enter>",
#                 lambda e, c=card: c.config(bg="#1e293b")
#             )

#             card.bind(
#                 "<Leave>",
#                 lambda e, c=card: c.config(bg=t["card"])
#             )

#             tk.Label(
#                 card,
#                 text=icon,
#                 bg=card["bg"],
#                 fg=color,
#                 font=("Segoe UI Emoji", 30)
#             ).pack(anchor="w", padx=20, pady=(18, 5))

#             tk.Label(
#                 card,
#                 text=title,
#                 bg=card["bg"],
#                 fg=t["text2"],
#                 font=("Segoe UI", 12)
#             ).pack(anchor="w", padx=20)

#             tk.Label(
#                 card,
#                 text=value,
#                 bg=card["bg"],
#                 fg=t["text"],
#                 font=("Segoe UI", 24, "bold")
#             ).pack(anchor="w", padx=20, pady=(5, 20))

#         # =====================================================
#         # STOCK VALUE SECTION
#         # =====================================================

#         stock_value_frame = tk.Frame(
#             self,
#             bg=t["bg"]
#         )

#         stock_value_frame.pack(fill="x", padx=20)

#         stock_card = tk.Frame(
#             stock_value_frame,
#             bg="#111827",
#             padx=25,
#             pady=18
#         )

#         stock_card.pack(fill="x", pady=10)

#         tk.Label(
#             stock_card,
#             text="🏪 Total Stock Value",
#             bg="#111827",
#             fg="#d1d5db",
#             font=("Segoe UI", 15, "bold")
#         ).pack(anchor="w")

#         tk.Label(
#             stock_card,
#             text=f"₹ {get_total_stock_value():,.2f}",
#             bg="#111827",
#             fg="#10b981",
#             font=("Segoe UI", 32, "bold")
#         ).pack(anchor="w", pady=(6, 0))

#         # =====================================================
#         # LIVE STOCK SECTION
#         # =====================================================

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
#             pady=(10, 15)
#         )

#         top_bar = tk.Frame(
#             stock_container,
#             bg=t["card"]
#         )

#         top_bar.pack(fill="x", padx=20, pady=15)

#         tk.Label(
#             top_bar,
#             text="📦 Available Stock",
#             bg=t["card"],
#             fg=t["text"],
#             font=("Segoe UI", 20, "bold")
#         ).pack(side="left")

#         tk.Label(
#             top_bar,
#             text="Live Inventory Status",
#             bg=t["card"],
#             fg=t["text2"],
#             font=("Segoe UI", 11)
#         ).pack(side="right")

#         # =====================================================
#         # TABLE DESIGN
#         # =====================================================

#         style = ttk.Style()

#         style.theme_use("default")

#         style.configure(
#             "Treeview",
#             background="#111827",
#             foreground="white",
#             fieldbackground="#111827",
#             rowheight=38,
#             borderwidth=0,
#             relief="flat",
#             font=("Segoe UI", 10)
#         )

#         style.map(
#             "Treeview",
#             background=[("selected", "#2563eb")]
#         )

#         style.configure(
#             "Treeview.Heading",
#             background="#2563eb",
#             foreground="white",
#             relief="flat",
#             font=("Segoe UI", 10, "bold")
#         )

#         columns = (
#             "ID",
#             "Product",
#             "Category",
#             "Available Stock",
#             "Price",
#             "Status"
#         )

#         self.stock_tree = ttk.Treeview(
#             stock_container,
#             columns=columns,
#             show="headings",
#             height=14
#         )

#         for col in columns:

#             self.stock_tree.heading(col, text=col)

#             self.stock_tree.column(
#                 col,
#                 anchor="center",
#                 width=150
#             )

#         self.stock_tree.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=(0, 20)
#         )

#         # =====================================================
#         # LOAD PRODUCTS
#         # =====================================================

#         self.load_stock()

#         # =====================================================
#         # LOW STOCK ALERTS
#         # =====================================================

#         low_products = get_low_stock_products(5)

#         if low_products:

#             low_frame = tk.Frame(
#                 self,
#                 bg="#2b0b0b",
#                 padx=20,
#                 pady=15
#             )

#             low_frame.pack(
#                 fill="x",
#                 padx=20,
#                 pady=(0, 20)
#             )

#             tk.Label(
#                 low_frame,
#                 text="⚠ Low Stock Alerts",
#                 bg="#2b0b0b",
#                 fg="#ef4444",
#                 font=("Segoe UI", 16, "bold")
#             ).pack(anchor="w")

#             for p in low_products[:5]:

#                 if p["quantity"] == 0:
#                     msg = f"{p['product_name']} → OUT OF STOCK"
#                 else:
#                     msg = f"{p['product_name']} → Only {p['quantity']} left"

#                 tk.Label(
#                     low_frame,
#                     text=msg,
#                     bg="#2b0b0b",
#                     fg="white",
#                     font=("Segoe UI", 11)
#                 ).pack(anchor="w", pady=3)

#     # =========================================================
#     # LOAD STOCK
#     # =========================================================

#     def load_stock(self):

#         self.stock_tree.delete(*self.stock_tree.get_children())

#         rows = get_all_products()

#         for row in rows:

#             qty = row["quantity"]

#             if qty == 0:

#                 status = "OUT OF STOCK"
#                 tag = "out"

#             elif qty <= 5:

#                 status = "LOW STOCK"
#                 tag = "low"

#             else:

#                 status = "IN STOCK"
#                 tag = "ok"

#             self.stock_tree.insert(
#                 "",
#                 "end",
#                 values=(
#                     row["product_id"],
#                     row["product_name"],
#                     row["category"],
#                     row["quantity"],
#                     f"₹ {row['price']}",
#                     status
#                 ),
#                 tags=(tag,)
#             )

#         self.stock_tree.tag_configure(
#             "out",
#             foreground="#ef4444"
#         )

#         self.stock_tree.tag_configure(
#             "low",
#             foreground="#f59e0b"
#         )

#         self.stock_tree.tag_configure(
#             "ok",
#             foreground="#10b981"
#         )

#     # =========================================================
#     # REFRESH
#     # =========================================================

#     def refresh(self):

#         self.load_stock()









"""
Professional Dynamic Dashboard
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
    get_total_sales,
    get_total_customers,
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
    # UI
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
        # TOP CARDS
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
        self.total_customers_var = tk.StringVar()
        self.total_sales_var = tk.StringVar()
        self.today_sales_var = tk.StringVar()
        self.stock_value_var = tk.StringVar()

        self.create_card(
            self.cards_frame,
            "📦",
            "Total Products",
            self.total_products_var,
            "#2563eb",
            0
        )

        self.create_card(
            self.cards_frame,
            "👥",
            "Customers",
            self.total_customers_var,
            "#10b981",
            1
        )

        self.create_card(
            self.cards_frame,
            "💰",
            "Total Sales",
            self.total_sales_var,
            "#f59e0b",
            2
        )

        self.create_card(
            self.cards_frame,
            "📈",
            "Today's Sales",
            self.today_sales_var,
            "#ef4444",
            3
        )

        # =========================================================
        # STOCK VALUE SECTION
        # =========================================================
        stock_frame = tk.Frame(
            self,
            bg=t["card"],
            highlightbackground=t["border"],
            highlightthickness=1,
            padx=25,
            pady=20
        )

        stock_frame.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        tk.Label(
            stock_frame,
            text="🏪 Total Stock Value",
            bg=t["card"],
            fg=t["text2"],
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w")

        self.stock_value_label = tk.Label(
            stock_frame,
            textvariable=self.stock_value_var,
            bg=t["card"],
            fg="#10b981",
            font=("Segoe UI", 30, "bold")
        )

        self.stock_value_label.pack(anchor="w", pady=(10, 0))

        # =========================================================
        # STOCK CHECK SECTION
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
            pady=(0, 20)
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

        # TABLE
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
    # CARD
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
            font=("Segoe UI", 12)
        ).pack(anchor="w", padx=20)

        tk.Label(
            card,
            textvariable=variable,
            bg=t["card"],
            fg=t["text"],
            font=("Segoe UI", 24, "bold")
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

        # DATABASE LIVE VALUES
        self.total_products_var.set(
            str(get_total_products())
        )

        self.total_customers_var.set(
            str(get_total_customers())
        )

        self.total_sales_var.set(
            f"₹ {get_total_sales():,.0f}"
        )

        self.today_sales_var.set(
            f"₹ {get_daily_sales():,.0f}"
        )

        self.stock_value_var.set(
            f"₹ {get_total_stock_value():,.2f}"
        )

        self.load_stock_table()