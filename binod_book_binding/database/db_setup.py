# """
# database/db_setup.py
# Database setup and connection for Binod Book Binding
# """

# import sqlite3
# import os
# import hashlib
# from datetime import datetime

# # Database file path
# DB_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(DB_DIR, "binod_book_binding.db")


# def get_connection():
#     """Return a connection to the SQLite database."""
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row  # Access columns by name
#     conn.execute("PRAGMA foreign_keys = ON")
#     return conn


# def hash_password(password: str) -> str:
#     """Return SHA-256 hash of password."""
#     return hashlib.sha256(password.encode()).hexdigest()


# def initialize_database():
#     """Create all tables if they don't exist and seed default data."""
#     conn = get_connection()
#     cursor = conn.cursor()

#     # ── Users / Login ──────────────────────────────────────────────────────────
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
#             username  TEXT    NOT NULL UNIQUE,
#             password  TEXT    NOT NULL,
#             role      TEXT    DEFAULT 'admin',
#             created_at TEXT   DEFAULT (datetime('now','localtime'))
#         )
#     """)

#     # Seed default admin if none exists
#     cursor.execute("SELECT COUNT(*) FROM users")
#     if cursor.fetchone()[0] == 0:
#         cursor.execute(
#             "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
#             ("admin", hash_password("admin123"), "admin"),
#         )

#     # ── Products ───────────────────────────────────────────────────────────────
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS product_db (
#             product_id   INTEGER PRIMARY KEY AUTOINCREMENT,
#             product_name TEXT    NOT NULL,
#             category     TEXT    NOT NULL,
#             quantity     INTEGER NOT NULL DEFAULT 0,
#             price        REAL    NOT NULL DEFAULT 0.0,
#             date_added   TEXT    DEFAULT (datetime('now','localtime'))
#         )
#     """)

#     # ── Customers / Bills ──────────────────────────────────────────────────────
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS customer_db (
#             customer_id      INTEGER PRIMARY KEY AUTOINCREMENT,
#             customer_name    TEXT    NOT NULL,
#             phone_number     TEXT,
#             address          TEXT,
#             product_id       INTEGER,
#             product_name     TEXT,
#             quantity         INTEGER NOT NULL DEFAULT 1,
#             price_per_item   REAL    NOT NULL DEFAULT 0.0,
#             total_bill       REAL    NOT NULL DEFAULT 0.0,
#             purchase_date    TEXT    DEFAULT (datetime('now','localtime')),
#             bill_number      TEXT,
#             FOREIGN KEY (product_id) REFERENCES product_db(product_id)
#         )
#     """)

#     # ── Bill Header (groups multiple items under one bill) ─────────────────────
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS bills (
#             bill_id       INTEGER PRIMARY KEY AUTOINCREMENT,
#             bill_number   TEXT    NOT NULL UNIQUE,
#             customer_name TEXT    NOT NULL,
#             phone_number  TEXT,
#             address       TEXT,
#             grand_total   REAL    NOT NULL DEFAULT 0.0,
#             bill_date     TEXT    DEFAULT (datetime('now','localtime'))
#         )
#     """)

#     conn.commit()
#     conn.close()
#     print(f"[DB] Database ready → {DB_PATH}")


# def generate_bill_number() -> str:
#     """Generate a unique bill number like BBB-20240101-0001."""
#     conn = get_connection()
#     cursor = conn.cursor()
#     today = datetime.now().strftime("%Y%m%d")
#     cursor.execute(
#         "SELECT COUNT(*) FROM bills WHERE bill_number LIKE ?",
#         (f"BBB-{today}-%",),
#     )
#     count = cursor.fetchone()[0] + 1
#     conn.close()
#     return f"BBB-{today}-{count:04d}"
















"""
database/db_setup.py
Database setup and connection for Binod Book Binding
Optimized with WAL Mode and high-concurrency timeout to completely stop database lock crashes.
"""

import sqlite3
import os
import hashlib
from datetime import datetime

# Database file path
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "binod_book_binding.db")


def get_connection():
    """Return a highly-concurrent connection to the SQLite database."""
    # timeout=30 prevents immediate failure if another module is writing
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row  # Access columns by name
    
    # Enable explicit modern database handling parameters
    conn.execute("PRAGMA foreign_keys = ON")
    # WAL mode enables simultaneous reading and writing without blocking paths
    conn.execute("PRAGMA journal_mode = WAL")
    
    return conn


def hash_password(password: str) -> str:
    """Return SHA-256 hash of password."""
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_database():
    """Create all tables if they don't exist and seed default data."""
    conn = get_connection()
    cursor = conn.cursor()

    # ── Users / Login ──────────────────────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            username  TEXT    NOT NULL UNIQUE,
            password  TEXT    NOT NULL,
            role      TEXT    DEFAULT 'admin',
            created_at TEXT   DEFAULT (datetime('now','localtime'))
        )
    """)

    # Seed default admin if none exists
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", hash_password("admin123"), "admin"),
        )

    # ── Products ───────────────────────────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_db (
            product_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT    NOT NULL,
            category     TEXT    NOT NULL,
            quantity     INTEGER NOT NULL DEFAULT 0,
            price        REAL    NOT NULL DEFAULT 0.0,
            date_added   TEXT    DEFAULT (datetime('now','localtime'))
        )
    """)

    # ── Customers / Bills ──────────────────────────────────────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_db (
            customer_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name    TEXT    NOT NULL,
            phone_number     TEXT,
            address          TEXT,
            product_id       INTEGER,
            product_name     TEXT,
            quantity         INTEGER NOT NULL DEFAULT 1,
            price_per_item   REAL    NOT NULL DEFAULT 0.0,
            total_bill       REAL    NOT NULL DEFAULT 0.0,
            purchase_date    TEXT    DEFAULT (datetime('now','localtime')),
            bill_number      TEXT,
            FOREIGN KEY (product_id) REFERENCES product_db(product_id)
        )
    """)

    # ── Bill Header (groups multiple items under one bill) ─────────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            bill_id       INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_number   TEXT    NOT NULL UNIQUE,
            customer_name TEXT    NOT NULL,
            phone_number  TEXT,
            address       TEXT,
            grand_total   REAL    NOT NULL DEFAULT 0.0,
            bill_date     TEXT    DEFAULT (datetime('now','localtime'))
        )
    """)

    conn.commit()
    conn.close()
    print(f"[DB] Database ready → {DB_PATH}")


def generate_bill_number() -> str:
    """Generate a unique bill number like BBB-20240101-0001."""
    conn = get_connection()
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y%m%d")
    cursor.execute(
        "SELECT COUNT(*) FROM bills WHERE bill_number LIKE ?",
        (f"BBB-{today}-%",),
    )
    count = cursor.fetchone()[0] + 1
    conn.close()
    return f"BBB-{today}-{count:04d}"