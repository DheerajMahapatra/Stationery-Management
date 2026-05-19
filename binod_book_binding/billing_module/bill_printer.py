"""
billing_module/bill_printer.py
Generate and print/export bills as PDF using reportlab or plain text fallback.
"""

import os
import sys
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)


def _try_reportlab():
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
        return True
    except ImportError:
        return False


HAS_REPORTLAB = _try_reportlab()


def generate_pdf_bill(bill_data: dict) -> str:
    """
    Generate a PDF bill and return its file path.
    Falls back to a plain-text .txt receipt if reportlab is unavailable.

    bill_data keys: bill_number, customer_name, phone, address,
                    items (list of dicts), grand_total, bill_date
    """
    safe_bn = bill_data["bill_number"].replace("/", "-")
    if HAS_REPORTLAB:
        return _generate_pdf(bill_data, safe_bn)
    else:
        return _generate_txt(bill_data, safe_bn)


# ── PDF generation ─────────────────────────────────────────────────────────────
def _generate_pdf(bill_data: dict, safe_bn: str) -> str:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT

    filepath = os.path.join(REPORTS_DIR, f"{safe_bn}.pdf")
    doc = SimpleDocTemplate(filepath, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=15*mm, bottomMargin=15*mm)
    styles = getSampleStyleSheet()

    NAVY  = colors.HexColor("#1a237e")
    GOLD  = colors.HexColor("#f9a825")
    LIGHT = colors.HexColor("#e8eaf6")

    title_style = ParagraphStyle("title", parent=styles["Title"],
                                 fontSize=22, textColor=NAVY,
                                 spaceAfter=2, alignment=1)
    sub_style   = ParagraphStyle("sub", parent=styles["Normal"],
                                 fontSize=9, textColor=colors.grey,
                                 alignment=1, spaceAfter=1)
    label_style = ParagraphStyle("label", parent=styles["Normal"],
                                 fontSize=10, textColor=NAVY, spaceBefore=4)
    value_style = ParagraphStyle("value", parent=styles["Normal"],
                                 fontSize=10, textColor=colors.black)

    story = []

    # Header
    story.append(Paragraph("Binod Book Binding", title_style))
    story.append(Paragraph("Stationery & Book Binding Shop", sub_style))
    story.append(Paragraph("📞 Contact: Your Phone  |  📍 Your Address", sub_style))
    story.append(Spacer(1, 8*mm))

    # Bill info table
    info = [
        ["Bill No:", bill_data["bill_number"],  "Date:", bill_data["bill_date"]],
        ["Customer:", bill_data["customer_name"], "Phone:", bill_data.get("phone", "")],
        ["Address:", bill_data.get("address", ""), "", ""],
    ]
    info_table = Table(info, colWidths=[30*mm, 70*mm, 20*mm, 50*mm])
    info_table.setStyle(TableStyle([
        ("FONTNAME",  (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",  (0,0), (-1,-1), 9),
        ("FONTNAME",  (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",  (2,0), (2,-1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0,0), (0,-1), NAVY),
        ("TEXTCOLOR", (2,0), (2,-1), NAVY),
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 6*mm))

    # Items table
    headers = ["#", "Product", "Qty", "Price/Unit (₹)", "Subtotal (₹)"]
    data = [headers]
    for i, item in enumerate(bill_data["items"], 1):
        data.append([
            str(i),
            item["product_name"],
            str(item["quantity"]),
            f"₹ {item['price']:.2f}",
            f"₹ {item['subtotal']:.2f}",
        ])
    # Grand total row
    data.append(["", "", "", "GRAND TOTAL", f"₹ {bill_data['grand_total']:.2f}"])

    col_w = [10*mm, 70*mm, 15*mm, 35*mm, 35*mm]
    items_table = Table(data, colWidths=col_w, repeatRows=1)
    items_table.setStyle(TableStyle([
        # Header row
        ("BACKGROUND",   (0,0), (-1,0), NAVY),
        ("TEXTCOLOR",    (0,0), (-1,0), colors.white),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,0), 10),
        ("ALIGN",        (0,0), (-1,0), "CENTER"),
        # Data rows
        ("FONTNAME",     (0,1), (-1,-2), "Helvetica"),
        ("FONTSIZE",     (0,1), (-1,-2), 9),
        ("ROWBACKGROUNDS",(0,1), (-1,-2), [colors.white, LIGHT]),
        ("ALIGN",        (2,1), (-1,-2), "RIGHT"),
        # Total row
        ("FONTNAME",     (0,-1), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE",     (0,-1), (-1,-1), 11),
        ("BACKGROUND",   (0,-1), (-1,-1), GOLD),
        ("TEXTCOLOR",    (0,-1), (-1,-1), NAVY),
        ("ALIGN",        (3,-1), (4,-1), "RIGHT"),
        # Grid
        ("GRID",         (0,0), (-1,-1), 0.5, colors.grey),
        ("LINEBELOW",    (0,0), (-1,0), 2, NAVY),
        ("LINEABOVE",    (0,-1), (-1,-1), 1.5, NAVY),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 4),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 8*mm))

    # Footer
    footer = ParagraphStyle("footer", parent=styles["Normal"],
                            fontSize=8, textColor=colors.grey,
                            alignment=1)
    story.append(Paragraph("Thank you for your purchase! — Binod Book Binding", footer))
    story.append(Paragraph("This is a computer-generated bill.", footer))

    doc.build(story)
    return filepath


# ── TXT fallback ───────────────────────────────────────────────────────────────
def _generate_txt(bill_data: dict, safe_bn: str) -> str:
    filepath = os.path.join(REPORTS_DIR, f"{safe_bn}.txt")
    width = 52
    sep = "=" * width
    thin = "-" * width

    lines = [
        sep,
        "        BINOD BOOK BINDING".center(width),
        "    Stationery & Book Binding Shop".center(width),
        sep,
        f"  Bill No : {bill_data['bill_number']}",
        f"  Date    : {bill_data['bill_date']}",
        thin,
        f"  Customer: {bill_data['customer_name']}",
        f"  Phone   : {bill_data.get('phone', '')}",
        f"  Address : {bill_data.get('address', '')}",
        thin,
        f"  {'#':<3} {'Product':<22} {'Qty':>4} {'Price':>7} {'Total':>8}",
        thin,
    ]
    for i, item in enumerate(bill_data["items"], 1):
        lines.append(
            f"  {i:<3} {item['product_name'][:22]:<22} {item['quantity']:>4}"
            f" {item['price']:>7.2f} {item['subtotal']:>8.2f}"
        )
    lines += [
        thin,
        f"  {'GRAND TOTAL':>40} {bill_data['grand_total']:>8.2f}",
        sep,
        "  Thank you for your purchase!".center(width),
        "  ** Computer Generated Bill **".center(width),
        sep,
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return filepath


def open_file(path: str):
    """Open the generated file with the system default application."""
    import subprocess, platform
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.call(["open", path])
        else:
            subprocess.call(["xdg-open", path])
    except Exception as e:
        print(f"Could not open file: {e}")
