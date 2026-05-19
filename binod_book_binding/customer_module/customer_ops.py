"""
customer_module/customer_ops.py
Operations for customer purchases, bill storage, and history.
"""

from database.db_setup import get_connection, generate_bill_number
from product_module.product_ops import reduce_stock, get_product_by_id
from datetime import datetime


# ── CREATE BILL ────────────────────────────────────────────────────────────────
def create_bill(customer_name: str, phone: str, address: str, items: list) -> dict:
    """
    Create a complete bill.

    items: list of dicts → {product_id, quantity}

    Returns: bill summary dict with bill_number, items detail, grand_total.
    Raises ValueError if any item is out of stock.
    """
    if not items:
        raise ValueError("No items in bill.")

    # Verify stock for all items first (atomic check)
    enriched = []
    for item in items:
        product = get_product_by_id(item["product_id"])
        if not product:
            raise ValueError(f"Product ID {item['product_id']} not found.")
        if product["quantity"] < item["quantity"]:
            raise ValueError(
                f"Insufficient stock for '{product['product_name']}'. "
                f"Available: {product['quantity']}, Requested: {item['quantity']}"
            )
        enriched.append({
            "product_id":   product["product_id"],
            "product_name": product["product_name"],
            "price":        product["price"],
            "quantity":     item["quantity"],
            "subtotal":     round(product["price"] * item["quantity"], 2),
        })

    # Reduce stock
    for e in enriched:
        reduce_stock(e["product_id"], e["quantity"])

    grand_total = round(sum(e["subtotal"] for e in enriched), 2)
    bill_number = generate_bill_number()
    bill_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    # Insert bill header
    cursor.execute(
        """INSERT INTO bills (bill_number, customer_name, phone_number, address, grand_total, bill_date)
           VALUES (?,?,?,?,?,?)""",
        (bill_number, customer_name, phone, address, grand_total, bill_date),
    )

    # Insert individual line items into customer_db
    for e in enriched:
        cursor.execute(
            """INSERT INTO customer_db
               (customer_name, phone_number, address, product_id, product_name,
                quantity, price_per_item, total_bill, purchase_date, bill_number)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (
                customer_name, phone, address,
                e["product_id"], e["product_name"],
                e["quantity"], e["price"], e["subtotal"],
                bill_date, bill_number,
            ),
        )

    conn.commit()
    conn.close()

    return {
        "bill_number":   bill_number,
        "customer_name": customer_name,
        "phone":         phone,
        "address":       address,
        "items":         enriched,
        "grand_total":   grand_total,
        "bill_date":     bill_date,
    }


# ── READ ───────────────────────────────────────────────────────────────────────
def get_all_bills() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills ORDER BY bill_date DESC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


def get_bill_items(bill_number: str) -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM customer_db WHERE bill_number=?", (bill_number,)
    )
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


def search_bills(query: str) -> list:
    """Search bills by customer name, phone, or bill number."""
    conn = get_connection()
    cursor = conn.cursor()
    like = f"%{query}%"
    cursor.execute(
        """SELECT * FROM bills
           WHERE customer_name LIKE ? OR phone_number LIKE ? OR bill_number LIKE ?
           ORDER BY bill_date DESC""",
        (like, like, like),
    )
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


def get_customer_history(phone: str) -> list:
    """All bills for a customer by phone number."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM bills WHERE phone_number=? ORDER BY bill_date DESC",
        (phone,),
    )
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows


# ── STATS ──────────────────────────────────────────────────────────────────────
def get_total_sales() -> float:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(grand_total) FROM bills")
    val = cursor.fetchone()[0] or 0.0
    conn.close()
    return round(val, 2)


def get_total_customers() -> int:
    """Unique customers (by phone)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT phone_number) FROM bills")
    val = cursor.fetchone()[0]
    conn.close()
    return val


def get_daily_sales(date_str: str = None) -> float:
    """Sales total for a given date (YYYY-MM-DD). Defaults to today."""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(grand_total) FROM bills WHERE bill_date LIKE ?",
        (f"{date_str}%",),
    )
    val = cursor.fetchone()[0] or 0.0
    conn.close()
    return round(val, 2)


def get_recent_bills(limit: int = 10) -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM bills ORDER BY bill_date DESC LIMIT ?", (limit,)
    )
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows
