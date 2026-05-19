"""
customer_module/customers_page.py
View customer history and search.
"""

import tkinter as tk
from assets.theme import get as T, FONTS
from assets.widgets import (
    FlatButton, make_treeview, populate_tree, section_header
)
from customer_module.customer_ops import (
    get_all_bills, search_bills, get_customer_history, get_bill_items
)


class CustomersPage(tk.Frame):
    def __init__(self, master, root_ref=None, **kwargs):
        t = T()
        super().__init__(master, bg=t["bg"], **kwargs)
        self.root_ref = root_ref
        self._build()

    def _build(self):
        t = T()
        section_header(self, "👤 Customer History", "Search and view customer purchases")

        # Search
        top = tk.Frame(self, bg=t["bg"])
        top.pack(fill="x", padx=24, pady=(0, 8))

        tk.Label(top, text="🔍", bg=t["bg"], fg=t["text2"],
                 font=FONTS["body"]).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *a: self._search())
        tk.Entry(top, textvariable=self.search_var,
                 bg=t["entry_bg"], fg=t["entry_fg"],
                 insertbackground=t["entry_fg"],
                 relief="flat", bd=0, font=FONTS["body"],
                 highlightthickness=1,
                 highlightbackground=t["border"],
                 highlightcolor=t["accent"],
                 width=32).pack(side="left", padx=8, ipady=5)
        tk.Label(top, text="(Search by name, phone, or bill no)",
                 bg=t["bg"], fg=t["text2"], font=FONTS["small"]).pack(side="left")

        FlatButton(top, text="Refresh", icon="🔄",
                   command=self.refresh).pack(side="right")

        # Bills table
        section_header(self, "📋 All Purchases")
        cols = [
            ("bill_number",   "Bill No",    130),
            ("customer_name", "Customer",   150),
            ("phone_number",  "Phone",      110),
            ("address",       "Address",    150),
            ("grand_total",   "Amount (₹)", 105),
            ("bill_date",     "Date",       150),
        ]
        tree_frame = tk.Frame(self, bg=t["bg"])
        tree_frame.pack(fill="both", expand=True, padx=24)
        self.tree = make_treeview(tree_frame, cols, height=14)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        # Items detail
        section_header(self, "📦 Purchase Items")
        item_frame = tk.Frame(self, bg=t["bg"])
        item_frame.pack(fill="x", padx=24, pady=(0, 12))
        item_cols = [
            ("product_name",  "Product",    200),
            ("quantity",      "Qty",         60),
            ("price_per_item","Unit (₹)",    90),
            ("total_bill",    "Subtotal (₹)",100),
        ]
        self.item_tree = make_treeview(item_frame, item_cols, height=6)

        self.refresh()

    def _search(self):
        q = self.search_var.get().strip()
        rows = search_bills(q) if q else get_all_bills()
        self._load(rows)

    def refresh(self):
        self._load(get_all_bills())

    def _load(self, rows):
        for r in rows:
            r["grand_total"] = f"₹ {r['grand_total']:,.2f}"
        populate_tree(self.tree, rows,
                      ["bill_number", "customer_name", "phone_number",
                       "address", "grand_total", "bill_date"])
        self.item_tree.delete(*self.item_tree.get_children())

    def _on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        bn = self.tree.item(sel[0], "values")[0]
        items = get_bill_items(bn)
        self.item_tree.delete(*self.item_tree.get_children())
        for i, item in enumerate(items):
            tag = "alt" if i % 2 == 1 else ""
            self.item_tree.insert("", "end", values=(
                item["product_name"], item["quantity"],
                f"₹ {item['price_per_item']:.2f}",
                f"₹ {item['total_bill']:.2f}",
            ), tags=(tag,))
        self.item_tree.tag_configure("alt", background=T()["tree_alt"])
