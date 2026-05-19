# """
# assets/theme.py
# Centralized color palette and font definitions for Binod Book Binding.
# Supports Dark and Light mode.
# """

# # ── Color Palettes ─────────────────────────────────────────────────────────────

# DARK = {
#     "bg":            "#0f1117",   # deepest background
#     "sidebar":       "#1a1d27",   # sidebar panel
#     "card":          "#1e2130",   # card / frame background
#     "card2":         "#252840",   # alternate card
#     "accent":        "#4f6ef7",   # primary accent (blue-indigo)
#     "accent2":       "#f9a825",   # secondary accent (gold)
#     "accent3":       "#26c281",   # success (green)
#     "danger":        "#e74c3c",   # danger / delete
#     "warn":          "#f39c12",   # warning / low stock
#     "text":          "#e8eaf6",   # primary text
#     "text2":         "#9e9eb5",   # secondary text / placeholder
#     "border":        "#2e3250",   # border
#     "hover":         "#2a2f4a",   # hover bg
#     "select":        "#3a4080",   # treeview selection
#     "tree_bg":       "#1a1d27",   # treeview background
#     "tree_alt":      "#1e2130",   # treeview alternate row
#     "header_bg":     "#252840",   # treeview header bg
#     "entry_bg":      "#252840",   # entry field bg
#     "entry_fg":      "#e8eaf6",   # entry field text
#     "btn_fg":        "#ffffff",
#     "mode":          "dark",
# }

# LIGHT = {
#     "bg":            "#f0f2f8",
#     "sidebar":       "#1a237e",   # deep navy sidebar
#     "card":          "#ffffff",
#     "card2":         "#e8eaf6",
#     "accent":        "#3949ab",
#     "accent2":       "#f9a825",
#     "accent3":       "#2e7d32",
#     "danger":        "#c62828",
#     "warn":          "#e65100",
#     "text":          "#1a1a2e",
#     "text2":         "#5c6bc0",
#     "border":        "#c5cae9",
#     "hover":         "#e8eaf6",
#     "select":        "#3949ab",
#     "tree_bg":       "#ffffff",
#     "tree_alt":      "#f3f4ff",
#     "header_bg":     "#e8eaf6",
#     "entry_bg":      "#ffffff",
#     "entry_fg":      "#1a1a2e",
#     "btn_fg":        "#ffffff",
#     "mode":          "light",
# }

# # Default
# THEME = DARK


# def set_theme(mode: str):
#     global THEME
#     THEME = DARK if mode == "dark" else LIGHT


# def get():
#     return THEME


# # ── Fonts ──────────────────────────────────────────────────────────────────────
# FONTS = {
#     "title":    ("Segoe UI", 20, "bold"),
#     "heading":  ("Segoe UI", 14, "bold"),
#     "subhead":  ("Segoe UI", 11, "bold"),
#     "body":     ("Segoe UI", 10),
#     "small":    ("Segoe UI", 9),
#     "mono":     ("Consolas", 10),
#     "logo":     ("Segoe UI", 16, "bold"),
#     "nav":      ("Segoe UI", 11),
#     "btn":      ("Segoe UI", 10, "bold"),
#     "stat":     ("Segoe UI", 22, "bold"),
#     "stat_lbl": ("Segoe UI", 9),
# }


# # ── Sidebar navigation items ───────────────────────────────────────────────────
# NAV_ITEMS = [
#     ("🏠", "Dashboard",    "dashboard"),
#     ("📦", "Products",     "products"),
#     ("🧾", "Billing",      "billing"),
#     ("📋", "Bills History","bills"),
#     ("👤", "Customers",    "customers"),
#     ("⚙️", "Settings",     "settings"),
# ]









"""
assets/theme.py
Ultra Professional Theme System
Binod Book Binding Management Software
Modern Enterprise UI Theme
"""

# ================= DARK THEME =================

DARK = {

    # MAIN COLORS
    "bg": "#0b1220",
    "sidebar": "#111827",

    # CARDS
    "card": "#1e293b",
    "card2": "#162033",

    # ACCENTS
    "accent": "#2563eb",
    "accent2": "#06b6d4",
    "accent3": "#10b981",

    # STATUS COLORS
    "danger": "#ef4444",
    "warn": "#f59e0b",
    "success": "#22c55e",

    # TEXT
    "text": "#f8fafc",
    "text2": "#94a3b8",

    # BORDERS
    "border": "#334155",

    # HOVER EFFECTS
    "hover": "#1e293b",
    "select": "#2563eb",

    # TREEVIEW
    "tree_bg": "#111827",
    "tree_alt": "#172033",

    # TABLE HEADER
    "header_bg": "#2563eb",

    # ENTRY
    "entry_bg": "#0f172a",
    "entry_fg": "#f8fafc",

    # BUTTON
    "btn_fg": "#ffffff",

    # EXTRA
    "table_bg": "#172033",
    "table_hover": "#22304a",

    "mode": "dark",
}


# ================= LIGHT THEME =================

LIGHT = {

    "bg": "#f1f5f9",
    "sidebar": "#1e293b",

    "card": "#ffffff",
    "card2": "#e2e8f0",

    "accent": "#2563eb",
    "accent2": "#06b6d4",
    "accent3": "#16a34a",

    "danger": "#dc2626",
    "warn": "#ea580c",
    "success": "#16a34a",

    "text": "#0f172a",
    "text2": "#475569",

    "border": "#cbd5e1",

    "hover": "#dbeafe",
    "select": "#2563eb",

    "tree_bg": "#ffffff",
    "tree_alt": "#f8fafc",

    "header_bg": "#2563eb",

    "entry_bg": "#ffffff",
    "entry_fg": "#0f172a",

    "btn_fg": "#ffffff",

    "table_bg": "#f8fafc",
    "table_hover": "#dbeafe",

    "mode": "light",
}


# ================= DEFAULT =================

THEME = DARK


# ================= SET THEME =================

def set_theme(mode: str):

    global THEME

    THEME = DARK if mode == "dark" else LIGHT


# ================= GET THEME =================

def get():

    return THEME


# ================= FONTS =================

FONTS = {

    # TITLES
    "title": ("Segoe UI", 26, "bold"),
    "heading": ("Segoe UI", 18, "bold"),
    "subhead": ("Segoe UI", 13, "bold"),

    # BODY
    "body": ("Segoe UI", 10),
    "small": ("Segoe UI", 9),

    # SPECIAL
    "mono": ("Consolas", 10),

    # SIDEBAR
    "logo": ("Segoe UI", 20, "bold"),
    "nav": ("Segoe UI", 11),

    # BUTTONS
    "btn": ("Segoe UI", 10, "bold"),

    # DASHBOARD STATS
    "stat": ("Segoe UI", 28, "bold"),
    "stat_lbl": ("Segoe UI", 10),

    # TABLES
    "table_head": ("Segoe UI", 10, "bold"),
    "table_body": ("Segoe UI", 10),

    # BIG NUMBERS
    "big": ("Segoe UI", 36, "bold"),
}


# ================= NAVIGATION =================

NAV_ITEMS = [

    ("🏠", "Dashboard", "dashboard"),

    ("📦", "Products", "products"),

    ("🧾", "Billing", "billing"),

    ("📋", "Sales History", "bills"),

    ("⚙️", "Settings", "settings"),
]