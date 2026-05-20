
# billing_module/bill_printer.py
# ENTERPRISE INVOICE GENERATOR
# Clean, Modern Layout with Automatic Text Wrapping & Refined Visuals

import os
from datetime import datetime

# Create reports directory
REPORTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "reports"
)
os.makedirs(REPORTS_DIR, exist_ok=True)


def check_reportlab_available():
    try:
        __import__('reportlab')
        return True
    except ImportError:
        return False


REPORTLAB_AVAILABLE = check_reportlab_available()


def generate_pdf_bill(bill_data: dict) -> str:
    safe_bn = str(bill_data["bill_number"]).replace("/", "-").replace("\\", "-")
    
    if REPORTLAB_AVAILABLE:
        return generate_pdf_with_reportlab(bill_data, safe_bn)
    return generate_text_receipt(bill_data, safe_bn)


def generate_pdf_with_reportlab(bill_data: dict, safe_bn: str) -> str:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

    filepath = os.path.join(REPORTS_DIR, f"{safe_bn}.pdf")

    # Page settings: 15mm margins maximize printable area cleanly
    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = getSampleStyleSheet()

    # =====================================================
    # REFINED COLOR PALETTE (Cool Tech / Corporate)
    # =====================================================
    PRIMARY = HexColor("#1E293B")     # Slate 800 (Deep Navy/Slate)
    ACCENT = HexColor("#0284C7")      # Sky 600 (Professional Blue Accent)
    TEXT_DARK = HexColor("#0F172A")   # Slate 900 (High contrast text)
    TEXT_MUTED = HexColor("#64748B")  # Slate 500 (Subtle descriptive text)
    BG_LIGHT = HexColor("#F8FAFC")    # Slate 50 (Alternating row color)
    BORDER_COLOR = HexColor("#E2E8F0")# Slate 200 (Clean, light gridlines)

    # =====================================================
    # TYPOGRAPHY & STYLES
    # =====================================================
    company_style = ParagraphStyle(
        "CompName", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=PRIMARY
    )
    tagline_style = ParagraphStyle(
        "Tagline", parent=styles["Normal"],
        fontName="Helvetica-Oblique", fontSize=9, leading=13, textColor=ACCENT
    )
    meta_style = ParagraphStyle(
        "MetaText", parent=styles["Normal"],
        fontName="Helvetica", fontSize=9, leading=14, textColor=TEXT_MUTED
    )
    invoice_title_style = ParagraphStyle(
        "InvTitle", parent=styles["Normal"],
        fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=ACCENT, alignment=TA_RIGHT
    )
    
    # Table Content Styles (Crucial for text wrapping)
    th_left = ParagraphStyle("THL", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=white, alignment=TA_LEFT)
    th_center = ParagraphStyle("THC", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=white, alignment=TA_CENTER)
    th_right = ParagraphStyle("THR", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=white, alignment=TA_RIGHT)
    
    td_left = ParagraphStyle("TDL", fontName="Helvetica", fontSize=9, leading=13, textColor=TEXT_DARK, alignment=TA_LEFT)
    td_center = ParagraphStyle("TDC", fontName="Helvetica", fontSize=9, leading=13, textColor=TEXT_DARK, alignment=TA_CENTER)
    td_right = ParagraphStyle("TDR", fontName="Helvetica", fontSize=9, leading=13, textColor=TEXT_DARK, alignment=TA_RIGHT)
    
    total_label_style = ParagraphStyle("TTL", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=white, alignment=TA_RIGHT)
    total_val_style = ParagraphStyle("TTV", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=white, alignment=TA_RIGHT)

    story = []

    # =====================================================
    # BRAND HEADER (Two-Column modern layout)
    # =====================================================
    header_left = [
        Paragraph("BINOD BOOK BINDING", company_style),
        Paragraph("Premium Stationery & Book Binding Shop", tagline_style),
        Spacer(1, 2 * mm),
        Paragraph("<b>✉</b> info@binodbooks.com | <b>✆</b> +91 XXXXXXXXXX", meta_style),
        Paragraph("📍 Your City, State, India - ZIP", meta_style)
    ]
    
    header_right = [
        Paragraph("INVOICE", invoice_title_style),
        Spacer(1, 4 * mm),
        Paragraph(f"<b>Invoice No:</b> {bill_data['bill_number']}", ParagraphStyle("R1", alignment=TA_RIGHT, fontSize=10, leading=14, textColor=TEXT_DARK)),
        Paragraph(f"<b>Date:</b> {bill_data.get('bill_date', datetime.now().strftime('%d-%m-%Y'))}", ParagraphStyle("R2", alignment=TA_RIGHT, fontSize=9, leading=13, textColor=TEXT_MUTED))
    ]

    header_table = Table(
        [[header_left, header_right]], 
        colWidths=[110 * mm, 70 * mm]
    )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    
    # Modern decorative colored accent bar
    story.append(Spacer(1, 4 * mm))
    bar_table = Table([[""]], colWidths=[180 * mm], rowHeights=[1 * mm])
    bar_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ACCENT)]))
    story.append(bar_table)
    story.append(Spacer(1, 6 * mm))

    # =====================================================
    # CLIENT BILL TO SECTION
    # =====================================================
    client_info = [
        Paragraph("<b>▼ BILL TO</b>", ParagraphStyle("BillTo", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=ACCENT)),
        Spacer(1, 1 * mm),
        Paragraph(f"<b>Customer:</b> {bill_data['customer_name']}", td_left),
        Paragraph(f"<b>Phone:</b> {bill_data.get('phone', '-')}", td_left),
        Paragraph(f"<b>Address:</b> {bill_data.get('address', '-')}", td_left)
    ]
    
    client_table = Table([[client_info]], colWidths=[180 * mm])
    client_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(client_table)
    story.append(Spacer(1, 6 * mm))

    # =====================================================
    # ITEMIZATION TABLE
    # =====================================================
    # Table columns layout width sum up exactly to 180mm template boundary
    col_widths = [12 * mm, 83 * mm, 20 * mm, 30 * mm, 35 * mm]
    
    headers = [
        Paragraph("#", th_center),
        Paragraph("Description / Product", th_left),
        Paragraph("Qty", th_center),
        Paragraph("Unit Price", th_right),
        Paragraph("Total Amount", th_right)
    ]
    
    table_data = [headers]

    for i, item in enumerate(bill_data["items"], 1):
        table_data.append([
            Paragraph(str(i), td_center),
            Paragraph(item["product_name"], td_left), # Will auto-wrap if long!
            Paragraph(str(item["quantity"]), td_center),
            Paragraph(f"{item['price']:.2f}", td_right),
            Paragraph(f"{item['subtotal']:.2f}", td_right)
        ])

    # Grand Total row matching layout architecture
    table_data.append([
        "", "", "", 
        Paragraph("GRAND TOTAL", total_label_style),
        Paragraph(f"{bill_data['grand_total']:.2f}", total_val_style)
    ])

    items_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    
    # Modern layout rules definitions
    t_style = TableStyle([
        # Header configuration
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        
        # Grid boundaries and styling configurations
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, BORDER_COLOR),
        
        # Grand total final line configuration 
        ("BACKGROUND", (3, -1), (4, -1), ACCENT),
        ("TOPPADDING", (0, -1), (-1, -1), 8),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
    ])
    
    # Optional dynamic clean background striping for items row
    for row in range(1, len(table_data) - 1):
        if row % 2 == 0:
            t_style.add("BACKGROUND", (0, row), (-1, row), BG_LIGHT)
            
    items_table.setStyle(t_style)
    story.append(items_table)
    story.append(Spacer(1, 12 * mm))

    # =====================================================
    # TERMS & SYSTEM FOOTER
    # =====================================================
    footer_text = ParagraphStyle("Ftr", fontName="Helvetica", fontSize=8, leading=12, textColor=TEXT_MUTED, alignment=TA_CENTER)
    thanks_text = ParagraphStyle("Thx", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=PRIMARY, alignment=TA_CENTER)
    
    story.append(Paragraph("Thank You For Your Business!", thanks_text))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Terms: Returns are accepted within 7 days with original receipt tags attached.", footer_text))
    story.append(Paragraph("This is a digitally compiled system invoice and requires no physical signatures.", footer_text))

    doc.build(story)
    return filepath


def generate_text_receipt(bill_data: dict, safe_bn: str) -> str:
    filepath = os.path.join(REPORTS_DIR, f"{safe_bn}.txt")
    width = 58
    sep = "=" * width
    thin = "-" * width
    bill_date = bill_data.get("bill_date", datetime.now().strftime("%d-%m-%Y %H:%M"))

    lines = [
        sep,
        "BINOD BOOK BINDING".center(width),
        "Premium Stationery & Book Binding Shop".center(width),
        sep,
        f"Bill No    : {bill_data['bill_number']}",
        f"Date       : {bill_date}",
        thin,
        f"Customer   : {bill_data['customer_name']}",
    ]

    if bill_data.get("phone"):
        lines.append(f"Phone      : {bill_data['phone']}")
    if bill_data.get("address"):
        lines.append(f"Address    : {bill_data['address']}")

    lines.extend([
        thin,
        f"{'#':<3} {'Product':<24} {'Qty':>4} {'Price':>9} {'Total':>10}",
        thin
    ])

    for i, item in enumerate(bill_data["items"], 1):
        product_name = item["product_name"][:24]
        lines.append(
            f"{i:<3} {product_name:<24} {item['quantity']:>4} {item['price']:>9.2f} {item['subtotal']:>10.2f}"
        )

    lines.extend([
        thin,
        f"{'GRAND TOTAL':>46} {bill_data['grand_total']:>10.2f}",
        sep,
        "THANK YOU FOR YOUR PURCHASE".center(width),
        "VISIT AGAIN".center(width),
        sep
    ])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filepath


def open_file(path: str):
    import subprocess
    import platform

    try:
        if not os.path.exists(path):
            return

        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.call(["open", path])
        else:
            subprocess.call(["xdg-open", path])
    except Exception as e:
        print(f"Could not open file: {e}")


def get_bill_preview_text(bill_data: dict) -> str:
    width = 58
    sep = "=" * width
    thin = "-" * width
    bill_date = bill_data.get("bill_date", datetime.now().strftime("%d-%m-%Y %H:%M"))

    lines = [
        sep,
        "BINOD BOOK BINDING".center(width),
        "Premium Stationery & Book Binding Shop".center(width),
        sep,
        f"Bill No    : {bill_data['bill_number']}",
        f"Date       : {bill_date}",
        f"Customer   : {bill_data['customer_name']}",
        thin,
        f"{'#':<3} {'Product':<24} {'Qty':>4} {'Price':>9} {'Total':>10}",
        thin
    ]

    for i, item in enumerate(bill_data["items"], 1):
        product_name = item["product_name"][:24]
        lines.append(
            f"{i:<3} {product_name:<24} {item['quantity']:>4} {item['price']:>9.2f} {item['subtotal']:>10.2f}"
        )

    lines.extend([
        thin,
        f"{'GRAND TOTAL':>46} {bill_data['grand_total']:>10.2f}",
        sep,
        "THANK YOU FOR YOUR PURCHASE".center(width),
        sep
    ])

    return "\n".join(lines)