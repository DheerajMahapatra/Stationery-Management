# # """
# # assets/theme.py
# # Centralized color palette and font definitions for Binod Book Binding.
# # Supports Dark and Light mode.
# # """

# # # ── Color Palettes ─────────────────────────────────────────────────────────────

# # DARK = {
# #     "bg":            "#0f1117",   # deepest background
# #     "sidebar":       "#1a1d27",   # sidebar panel
# #     "card":          "#1e2130",   # card / frame background
# #     "card2":         "#252840",   # alternate card
# #     "accent":        "#4f6ef7",   # primary accent (blue-indigo)
# #     "accent2":       "#f9a825",   # secondary accent (gold)
# #     "accent3":       "#26c281",   # success (green)
# #     "danger":        "#e74c3c",   # danger / delete
# #     "warn":          "#f39c12",   # warning / low stock
# #     "text":          "#e8eaf6",   # primary text
# #     "text2":         "#9e9eb5",   # secondary text / placeholder
# #     "border":        "#2e3250",   # border
# #     "hover":         "#2a2f4a",   # hover bg
# #     "select":        "#3a4080",   # treeview selection
# #     "tree_bg":       "#1a1d27",   # treeview background
# #     "tree_alt":      "#1e2130",   # treeview alternate row
# #     "header_bg":     "#252840",   # treeview header bg
# #     "entry_bg":      "#252840",   # entry field bg
# #     "entry_fg":      "#e8eaf6",   # entry field text
# #     "btn_fg":        "#ffffff",
# #     "mode":          "dark",
# # }

# # LIGHT = {
# #     "bg":            "#f0f2f8",
# #     "sidebar":       "#1a237e",   # deep navy sidebar
# #     "card":          "#ffffff",
# #     "card2":         "#e8eaf6",
# #     "accent":        "#3949ab",
# #     "accent2":       "#f9a825",
# #     "accent3":       "#2e7d32",
# #     "danger":        "#c62828",
# #     "warn":          "#e65100",
# #     "text":          "#1a1a2e",
# #     "text2":         "#5c6bc0",
# #     "border":        "#c5cae9",
# #     "hover":         "#e8eaf6",
# #     "select":        "#3949ab",
# #     "tree_bg":       "#ffffff",
# #     "tree_alt":      "#f3f4ff",
# #     "header_bg":     "#e8eaf6",
# #     "entry_bg":      "#ffffff",
# #     "entry_fg":      "#1a1a2e",
# #     "btn_fg":        "#ffffff",
# #     "mode":          "light",
# # }

# # # Default
# # THEME = DARK


# # def set_theme(mode: str):
# #     global THEME
# #     THEME = DARK if mode == "dark" else LIGHT


# # def get():
# #     return THEME


# # # ── Fonts ──────────────────────────────────────────────────────────────────────
# # FONTS = {
# #     "title":    ("Segoe UI", 20, "bold"),
# #     "heading":  ("Segoe UI", 14, "bold"),
# #     "subhead":  ("Segoe UI", 11, "bold"),
# #     "body":     ("Segoe UI", 10),
# #     "small":    ("Segoe UI", 9),
# #     "mono":     ("Consolas", 10),
# #     "logo":     ("Segoe UI", 16, "bold"),
# #     "nav":      ("Segoe UI", 11),
# #     "btn":      ("Segoe UI", 10, "bold"),
# #     "stat":     ("Segoe UI", 22, "bold"),
# #     "stat_lbl": ("Segoe UI", 9),
# # }


# # # ── Sidebar navigation items ───────────────────────────────────────────────────
# # NAV_ITEMS = [
# #     ("🏠", "Dashboard",    "dashboard"),
# #     ("📦", "Products",     "products"),
# #     ("🧾", "Billing",      "billing"),
# #     ("📋", "Bills History","bills"),
# #     ("👤", "Customers",    "customers"),
# #     ("⚙️", "Settings",     "settings"),
# # ]









# # """
# # assets/theme.py
# # Ultra Professional Theme System
# # Binod Book Binding Management Software
# # Modern Enterprise UI Theme
# # """

# # # ================= DARK THEME =================

# # DARK = {

# #     # MAIN COLORS
# #     "bg": "#0b1220",
# #     "sidebar": "#111827",

# #     # CARDS
# #     "card": "#1e293b",
# #     "card2": "#162033",

# #     # ACCENTS
# #     "accent": "#2563eb",
# #     "accent2": "#06b6d4",
# #     "accent3": "#10b981",

# #     # STATUS COLORS
# #     "danger": "#ef4444",
# #     "warn": "#f59e0b",
# #     "success": "#22c55e",

# #     # TEXT
# #     "text": "#f8fafc",
# #     "text2": "#94a3b8",

# #     # BORDERS
# #     "border": "#334155",

# #     # HOVER EFFECTS
# #     "hover": "#1e293b",
# #     "select": "#2563eb",

# #     # TREEVIEW
# #     "tree_bg": "#111827",
# #     "tree_alt": "#172033",

# #     # TABLE HEADER
# #     "header_bg": "#2563eb",

# #     # ENTRY
# #     "entry_bg": "#0f172a",
# #     "entry_fg": "#f8fafc",

# #     # BUTTON
# #     "btn_fg": "#ffffff",

# #     # EXTRA
# #     "table_bg": "#172033",
# #     "table_hover": "#22304a",

# #     "mode": "dark",
# # }


# # # ================= LIGHT THEME =================

# # LIGHT = {

# #     "bg": "#f1f5f9",
# #     "sidebar": "#1e293b",

# #     "card": "#ffffff",
# #     "card2": "#e2e8f0",

# #     "accent": "#2563eb",
# #     "accent2": "#06b6d4",
# #     "accent3": "#16a34a",

# #     "danger": "#dc2626",
# #     "warn": "#ea580c",
# #     "success": "#16a34a",

# #     "text": "#0f172a",
# #     "text2": "#475569",

# #     "border": "#cbd5e1",

# #     "hover": "#dbeafe",
# #     "select": "#2563eb",

# #     "tree_bg": "#ffffff",
# #     "tree_alt": "#f8fafc",

# #     "header_bg": "#2563eb",

# #     "entry_bg": "#ffffff",
# #     "entry_fg": "#0f172a",

# #     "btn_fg": "#ffffff",

# #     "table_bg": "#f8fafc",
# #     "table_hover": "#dbeafe",

# #     "mode": "light",
# # }


# # # ================= DEFAULT =================

# # THEME = DARK


# # # ================= SET THEME =================

# # def set_theme(mode: str):

# #     global THEME

# #     THEME = DARK if mode == "dark" else LIGHT


# # # ================= GET THEME =================

# # def get():

# #     return THEME


# # # ================= FONTS =================

# # FONTS = {

# #     # TITLES
# #     "title": ("Segoe UI", 26, "bold"),
# #     "heading": ("Segoe UI", 18, "bold"),
# #     "subhead": ("Segoe UI", 13, "bold"),

# #     # BODY
# #     "body": ("Segoe UI", 10),
# #     "small": ("Segoe UI", 9),

# #     # SPECIAL
# #     "mono": ("Consolas", 10),

# #     # SIDEBAR
# #     "logo": ("Segoe UI", 20, "bold"),
# #     "nav": ("Segoe UI", 11),

# #     # BUTTONS
# #     "btn": ("Segoe UI", 10, "bold"),

# #     # DASHBOARD STATS
# #     "stat": ("Segoe UI", 28, "bold"),
# #     "stat_lbl": ("Segoe UI", 10),

# #     # TABLES
# #     "table_head": ("Segoe UI", 10, "bold"),
# #     "table_body": ("Segoe UI", 10),

# #     # BIG NUMBERS
# #     "big": ("Segoe UI", 36, "bold"),
# # }


# # # ================= NAVIGATION =================

# # NAV_ITEMS = [

# #     ("🏠", "Dashboard", "dashboard"),

# #     ("📦", "Products", "products"),

# #     ("🧾", "Billing", "billing"),

# #     ("📋", "Sales History", "bills"),

# #     ("⚙️", "Settings", "settings"),
# # ]










# # assets/theme.py
# # ✨ Premium Aesthetic Theme System ✨
# # Binod Book Binding Management Software
# # Modern, Professional, Visually Stunning UI Theme

# from typing import Dict, Any

# # ================= 🎨 PREMIUM DARK THEME =================
# # Deep, sophisticated dark theme with vibrant accents

# PREMIUM_DARK: Dict[str, Any] = {

#     # === MAIN BACKGROUNDS ===
#     "bg": "#0A0E17",              # Deepest background - rich dark blue-black
#     "sidebar": "#0F1420",         # Sidebar - slightly lighter than main bg
#     "card": "#151C2C",            # Card background - elegant navy tone
#     "card2": "#1A2235",           # Secondary card variant
    
#     # === GRADIENTS (for special elements) ===
#     "gradient_primary": ["#4F46E5", "#7C3AED"],  # Indigo to purple
#     "gradient_success": ["#10B981", "#34D399"],  # Emerald green
#     "gradient_danger": ["#EF4444", "#F87171"],   # Coral red
#     "gradient_accent": ["#3B82F6", "#06B6D4"],   # Blue to cyan
    
#     # === PRIMARY ACCENTS ===
#     "accent": "#6366F1",          # Primary - Indigo (modern, professional)
#     "accent2": "#8B5CF6",         # Secondary - Violet (creative flair)
#     "accent3": "#10B981",         # Tertiary - Emerald (success/payment)
    
#     # === STATUS COLORS ===
#     "danger": "#EF4444",          # Error/Delete - vibrant red
#     "warn": "#F59E0B",            # Warning/Low stock - amber
#     "success": "#10B981",         # Success - emerald green
#     "info": "#3B82F6",            # Information - bright blue
    
#     # === TEXT COLORS ===
#     "text": "#F1F5F9",            # Primary text - off-white
#     "text2": "#94A3B8",           # Secondary text - slate gray
#     "text3": "#64748B",           # Tertiary text - darker slate
#     "text_inverse": "#0F172A",    # Text on light backgrounds
    
#     # === BORDERS & DIVIDERS ===
#     "border": "#1E293B",          # Standard border
#     "border_light": "#334155",    # Lighter border for subtle separation
#     "border_focus": "#818CF8",    # Focus state border
    
#     # === HOVER & INTERACTION STATES ===
#     "hover": "#1E293B",           # Hover background
#     "hover_accent": "#4F46E5",    # Hover on accent elements
#     "select": "#4338CA",          # Selection background
#     "active": "#312E81",          # Active state
    
#     # === TABLE/GRID ELEMENTS ===
#     "tree_bg": "#111827",         # Table row background
#     "tree_alt": "#1A2235",        # Alternate row background
#     "tree_hover": "#1E293B",      # Row hover state
#     "table_header_bg": "#1E293B", # Header background
#     "table_header_text": "#F1F5F9", # Header text
    
#     # === FORM ELEMENTS ===
#     "entry_bg": "#0F172A",        # Input field background
#     "entry_fg": "#F1F5F9",        # Input text
#     "entry_border": "#334155",    # Input border
#     "entry_focus_border": "#6366F1", # Input focus border
#     "placeholder": "#64748B",      # Placeholder text
    
#     # === BUTTONS ===
#     "btn_primary": "#6366F1",     # Primary button
#     "btn_secondary": "#475569",   # Secondary button
#     "btn_success": "#10B981",     # Success button
#     "btn_danger": "#EF4444",      # Danger button
#     "btn_warning": "#F59E0B",     # Warning button
    
#     # === CARD SPECIFIC ===
#     "card_shadow": "#00000020",   # Shadow color for cards
#     "card_border": "#1E293B",     # Card border color
#     "card_glow": "#6366F120",     # Card glow effect
    
#     # === CHART & STATS ===
#     "chart_1": "#6366F1",         # Primary chart color
#     "chart_2": "#10B981",         # Secondary chart color
#     "chart_3": "#F59E0B",         # Tertiary chart color
#     "chart_4": "#EF4444",         # Quaternary chart color
#     "chart_5": "#8B5CF6",         # Quinary chart color
    
#     # === MODAL & DIALOG ===
#     "modal_bg": "#151C2C",        # Modal background
#     "modal_overlay": "#0A0E17CC",  # Modal overlay (with opacity)
    
#     # === TOAST & NOTIFICATION ===
#     "toast_success": "#065F46",   # Success toast bg
#     "toast_error": "#991B1B",     # Error toast bg
#     "toast_warning": "#92400E",   # Warning toast bg
#     "toast_info": "#1E40AF",      # Info toast bg
    
#     # === SIDEBAR SPECIFIC ===
#     "sidebar_active": "#4F46E5",  # Active sidebar item
#     "sidebar_hover": "#1E293B",   # Sidebar hover state
#     "sidebar_icon": "#94A3B8",    # Sidebar icon color
#     "sidebar_text": "#94A3B8",    # Sidebar text color
#     "sidebar_text_active": "#F1F5F9", # Active sidebar text
    
#     # === HEADER ===
#     "header_bg": "#0F1420",       # Header background
#     "header_text": "#F1F5F9",     # Header text
    
#     # === MISCELLANEOUS ===
#     "scrollbar_bg": "#1E293B",    # Scrollbar track
#     "scrollbar_thumb": "#475569", # Scrollbar thumb
#     "scrollbar_thumb_hover": "#6366F1", # Scrollbar thumb hover
#     "progress_bg": "#1E293B",     # Progress bar background
#     "progress_fill": "#6366F1",   # Progress bar fill
    
#     "mode": "dark",
#     "version": "2.0",
#     "name": "Premium Dark"
# }


# # ================= ☀️ PREMIUM LIGHT THEME =================
# # Clean, bright, professional light theme

# PREMIUM_LIGHT: Dict[str, Any] = {

#     # === MAIN BACKGROUNDS ===
#     "bg": "#F8FAFC",              # Very light slate background
#     "sidebar": "#FFFFFF",         # Pure white sidebar
#     "card": "#FFFFFF",            # Pure white cards
#     "card2": "#F1F5F9",           # Slightly off-white secondary
    
#     # === GRADIENTS ===
#     "gradient_primary": ["#4F46E5", "#7C3AED"],
#     "gradient_success": ["#10B981", "#34D399"],
#     "gradient_danger": ["#EF4444", "#F87171"],
#     "gradient_accent": ["#3B82F6", "#06B6D4"],
    
#     # === PRIMARY ACCENTS ===
#     "accent": "#4F46E5",          # Primary - Indigo
#     "accent2": "#7C3AED",         # Secondary - Purple
#     "accent3": "#059669",         # Tertiary - Emerald
    
#     # === STATUS COLORS ===
#     "danger": "#DC2626",          # Error/Delete
#     "warn": "#D97706",            # Warning
#     "success": "#059669",         # Success
#     "info": "#2563EB",            # Information
    
#     # === TEXT COLORS ===
#     "text": "#0F172A",            # Primary text - dark slate
#     "text2": "#475569",           # Secondary text - slate
#     "text3": "#64748B",           # Tertiary text - light slate
#     "text_inverse": "#FFFFFF",    # Text on dark backgrounds
    
#     # === BORDERS & DIVIDERS ===
#     "border": "#E2E8F0",          # Standard border
#     "border_light": "#F1F5F9",    # Lighter border
#     "border_focus": "#6366F1",    # Focus state border
    
#     # === HOVER & INTERACTION STATES ===
#     "hover": "#F1F5F9",           # Hover background
#     "hover_accent": "#4338CA",    # Hover on accent elements
#     "select": "#C7D2FE",          # Selection background
#     "active": "#E0E7FF",          # Active state
    
#     # === TABLE/GRID ELEMENTS ===
#     "tree_bg": "#FFFFFF",         # Table row background
#     "tree_alt": "#F8FAFC",        # Alternate row background
#     "tree_hover": "#F1F5F9",      # Row hover state
#     "table_header_bg": "#F1F5F9", # Header background
#     "table_header_text": "#0F172A", # Header text
    
#     # === FORM ELEMENTS ===
#     "entry_bg": "#FFFFFF",        # Input field background
#     "entry_fg": "#0F172A",        # Input text
#     "entry_border": "#E2E8F0",    # Input border
#     "entry_focus_border": "#6366F1", # Input focus border
#     "placeholder": "#94A3B8",     # Placeholder text
    
#     # === BUTTONS ===
#     "btn_primary": "#4F46E5",     # Primary button
#     "btn_secondary": "#64748B",   # Secondary button
#     "btn_success": "#059669",     # Success button
#     "btn_danger": "#DC2626",      # Danger button
#     "btn_warning": "#D97706",     # Warning button
    
#     # === CARD SPECIFIC ===
#     "card_shadow": "#0F172A0A",   # Shadow color for cards
#     "card_border": "#E2E8F0",     # Card border color
#     "card_glow": "#4F46E520",     # Card glow effect
    
#     # === CHART & STATS ===
#     "chart_1": "#4F46E5",
#     "chart_2": "#059669",
#     "chart_3": "#D97706",
#     "chart_4": "#DC2626",
#     "chart_5": "#7C3AED",
    
#     # === MODAL & DIALOG ===
#     "modal_bg": "#FFFFFF",
#     "modal_overlay": "#0F172A66",
    
#     # === TOAST & NOTIFICATION ===
#     "toast_success": "#ECFDF5",
#     "toast_error": "#FEF2F2",
#     "toast_warning": "#FFFBEB",
#     "toast_info": "#EFF6FF",
    
#     # === SIDEBAR SPECIFIC ===
#     "sidebar_active": "#4F46E5",
#     "sidebar_hover": "#F1F5F9",
#     "sidebar_icon": "#64748B",
#     "sidebar_text": "#475569",
#     "sidebar_text_active": "#FFFFFF",
    
#     # === HEADER ===
#     "header_bg": "#FFFFFF",
#     "header_text": "#0F172A",
    
#     # === MISCELLANEOUS ===
#     "scrollbar_bg": "#E2E8F0",
#     "scrollbar_thumb": "#94A3B8",
#     "scrollbar_thumb_hover": "#4F46E5",
#     "progress_bg": "#E2E8F0",
#     "progress_fill": "#4F46E5",
    
#     "mode": "light",
#     "version": "2.0",
#     "name": "Premium Light"
# }


# # ================= 🌙 DEFAULT THEME (Premium Dark) =================
# THEME = PREMIUM_DARK


# # ================= 🎯 THEME SWITCHER =================

# def set_theme(mode: str) -> None:
#     """
#     Switch between dark and light themes.
    
#     Args:
#         mode: 'dark' or 'light'
#     """
#     global THEME
    
#     if mode.lower() == 'dark':
#         THEME = PREMIUM_DARK
#     elif mode.lower() == 'light':
#         THEME = PREMIUM_LIGHT
#     else:
#         raise ValueError(f"Invalid theme mode: {mode}. Use 'dark' or 'light'.")


# def get() -> Dict[str, Any]:
#     """
#     Get current theme configuration.
    
#     Returns:
#         Current theme dictionary
#     """
#     return THEME


# def get_gradient(gradient_name: str) -> tuple:
#     """
#     Get gradient colors by name.
    
#     Args:
#         gradient_name: 'primary', 'success', 'danger', or 'accent'
    
#     Returns:
#         Tuple of (start_color, end_color)
#     """
#     gradients = {
#         'primary': THEME.get('gradient_primary', ['#4F46E5', '#7C3AED']),
#         'success': THEME.get('gradient_success', ['#10B981', '#34D399']),
#         'danger': THEME.get('gradient_danger', ['#EF4444', '#F87171']),
#         'accent': THEME.get('gradient_accent', ['#3B82F6', '#06B6D4']),
#     }
#     return gradients.get(gradient_name, gradients['primary'])


# def is_dark_mode() -> bool:
#     """Check if current theme is dark mode."""
#     return THEME.get('mode') == 'dark'


# # ================= 🔤 TYPOGRAPHY SYSTEM =================
# # Modern, readable font stack with fallbacks

# FONTS = {
#     # === TITLES & HEADINGS ===
#     "title": ("Inter", "Segoe UI", "Helvetica Neue", 32, "bold"),
#     "title_large": ("Inter", "Segoe UI", "Helvetica Neue", 40, "bold"),
#     "heading": ("Inter", "Segoe UI", "Helvetica Neue", 20, "bold"),
#     "subhead": ("Inter", "Segoe UI", "Helvetica Neue", 15, "semibold"),
#     "h1": ("Inter", "Segoe UI", "Helvetica Neue", 28, "bold"),
#     "h2": ("Inter", "Segoe UI", "Helvetica Neue", 24, "bold"),
#     "h3": ("Inter", "Segoe UI", "Helvetica Neue", 20, "semibold"),
#     "h4": ("Inter", "Segoe UI", "Helvetica Neue", 18, "semibold"),
    
#     # === BODY TEXT ===
#     "body": ("Inter", "Segoe UI", "Helvetica Neue", 11, "normal"),
#     "body_large": ("Inter", "Segoe UI", "Helvetica Neue", 13, "normal"),
#     "body_small": ("Inter", "Segoe UI", "Helvetica Neue", 10, "normal"),
#     "body_bold": ("Inter", "Segoe UI", "Helvetica Neue", 11, "bold"),
    
#     # === SPECIAL TEXT ===
#     "small": ("Inter", "Segoe UI", "Helvetica Neue", 9, "normal"),
#     "caption": ("Inter", "Segoe UI", "Helvetica Neue", 8, "normal"),
#     "mono": ("JetBrains Mono", "Consolas", "Monaco", 10, "normal"),
#     "mono_bold": ("JetBrains Mono", "Consolas", "Monaco", 10, "bold"),
    
#     # === UI ELEMENTS ===
#     "logo": ("Inter", "Segoe UI", "Helvetica Neue", 22, "bold"),
#     "nav": ("Inter", "Segoe UI", "Helvetica Neue", 12, "medium"),
#     "nav_active": ("Inter", "Segoe UI", "Helvetica Neue", 12, "bold"),
#     "btn": ("Inter", "Segoe UI", "Helvetica Neue", 11, "semibold"),
#     "btn_large": ("Inter", "Segoe UI", "Helvetica Neue", 13, "semibold"),
#     "btn_small": ("Inter", "Segoe UI", "Helvetica Neue", 10, "semibold"),
    
#     # === TABLES ===
#     "table_head": ("Inter", "Segoe UI", "Helvetica Neue", 11, "bold"),
#     "table_body": ("Inter", "Segoe UI", "Helvetica Neue", 11, "normal"),
    
#     # === STATS & METRICS ===
#     "stat": ("Inter", "Segoe UI", "Helvetica Neue", 32, "bold"),
#     "stat_large": ("Inter", "Segoe UI", "Helvetica Neue", 40, "bold"),
#     "stat_label": ("Inter", "Segoe UI", "Helvetica Neue", 11, "medium"),
    
#     # === DASHBOARD ===
#     "dashboard_title": ("Inter", "Segoe UI", "Helvetica Neue", 24, "bold"),
#     "dashboard_value": ("Inter", "Segoe UI", "Helvetica Neue", 36, "bold"),
    
#     # === FORMS ===
#     "label": ("Inter", "Segoe UI", "Helvetica Neue", 11, "medium"),
#     "input": ("Inter", "Segoe UI", "Helvetica Neue", 11, "normal"),
#     "placeholder": ("Inter", "Segoe UI", "Helvetica Neue", 11, "normal"),
    
#     # === BIG NUMBERS ===
#     "big": ("Inter", "Segoe UI", "Helvetica Neue", 42, "bold"),
#     "huge": ("Inter", "Segoe UI", "Helvetica Neue", 56, "bold"),
# }


# # Helper function to get proper font tuple
# def get_font(key: str) -> tuple:
#     """Get font tuple by key with proper fallback."""
#     font_definition = FONTS.get(key, FONTS["body"])
#     # Filter out None values and ensure all parts are strings
#     return tuple(str(part) for part in font_definition if part is not None)


# # ================= 🧭 NAVIGATION STRUCTURE =================
# # Organized navigation items with icons and routes

# NAV_ITEMS = [
#     {
#         "icon": "🏠",
#         "label": "Dashboard",
#         "route": "dashboard",
#         "description": "Overview and analytics"
#     },
#     {
#         "icon": "📦",
#         "label": "Products",
#         "route": "products",
#         "description": "Manage inventory"
#     },
#     {
#         "icon": "🧾",
#         "label": "Billing",
#         "route": "billing",
#         "description": "Point of Sale"
#     },
#     {
#         "icon": "📋",
#         "label": "Sales History",
#         "route": "bills",
#         "description": "View past transactions"
#     },
#     {
#         "icon": "⚙️",
#         "label": "Settings",
#         "route": "settings",
#         "description": "System preferences"
#     },
# ]


# # ================= 🎨 CSS-LIKE STYLE HELPERS =================

# def card_style() -> Dict[str, Any]:
#     """Returns card styling attributes."""
#     t = THEME
#     return {
#         "bg": t["card"],
#         "relief": "flat",
#         "bd": 0,
#         "highlightthickness": 1,
#         "highlightbackground": t["card_border"],
#         "highlightcolor": t["accent"]
#     }


# def button_style(variant: str = "primary") -> Dict[str, Any]:
#     """Returns button styling based on variant."""
#     t = THEME
#     variants = {
#         "primary": {"bg": t["btn_primary"], "fg": "#FFFFFF"},
#         "secondary": {"bg": t["btn_secondary"], "fg": "#FFFFFF"},
#         "success": {"bg": t["btn_success"], "fg": "#FFFFFF"},
#         "danger": {"bg": t["btn_danger"], "fg": "#FFFFFF"},
#         "warning": {"bg": t["btn_warning"], "fg": "#FFFFFF"},
#         "outline": {"bg": "transparent", "fg": t["accent"], "highlightbackground": t["accent"]}
#     }
#     return variants.get(variant, variants["primary"])


# def get_shadow_color() -> str:
#     """Returns appropriate shadow color for current theme."""
#     return THEME.get("card_shadow", "#00000020")


# # ================= 📦 EXPORTS =================

# __all__ = [
#     'DARK',
#     'LIGHT',
#     'THEME',
#     'PREMIUM_DARK',
#     'PREMIUM_LIGHT',
#     'FONTS',
#     'NAV_ITEMS',
#     'set_theme',
#     'get',
#     'get_gradient',
#     'is_dark_mode',
#     'get_font',
#     'card_style',
#     'button_style',
#     'get_shadow_color'
# ]

















# assets/theme.py
# ✨ Premium Aesthetic Theme System ✨
# Binod Book Binding Management Software
# Modern, Professional, Visually Stunning UI Theme

from typing import Dict, Any

# ================= 🎨 PREMIUM DARK THEME =================
# Deep, sophisticated dark theme with vibrant accents

PREMIUM_DARK: Dict[str, Any] = {

    # === MAIN BACKGROUNDS ===
    "bg": "#0A0E17",              # Deepest background - rich dark blue-black
    "sidebar": "#0F1420",         # Sidebar - slightly lighter than main bg
    "card": "#151C2C",            # Card background - elegant navy tone
    "card2": "#1A2235",           # Secondary card variant
    
    # === PRIMARY ACCENTS ===
    "accent": "#6366F1",          # Primary - Indigo (modern, professional)
    "accent2": "#8B5CF6",         # Secondary - Violet (creative flair)
    "accent3": "#10B981",         # Tertiary - Emerald (success/payment)
    
    # === STATUS COLORS ===
    "danger": "#EF4444",          # Error/Delete - vibrant red
    "warn": "#F59E0B",            # Warning/Low stock - amber
    "success": "#10B981",         # Success - emerald green
    "info": "#3B82F6",            # Information - bright blue
    
    # === TEXT COLORS ===
    "text": "#F1F5F9",            # Primary text - off-white
    "text2": "#94A3B8",           # Secondary text - slate gray
    "text3": "#64748B",           # Tertiary text - darker slate
    "text_inverse": "#0F172A",    # Text on light backgrounds
    
    # === BORDERS & DIVIDERS ===
    "border": "#1E293B",          # Standard border
    "border_light": "#334155",    # Lighter border for subtle separation
    "border_focus": "#818CF8",    # Focus state border
    
    # === HOVER & INTERACTION STATES ===
    "hover": "#1E293B",           # Hover background
    "hover_accent": "#4F46E5",    # Hover on accent elements
    "select": "#4338CA",          # Selection background
    "active": "#312E81",          # Active state
    
    # === TABLE/GRID ELEMENTS ===
    "tree_bg": "#111827",         # Table row background
    "tree_alt": "#1A2235",        # Alternate row background
    "tree_hover": "#1E293B",      # Row hover state
    "header_bg": "#2563eb",       # Header background
    "table_header_bg": "#1E293B", # Header background
    
    # === FORM ELEMENTS ===
    "entry_bg": "#0F172A",        # Input field background
    "entry_fg": "#F1F5F9",        # Input text
    "entry_border": "#334155",    # Input border
    "entry_focus_border": "#6366F1", # Input focus border
    
    # === BUTTONS ===
    "btn_primary": "#6366F1",     # Primary button
    "btn_secondary": "#475569",   # Secondary button
    "btn_success": "#10B981",     # Success button
    "btn_danger": "#EF4444",      # Danger button
    "btn_warning": "#F59E0B",     # Warning button
    "btn_fg": "#ffffff",          # Button text color
    
    # === CARD SPECIFIC ===
    "card_border": "#1E293B",     # Card border color
    
    # === MODAL & DIALOG ===
    "modal_bg": "#151C2C",        # Modal background
    
    # === SIDEBAR SPECIFIC ===
    "sidebar_active": "#4F46E5",  # Active sidebar item
    "sidebar_hover": "#1E293B",   # Sidebar hover state
    "sidebar_icon": "#94A3B8",    # Sidebar icon color
    "sidebar_text": "#94A3B8",    # Sidebar text color
    
    # === HEADER ===
    "header_bg": "#0F1420",       # Header background
    
    # === MISCELLANEOUS ===
    "scrollbar_bg": "#1E293B",    # Scrollbar track
    "scrollbar_thumb": "#475569", # Scrollbar thumb
    
    "mode": "dark",
}


# ================= ☀️ PREMIUM LIGHT THEME =================
# Clean, bright, professional light theme

PREMIUM_LIGHT: Dict[str, Any] = {

    # === MAIN BACKGROUNDS ===
    "bg": "#F8FAFC",              # Very light slate background
    "sidebar": "#FFFFFF",         # Pure white sidebar
    "card": "#FFFFFF",            # Pure white cards
    "card2": "#F1F5F9",           # Slightly off-white secondary
    
    # === PRIMARY ACCENTS ===
    "accent": "#4F46E5",          # Primary - Indigo
    "accent2": "#7C3AED",         # Secondary - Purple
    "accent3": "#059669",         # Tertiary - Emerald
    
    # === STATUS COLORS ===
    "danger": "#DC2626",          # Error/Delete
    "warn": "#D97706",            # Warning
    "success": "#059669",         # Success
    "info": "#2563EB",            # Information
    
    # === TEXT COLORS ===
    "text": "#0F172A",            # Primary text - dark slate
    "text2": "#475569",           # Secondary text - slate
    "text3": "#64748B",           # Tertiary text - light slate
    "text_inverse": "#FFFFFF",    # Text on dark backgrounds
    
    # === BORDERS & DIVIDERS ===
    "border": "#E2E8F0",          # Standard border
    "border_light": "#F1F5F9",    # Lighter border
    "border_focus": "#6366F1",    # Focus state border
    
    # === HOVER & INTERACTION STATES ===
    "hover": "#F1F5F9",           # Hover background
    "hover_accent": "#4338CA",    # Hover on accent elements
    "select": "#C7D2FE",          # Selection background
    "active": "#E0E7FF",          # Active state
    
    # === TABLE/GRID ELEMENTS ===
    "tree_bg": "#FFFFFF",         # Table row background
    "tree_alt": "#F8FAFC",        # Alternate row background
    "tree_hover": "#F1F5F9",      # Row hover state
    "header_bg": "#2563eb",       # Header background
    "table_header_bg": "#F1F5F9", # Header background
    
    # === FORM ELEMENTS ===
    "entry_bg": "#FFFFFF",        # Input field background
    "entry_fg": "#0F172A",        # Input text
    "entry_border": "#E2E8F0",    # Input border
    "entry_focus_border": "#6366F1", # Input focus border
    
    # === BUTTONS ===
    "btn_primary": "#4F46E5",     # Primary button
    "btn_secondary": "#64748B",   # Secondary button
    "btn_success": "#059669",     # Success button
    "btn_danger": "#DC2626",      # Danger button
    "btn_warning": "#D97706",     # Warning button
    "btn_fg": "#ffffff",          # Button text color
    
    # === CARD SPECIFIC ===
    "card_border": "#E2E8F0",     # Card border color
    
    # === MODAL & DIALOG ===
    "modal_bg": "#FFFFFF",        # Modal background
    
    # === SIDEBAR SPECIFIC ===
    "sidebar_active": "#4F46E5",  # Active sidebar item
    "sidebar_hover": "#F1F5F9",   # Sidebar hover state
    "sidebar_icon": "#64748B",    # Sidebar icon color
    "sidebar_text": "#475569",    # Sidebar text color
    
    # === HEADER ===
    "header_bg": "#FFFFFF",       # Header background
    
    # === MISCELLANEOUS ===
    "scrollbar_bg": "#E2E8F0",    # Scrollbar track
    "scrollbar_thumb": "#94A3B8", # Scrollbar thumb
    
    "mode": "light",
}


# ================= 🌙 DEFAULT THEME (Premium Dark) =================
THEME = PREMIUM_DARK


# ================= 🎯 THEME SWITCHER =================

def set_theme(mode: str) -> None:
    """
    Switch between dark and light themes.
    
    Args:
        mode: 'dark' or 'light'
    """
    global THEME
    
    if mode.lower() == 'dark':
        THEME = PREMIUM_DARK
    elif mode.lower() == 'light':
        THEME = PREMIUM_LIGHT
    else:
        raise ValueError(f"Invalid theme mode: {mode}. Use 'dark' or 'light'.")


def get() -> Dict[str, Any]:
    """
    Get current theme configuration.
    
    Returns:
        Current theme dictionary
    """
    return THEME


def is_dark_mode() -> bool:
    """Check if current theme is dark mode."""
    return THEME.get('mode') == 'dark'


# ================= 🔤 TYPOGRAPHY SYSTEM =================
# Simplified fonts for Tkinter compatibility - exactly 3 elements each

FONTS = {
    # === TITLES & HEADINGS ===
    "title": ("Segoe UI", 26, "bold"),
    "title_large": ("Segoe UI", 32, "bold"),
    "heading": ("Segoe UI", 18, "bold"),
    "subhead": ("Segoe UI", 13, "bold"),
    "h1": ("Segoe UI", 28, "bold"),
    "h2": ("Segoe UI", 24, "bold"),
    "h3": ("Segoe UI", 20, "bold"),
    "h4": ("Segoe UI", 18, "bold"),
    
    # === BODY TEXT ===
    "body": ("Segoe UI", 11, "normal"),
    "body_large": ("Segoe UI", 13, "normal"),
    "body_small": ("Segoe UI", 10, "normal"),
    "body_bold": ("Segoe UI", 11, "bold"),
    
    # === SPECIAL TEXT ===
    "small": ("Segoe UI", 9, "normal"),
    "caption": ("Segoe UI", 8, "normal"),
    "mono": ("Consolas", 10, "normal"),
    "mono_bold": ("Consolas", 10, "bold"),
    
    # === UI ELEMENTS ===
    "logo": ("Segoe UI", 20, "bold"),
    "nav": ("Segoe UI", 11, "normal"),
    "nav_active": ("Segoe UI", 11, "bold"),
    "btn": ("Segoe UI", 10, "bold"),
    "btn_large": ("Segoe UI", 12, "bold"),
    "btn_small": ("Segoe UI", 9, "bold"),
    
    # === TABLES ===
    "table_head": ("Segoe UI", 10, "bold"),
    "table_body": ("Segoe UI", 10, "normal"),
    
    # === STATS & METRICS ===
    "stat": ("Segoe UI", 28, "bold"),
    "stat_large": ("Segoe UI", 36, "bold"),
    "stat_label": ("Segoe UI", 10, "normal"),
    
    # === DASHBOARD ===
    "dashboard_title": ("Segoe UI", 24, "bold"),
    "dashboard_value": ("Segoe UI", 32, "bold"),
    
    # === FORMS ===
    "label": ("Segoe UI", 10, "normal"),
    "input": ("Segoe UI", 11, "normal"),
    
    # === BIG NUMBERS ===
    "big": ("Segoe UI", 36, "bold"),
    "huge": ("Segoe UI", 48, "bold"),
}


# ================= 🧭 NAVIGATION STRUCTURE =================

NAV_ITEMS = [
    ("🏠", "Dashboard", "dashboard"),
    ("📦", "Products", "products"),
    ("🧾", "Billing", "billing"),
    ("📋", "Sales History", "bills"),
    ("⚙️", "Settings", "settings"),
]


# ================= 📦 EXPORTS =================

__all__ = [
    'PREMIUM_DARK',
    'PREMIUM_LIGHT',
    'THEME',
    'FONTS',
    'NAV_ITEMS',
    'set_theme',
    'get',
    'is_dark_mode',
]