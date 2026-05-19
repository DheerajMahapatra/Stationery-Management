# Binod Book Binding — Management Software
## Requirements

Python 3.10 or newer is required. Tkinter ships with Python by default.

### Install optional PDF export support:
```
pip install reportlab
```

Without reportlab, bills are exported as nicely formatted `.txt` files.

---

## How to Run

```
python main.py
```

Default login:
- **Username:** `admin`
- **Password:** `admin123`

---

## Features

| Module | Features |
|---|---|
| Dashboard | Live stats, recent bills, low-stock alerts |
| Products | Add / Edit / Delete products, search, low-stock filter |
| Billing (POS) | Cart-based billing, automatic stock deduction, bill popup |
| Bills History | View all bills, search, export PDF |
| Customers | Customer purchase history, search |
| Settings | Dark/Light theme, change password, database backup |

---

## Folder Structure

```
binod_book_binding/
├── main.py                     ← Entry point (run this)
├── main_app.py                 ← Main window + sidebar
├── login_window.py             ← Login screen
├── database/
│   ├── db_setup.py             ← SQLite init, connection
│   └── binod_book_binding.db   ← Auto-created on first run
├── product_module/
│   ├── product_ops.py          ← CRUD for products
│   ├── products_page.py        ← Products UI
│   └── dashboard_page.py       ← Dashboard UI
├── customer_module/
│   ├── customer_ops.py         ← Bill creation, customer queries
│   └── customers_page.py       ← Customers UI
├── billing_module/
│   ├── billing_page.py         ← POS / New bill UI
│   ├── bills_history_page.py   ← Bills history UI
│   └── bill_printer.py         ← PDF / TXT bill generation
├── assets/
│   ├── theme.py                ← Colors, fonts, nav config
│   ├── widgets.py              ← Reusable Tkinter widgets
│   └── settings_page.py        ← Settings UI
└── reports/                    ← Generated bills saved here
```

---

## Notes

- Fully offline — no internet required.
- Database is auto-created at `database/binod_book_binding.db`.
- Bills are saved to the `reports/` folder.
- Use Settings → Backup Database to make a copy of your data.
