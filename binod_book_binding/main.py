"""
main.py
Entry point for Binod Book Binding Management System.

Run:  python main.py

Requirements:
    Python 3.10+
    reportlab  (optional — for PDF export): pip install reportlab

Default login: admin / admin123
"""

import sys
import os

# ── Ensure the project root is on sys.path ─────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ── Bootstrap database ─────────────────────────────────────────────────────────
from database.db_setup import initialize_database
initialize_database()

# ── Login ──────────────────────────────────────────────────────────────────────
from login_window import LoginWindow
login = LoginWindow()
login.mainloop()

if not login.logged_in:
    sys.exit(0)  # User closed login window

# ── Launch main app ────────────────────────────────────────────────────────────
from main_app import MainApp
app = MainApp()
app.mainloop()
