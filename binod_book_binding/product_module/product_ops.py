
"""
Professional Product Operations
"""

from database.db_setup import get_connection
from datetime import datetime


# ================= ADD PRODUCT =================
def add_product(name, category, quantity, price):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO product_db
        (
            product_name,
            category,
            quantity,
            price,
            date_added
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            name.strip(),
            category.strip(),
            int(quantity),
            float(price),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()

    pid = cursor.lastrowid

    conn.close()

    return pid


# ================= GET PRODUCTS =================
def get_all_products():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM product_db
        ORDER BY product_id DESC
    """)

    rows = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return rows


# ================= SEARCH =================
def search_products(query):

    conn = get_connection()

    cursor = conn.cursor()

    search = f"%{query}%"

    cursor.execute(
        """
        SELECT *
        FROM product_db
        WHERE product_name LIKE ?
        OR category LIKE ?
        OR CAST(product_id AS TEXT) LIKE ?
        """,
        (
            search,
            search,
            search
        )
    )

    rows = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return rows


# ================= LOW STOCK =================
def get_low_stock_products(threshold=5):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM product_db
        WHERE quantity <= ?
        ORDER BY quantity ASC
        """,
        (threshold,)
    )

    rows = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return rows


# ================= UPDATE =================
def update_product(pid, name, category, quantity, price):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE product_db
        SET
            product_name=?,
            category=?,
            quantity=?,
            price=?
        WHERE product_id=?
        """,
        (
            name,
            category,
            quantity,
            price,
            pid
        )
    )

    conn.commit()

    conn.close()


# ================= DELETE =================
def delete_product(pid):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM product_db WHERE product_id=?",
        (pid,)
    )

    conn.commit()

    conn.close()


# ================= REDUCE STOCK =================
def reduce_stock(product_id, qty_sold):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT quantity FROM product_db WHERE product_id=?",
        (product_id,)
    )

    row = cursor.fetchone()

    if not row:

        conn.close()

        return False

    stock = row[0]

    if stock < qty_sold:

        conn.close()

        return False

    cursor.execute(
        """
        UPDATE product_db
        SET quantity = quantity - ?
        WHERE product_id=?
        """,
        (
            qty_sold,
            product_id
        )
    )

    conn.commit()

    conn.close()

    return True


# ================= GET PRODUCT BY ID =================
def get_product_by_id(product_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM product_db
        WHERE product_id=?
        """,
        (product_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


# ================= GET ALL CATEGORIES =================
def get_all_categories():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT category
        FROM product_db
        ORDER BY category
        """
    )

    rows = [r[0] for r in cursor.fetchall()]

    conn.close()

    return rows


# ================= TOTAL PRODUCTS =================
def get_total_products():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM product_db
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ================= TOTAL STOCK VALUE =================
def get_total_stock_value():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(quantity * price)
        FROM product_db
        """
    )

    value = cursor.fetchone()[0]

    conn.close()

    return value if value else 0