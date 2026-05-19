"""
billing_module/bills_history_page.py
View all bills, search, reprint.
"""

import tkinter as tk
from tkinter import messagebox
from assets.theme import get as T, FONTS
from assets.widgets import (
    FlatButton, make_treeview, populate_tree, section_header, Toast
)
from customer_module.customer_ops import (
    get_all_bills, search_bills, get_bill_items
)
from billing_module.bill_printer import generate_pdf_bill, open_file


class BillsHistoryPage(tk.Frame):
    def __init__(self, master, root_ref=None, **kwargs):
        t = T()
        super().__init__(master, bg=t["bg"], **kwargs)
        self.root_ref = root_ref
        self._build()

    def _build(self):
        t = T()
        section_header(self, "📋 Bills History", "All past transactions")

        # Search + actions
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

        FlatButton(top, text="Refresh", icon="🔄",
                   command=self.refresh).pack(side="left", padx=4)
        FlatButton(top, text="View Bill", icon="👁️",
                   command=self._view_bill).pack(side="left", padx=4)
        FlatButton(top, text="Export PDF", icon="📄",
                   command=self._export_pdf).pack(side="left", padx=4)

        # Bills table
        cols = [
            ("bill_number",   "Bill No",    140),
            ("customer_name", "Customer",   160),
            ("phone_number",  "Phone",      120),
            ("address",       "Address",    160),
            ("grand_total",   "Amount (₹)", 110),
            ("bill_date",     "Date",       155),
        ]
        tree_frame = tk.Frame(self, bg=t["bg"])
        tree_frame.pack(fill="both", expand=True, padx=24)
        self.tree = make_treeview(tree_frame, cols, height=16)
        self.tree.bind("<Double-1>", lambda e: self._view_bill())

        # Bill items panel
        section_header(self, "📦 Bill Items (selected bill)")
        item_cols = [
            ("product_name", "Product",   200),
            ("quantity",     "Qty",        60),
            ("price_per_item","Unit (₹)",  90),
            ("total_bill",   "Subtotal (₹)",100),
        ]
        item_frame = tk.Frame(self, bg=t["bg"])
        item_frame.pack(fill="x", padx=24, pady=(0, 12))
        self.item_tree = make_treeview(item_frame, item_cols, height=6)

        self.refresh()

    def _search(self):
        q = self.search_var.get().strip()
        rows = search_bills(q) if q else get_all_bills()
        self._load(rows)

    def refresh(self):
        rows = get_all_bills()
        self._load(rows)

    def _load(self, rows):
        for r in rows:
            r["grand_total"] = f"₹ {r['grand_total']:,.2f}"
        populate_tree(self.tree, rows,
                      ["bill_number", "customer_name", "phone_number",
                       "address", "grand_total", "bill_date"])
        self.item_tree.delete(*self.item_tree.get_children())

    def _get_selected_bill(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Select Bill", "Please select a bill first.")
            return None
        return self.tree.item(sel[0], "values")[0]  # bill_number

    def _view_bill(self):
        bn = self._get_selected_bill()
        if not bn:
            return
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

    def _export_pdf(self):
        bn = self._get_selected_bill()
        if not bn:
            return
        sel = self.tree.selection()
        vals = self.tree.item(sel[0], "values")
        items_raw = get_bill_items(bn)
        items = [{
            "product_name": it["product_name"],
            "quantity":     it["quantity"],
            "price":        it["price_per_item"],
            "subtotal":     it["total_bill"],
        } for it in items_raw]

        grand_total = sum(it["subtotal"] for it in items)
        bill_data = {
            "bill_number":   bn,
            "customer_name": vals[1],
            "phone":         vals[2],
            "address":       vals[3],
            "items":         items,
            "grand_total":   grand_total,
            "bill_date":     vals[5],
        }
        path = generate_pdf_bill(bill_data)
        open_file(path)
        Toast(self.root_ref or self, f"PDF saved!", "success")
