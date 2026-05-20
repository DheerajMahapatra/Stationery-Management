# assets/theme.py
# ✨ Professional Premium Theme System ✨
# Binod Book Binding Management Software
# Refined color palettes, modern typography, and enhanced utility functions

from typing import Dict, Any, Tuple, Optional

# ================= 🎨 PROFESSIONAL DARK THEME =================
# Sophisticated, low‑glare dark palette with vibrant yet readable accents

PROFESSIONAL_DARK: Dict[str, Any] = {

    # --- BACKGROUND HIERARCHY ---
    "bg":            "#0c0f17",      # Deepest canvas
    "sidebar":       "#111622",      # Slightly elevated
    "card":          "#181c28",      # Card surfaces
    "card2":         "#1e2332",      # Alternative card background
    "card_elevated": "#222839",      # Hovered / focused card

    # --- ACCENT COLOURS ---
    "accent":        "#6c8cff",      # Soft indigo – primary interactive colour
    "accent2":       "#a78bfa",      # Soft violet – secondary emphasis
    "accent3":       "#34d399",      # Mint green – success / positive actions

    # --- SEMANTIC COLOURS ---
    "success":       "#34d399",
    "danger":        "#f87171",      # Soft red for destructive actions
    "warn":          "#fbbf24",      # Amber for warnings
    "info":          "#60a5fa",      # Sky blue for informational elements

    # --- TEXT COLOURS ---
    "text":          "#e9edf5",      # Primary text – excellent contrast
    "text2":         "#8b93a5",      # Secondary / muted text
    "text3":         "#5c6377",      # Disabled / tertiary text
    "text_inverse":  "#0f111a",      # Text on light backgrounds

    # --- BORDERS & SEPARATORS ---
    "border":        "#242a38",      # Standard border
    "border_light":  "#2c3344",      # Softer border
    "border_focus":  "#6c8cff",      # Ring / outline when focused

    # --- INTERACTION STATES ---
    "hover":         "#202433",      # Generic hover background
    "hover_accent":  "#7b9aff",      # Hover over accent-coloured elements
    "select":        "#2d3550",      # Selected / active background
    "active":        "#3a4468",      # Pressed / active state

    # --- TABLE / TREEVIEW ---
    "tree_bg":       "#111622",      # Row background
    "tree_alt":      "#181c28",      # Alternating row
    "tree_hover":    "#202433",      # Row hover
    "header_bg":     "#242a38",      # Column header background
    "header_text":   "#e9edf5",      # Column header text

    # --- FORM INPUTS ---
    "entry_bg":      "#121621",      # Input field background
    "entry_fg":      "#e9edf5",      # Input text
    "entry_border":  "#2c3344",      # Input border
    "entry_focus_border": "#6c8cff",
    "placeholder":   "#5c6377",

    # --- BUTTONS ---
    "btn_fg":        "#ffffff",
    "btn_primary":   "#6c8cff",
    "btn_secondary": "#4b5563",
    "btn_success":   "#34d399",
    "btn_danger":    "#f87171",
    "btn_warning":   "#fbbf24",

    # --- SIDEBAR SPECIFIC ---
    "sidebar_active": "#6c8cff",
    "sidebar_hover":  "#1e2332",
    "sidebar_icon":   "#8b93a5",
    "sidebar_text":   "#8b93a5",
    "sidebar_text_active": "#ffffff",

    # --- SCROLLBAR ---
    "scrollbar_bg":    "#181c28",
    "scrollbar_thumb": "#4b5563",
    "scrollbar_thumb_hover": "#6c8cff",

    # --- MODAL / DIALOG ---
    "modal_bg":      "#181c28",
    "modal_overlay": "#0c0f17b3",

    "mode": "dark",
    "name": "Professional Dark"
}


# ================= ☀️ PROFESSIONAL LIGHT THEME =================
# Clean, airy, high‑readability light palette

PROFESSIONAL_LIGHT: Dict[str, Any] = {

    # --- BACKGROUND HIERARCHY ---
    "bg":            "#f4f6fb",      # Page background
    "sidebar":       "#ffffff",      # Crisp white sidebar
    "card":          "#ffffff",      # Card surfaces
    "card2":         "#f0f2f8",      # Subtle offset card
    "card_elevated": "#ffffff",      # Raised card

    # --- ACCENT COLOURS ---
    "accent":        "#4f5de4",      # Strong indigo
    "accent2":       "#7c3aed",      # Violet
    "accent3":       "#059669",      # Deep green

    # --- SEMANTIC COLOURS ---
    "success":       "#059669",
    "danger":        "#dc2626",
    "warn":          "#d97706",
    "info":          "#2563eb",

    # --- TEXT COLOURS ---
    "text":          "#0f172a",      # Almost black – excellent contrast
    "text2":         "#475569",      # Medium slate
    "text3":         "#94a3b8",      # Light slate
    "text_inverse":  "#ffffff",

    # --- BORDERS & SEPARATORS ---
    "border":        "#e2e8f0",
    "border_light":  "#f1f5f9",
    "border_focus":  "#4f5de4",

    # --- INTERACTION STATES ---
    "hover":         "#f1f5f9",
    "hover_accent":  "#4338ca",
    "select":        "#e0e7ff",
    "active":        "#c7d2fe",

    # --- TABLE / TREEVIEW ---
    "tree_bg":       "#ffffff",
    "tree_alt":      "#f8fafc",
    "tree_hover":    "#f1f5f9",
    "header_bg":     "#f1f5f9",
    "header_text":   "#0f172a",

    # --- FORM INPUTS ---
    "entry_bg":      "#ffffff",
    "entry_fg":      "#0f172a",
    "entry_border":  "#e2e8f0",
    "entry_focus_border": "#4f5de4",
    "placeholder":   "#94a3b8",

    # --- BUTTONS ---
    "btn_fg":        "#ffffff",
    "btn_primary":   "#4f5de4",
    "btn_secondary": "#64748b",
    "btn_success":   "#059669",
    "btn_danger":    "#dc2626",
    "btn_warning":   "#d97706",

    # --- SIDEBAR SPECIFIC ---
    "sidebar_active": "#4f5de4",
    "sidebar_hover":  "#f1f5f9",
    "sidebar_icon":   "#64748b",
    "sidebar_text":   "#475569",
    "sidebar_text_active": "#ffffff",

    # --- SCROLLBAR ---
    "scrollbar_bg":    "#f1f5f9",
    "scrollbar_thumb": "#cbd5e1",
    "scrollbar_thumb_hover": "#4f5de4",

    # --- MODAL / DIALOG ---
    "modal_bg":      "#ffffff",
    "modal_overlay": "#0f172a66",

    "mode": "light",
    "name": "Professional Light"
}


# ================= 🌙 DEFAULT THEME =================
THEME = PROFESSIONAL_DARK


# ================= 🎯 THEME SWITCHING =================

def set_theme(mode: str) -> None:
    """Switch between 'dark' and 'light' professional themes."""
    global THEME
    mode = mode.lower()
    if mode == 'dark':
        THEME = PROFESSIONAL_DARK
    elif mode == 'light':
        THEME = PROFESSIONAL_LIGHT
    else:
        raise ValueError(f"Unknown theme mode: {mode}. Use 'dark' or 'light'.")


def get() -> Dict[str, Any]:
    """Return the current theme dictionary."""
    return THEME


def get_color(key: str, fallback: str = "#000000") -> str:
    """Safely retrieve a colour from the current theme."""
    return THEME.get(key, fallback)


def is_dark_mode() -> bool:
    """Check if the current theme is dark."""
    return THEME.get('mode') == 'dark'


def get_hover_color(base_color: str, darken: float = 0.15) -> str:
    """
    Return a slightly darker/lighter version of a hex colour for hover states.
    Simple heuristic – works best for solid buttons.
    """
    base_color = base_color.lstrip('#')
    r, g, b = int(base_color[0:2], 16), int(base_color[2:4], 16), int(base_color[4:6], 16)
    # darken
    r = max(0, int(r * (1 - darken)))
    g = max(0, int(g * (1 - darken)))
    b = max(0, int(b * (1 - darken)))
    return f"#{r:02x}{g:02x}{b:02x}"


# ================= 🔤 TYPOGRAPHY SYSTEM =================
# Clean, modern font stack – all Tkinter‑compatible (3‑tuple)

FONTS = {
    # Titles & headings
    "title":          ("Segoe UI", 26, "bold"),
    "title_large":    ("Segoe UI", 32, "bold"),
    "heading":        ("Segoe UI", 18, "bold"),
    "subhead":        ("Segoe UI", 13, "bold"),
    "h1":             ("Segoe UI", 28, "bold"),
    "h2":             ("Segoe UI", 24, "bold"),
    "h3":             ("Segoe UI", 20, "bold"),
    "h4":             ("Segoe UI", 18, "bold"),

    # Body text
    "body":           ("Segoe UI", 11),
    "body_large":     ("Segoe UI", 13),
    "body_small":     ("Segoe UI", 10),
    "body_bold":      ("Segoe UI", 11, "bold"),

    # Special
    "small":          ("Segoe UI", 9),
    "caption":        ("Segoe UI", 8),
    "mono":           ("Consolas", 10),
    "mono_bold":      ("Consolas", 10, "bold"),

    # UI elements
    "logo":           ("Segoe UI", 20, "bold"),
    "nav":            ("Segoe UI", 11),
    "nav_active":     ("Segoe UI", 11, "bold"),
    "btn":            ("Segoe UI", 10, "bold"),
    "btn_large":      ("Segoe UI", 12, "bold"),
    "btn_small":      ("Segoe UI", 9, "bold"),

    # Tables
    "table_head":     ("Segoe UI", 10, "bold"),
    "table_body":     ("Segoe UI", 10),

    # Stats & metrics
    "stat":           ("Segoe UI", 28, "bold"),
    "stat_large":     ("Segoe UI", 36, "bold"),
    "stat_label":     ("Segoe UI", 10),

    # Dashboard
    "dashboard_title": ("Segoe UI", 24, "bold"),
    "dashboard_value": ("Segoe UI", 32, "bold"),

    # Forms
    "label":          ("Segoe UI", 10),
    "input":          ("Segoe UI", 11),

    # Big numbers
    "big":            ("Segoe UI", 36, "bold"),
    "huge":           ("Segoe UI", 48, "bold"),
}


# ================= 🧭 NAVIGATION STRUCTURE =================
NAV_ITEMS = [
    ("🏠", "Dashboard",    "dashboard"),
    ("📦", "Products",     "products"),
    ("🧾", "Billing",      "billing"),
    ("📋", "Sales History", "bills"),
    ("⚙️", "Settings",     "settings"),
]


# ================= 📦 EXPORTS =================
__all__ = [
    'PROFESSIONAL_DARK',
    'PROFESSIONAL_LIGHT',
    'THEME',
    'FONTS',
    'NAV_ITEMS',
    'set_theme',
    'get',
    'get_color',
    'is_dark_mode',
    'get_hover_color',
]