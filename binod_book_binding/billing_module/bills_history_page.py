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
        
        # UI Placeholder state tracks
        self.placeholder_text = "Search by client or bill number..."
        self._build()

    def _build(self):
        t = T()
        section_header(self, "📋 Bills History", "All past transactions")

        # =====================================================
        # TOP ACTIONS BAR
        # =====================================================
        top = tk.Frame(self, bg=t["bg"])
        top.pack(fill="x", padx=24, pady=(0, 12))

        # Search wrapper group
        search_frame = tk.Frame(top, bg=t["bg"])
        search_frame.pack(side="left", fill="y")

        tk.Label(search_frame, text="🔍", bg=t["bg"], fg=t["text2"],
                 font=FONTS["body"]).pack(side="left")
        
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *a: self._search())
        
        self.search_entry = tk.Entry(
            search_frame, textvariable=self.search_var,
            bg=t["entry_bg"], fg=t["text2"], # Initialized using muted placeholder color profile
            insertbackground=t["entry_fg"],
            relief="flat", bd=0, font=FONTS["body"],
            highlightthickness=1,
            highlightbackground=t["border"],
            highlightcolor=t["accent"],
            width=36
        )
        self.search_entry.pack(side="left", padx=8, ipady=5)
        
        # Setup modern entry field visual interactive placeholders
        self.search_entry.insert(0, self.placeholder_text)
        self.search_entry.bind("<FocusIn>", self._clear_placeholder)
        self.search_entry.bind("<FocusOut>", self._add_placeholder)

        # Action Buttons Layout Group (Removed reduntant View Bill action)
        FlatButton(top, text="Refresh Logs", icon="🔄",
                   command=self.refresh).pack(side="right", padx=4)
        FlatButton(top, text="Export PDF / Print", icon="📄",
                   command=self._export_pdf).pack(side="right", padx=4)

        # =====================================================
        # MASTER: BILLS SUMMARY VIEW
        # =====================================================
        cols = [
            ("bill_number",   "Bill No",    140),
            ("customer_name", "Customer",   180),
            ("phone_number",  "Phone",      120),
            ("address",       "Address",    180),
            ("grand_total",   "Amount",     110),
            ("bill_date",     "Date",       155),
        ]
        
        tree_frame = tk.Frame(self, bg=t["bg"])
        tree_frame.pack(fill="both", expand=True, padx=24, pady=(0, 12))
        
        self.tree = make_treeview(tree_frame, cols, height=12)
        
        # UI Event Triggers: Connect live sync selections & double click overrides
        self.tree.bind("<<TreeviewSelect>>", lambda e: self._view_bill_details())
        self.tree.bind("<Double-1>", lambda e: self._export_pdf())

        # =====================================================
        # DETAIL: ITEMIZED PANEL VIEW
        # =====================================================
        section_header(self, "📦 Bill Items", "Breakdown of the selected statement logs")
        
        item_cols = [
            ("product_name", "Product / Description", 240),
            ("quantity",     "Qty",                    70),
            ("price_per_item","Unit Price",            110),
            ("total_bill",   "Subtotal",               120),
        ]
        
        item_frame = tk.Frame(self, bg=t["bg"])
        item_frame.pack(fill="x", padx=24, pady=(0, 16))
        self.item_tree = make_treeview(item_frame, item_cols, height=6)

        self.refresh()

    # Placeholder focus events definitions
    def _clear_placeholder(self, event):
        t = T()
        if self.search_var.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=t["entry_fg"])

    def _add_placeholder(self, event):
        t = T()
        if not self.search_var.get().strip():
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg=t["text2"])

    def _search(self):
        q = self.search_var.get().strip()
        # Prevent query collisions with default helper placeholder text strings
        if q == self.placeholder_text:
            return
            
        rows = search_bills(q) if q else get_all_bills()
        self._load(rows)

    def refresh(self):
        # Temporarily detach validation listeners during updates to prevent recursive filter loops
        current_query = self.search_var.get()
        if current_query and current_query != self.placeholder_text:
            rows = search_bills(current_query)
        else:
            rows = get_all_bills()
        self._load(rows)

    def _load(self, rows):
        for r in rows:
            # Check explicitly if formatting is already present to prevent duplicating symbols
            if isinstance(r["grand_total"], (int, float)):
                r["grand_total"] = f"₹ {r['grand_total']:,.2f}"
                
        populate_tree(self.tree, rows,
                      ["bill_number", "customer_name", "phone_number",
                       "address", "grand_total", "bill_date"])
        self.item_tree.delete(*self.item_tree.get_children())

    def _get_selected_bill(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return self.tree.item(sel[0], "values")[0]  # Return unique bill_number identifier string

    def _view_bill_details(self):
        bn = self._get_selected_bill()
        if not bn:
            return
            
        items = get_bill_items(bn)
        self.item_tree.delete(*self.item_tree.get_children())
        
        for i, item in enumerate(items):
            tag = "alt" if i % 2 == 1 else ""
            self.item_tree.insert(
                "", "end", 
                values=(
                    item["product_name"], 
                    item["quantity"],
                    f"₹ {item['price_per_item']:,.2f}",
                    f"₹ {item['total_bill']:,.2f}",
                ), 
                tags=(tag,)
            )
        self.item_tree.tag_configure("alt", background=T()["tree_alt"])

    def _export_pdf(self):
        bn = self._get_selected_bill()
        if not bn:
            messagebox.showinfo("Selection Required", "Please select an invoice from the ledger queue first.")
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
        
        try:
            path = generate_pdf_bill(bill_data)
            open_file(path)
            Toast(self.root_ref or self, "Invoice PDF Generated Successfully!", "success")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred while compiling your document file: {e}")
