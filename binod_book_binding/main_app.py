"""
main_app.py
Main application window with sidebar navigation.
"""

import tkinter as tk
from tkinter import messagebox
from assets.theme import get as T, FONTS, NAV_ITEMS
from assets.widgets import Toast


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binod Book Binding — Management System")
        self.state("zoomed")          # Start maximized on Windows
        self.minsize(1000, 640)
        self._current_page = None
        self._pages = {}
        self._nav_btns = {}
        self._build_ui()

    def _build_ui(self):
        t = T()
        self.configure(bg=t["bg"])
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ── Sidebar ────────────────────────────────────────────────────────────
        self.sidebar = tk.Frame(self, bg=t["sidebar"], width=220)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self._build_sidebar()

        # ── Content area ───────────────────────────────────────────────────────
        self.content = tk.Frame(self, bg=t["bg"])
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # Load pages lazily
        self._load_pages()

        # Show dashboard by default
        self._show_page("dashboard")

    def _build_sidebar(self):
        t = T()

        # Logo
        logo_frame = tk.Frame(self.sidebar, bg=t["accent"], pady=20)
        logo_frame.pack(fill="x")
        tk.Label(logo_frame, text="📚", bg=t["accent"],
                 font=("Segoe UI", 28)).pack()
        tk.Label(logo_frame, text="Binod Book",
                 bg=t["accent"], fg="#ffffff",
                 font=FONTS["logo"]).pack()
        tk.Label(logo_frame, text="Binding",
                 bg=t["accent"], fg="#c5cae9",
                 font=FONTS["small"]).pack()

        # Nav items
        nav_frame = tk.Frame(self.sidebar, bg=t["sidebar"])
        nav_frame.pack(fill="both", expand=True, pady=12)

        for icon, label, key in NAV_ITEMS:
            btn = tk.Button(
                nav_frame,
                text=f"  {icon}  {label}",
                bg=t["sidebar"], fg=t["text2"],
                activebackground=t["hover"], activeforeground=t["text"],
                relief="flat", bd=0, cursor="hand2",
                anchor="w", padx=16, pady=12,
                font=FONTS["nav"],
                command=lambda k=key: self._show_page(k),
            )
            btn.pack(fill="x")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=t["hover"], fg=t["text"]))
            btn.bind("<Leave>", lambda e, b=btn, k=key: b.config(
                bg=t["select"] if self._current_page == k else t["sidebar"],
                fg=t["text"] if self._current_page == k else t["text2"]
            ))
            self._nav_btns[key] = btn

        # Spacer + logout
        tk.Frame(self.sidebar, bg=t["border"], height=1).pack(fill="x", padx=16, pady=4)

        logout_btn = tk.Button(
            self.sidebar,
            text="  🚪  Logout",
            bg=t["sidebar"], fg=t["danger"],
            activebackground=t["hover"], activeforeground=t["danger"],
            relief="flat", bd=0, cursor="hand2",
            anchor="w", padx=16, pady=12,
            font=FONTS["nav"],
            command=self._logout,
        )
        logout_btn.pack(fill="x", side="bottom", pady=4)

        # Version
        tk.Label(self.sidebar, text="v1.0 — Offline Mode",
                 bg=t["sidebar"], fg=t["text2"],
                 font=FONTS["small"]).pack(side="bottom", pady=4)

    def _load_pages(self):
        """Lazy-load all pages once."""
        from product_module.dashboard_page import DashboardPage
        from product_module.products_page  import ProductsPage
        from billing_module.billing_page   import BillingPage
        from billing_module.bills_history_page import BillsHistoryPage
        from customer_module.customers_page import CustomersPage
        from assets.settings_page          import SettingsPage

        for Page, key, kwargs in [
            (DashboardPage,    "dashboard", {}),
            (ProductsPage,     "products",  {"root_ref": self}),
            (BillingPage,      "billing",   {"root_ref": self,
                                             "on_bill_created": self._on_bill_created}),
            (BillsHistoryPage, "bills",     {"root_ref": self}),
            (CustomersPage,    "customers", {"root_ref": self}),
            (SettingsPage,     "settings",  {"root_ref": self,
                                             "on_theme_change": self._on_theme_change}),
        ]:
            page = Page(self.content, **kwargs)
            page.grid(row=0, column=0, sticky="nsew")
            self._pages[key] = page

    def _show_page(self, key: str):
        t = T()
        # Update sidebar highlight
        for k, btn in self._nav_btns.items():
            if k == key:
                btn.config(bg=t["select"], fg=t["text"])
            else:
                btn.config(bg=t["sidebar"], fg=t["text2"])

        self._current_page = key
        page = self._pages.get(key)
        if page:
            page.tkraise()
            if hasattr(page, "refresh"):
                page.refresh()

    def _on_bill_created(self):
        """Callback: refresh dashboard after a bill is created."""
        if "dashboard" in self._pages:
            self._pages["dashboard"].refresh()
        if "bills" in self._pages:
            self._pages["bills"].refresh()

    def _on_theme_change(self):
        pass  # Full restart needed for complete re-theme

    def _logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.destroy()
