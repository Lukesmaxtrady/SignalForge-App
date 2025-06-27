from fpdf import FPDF

def export_pdf_report(title, table, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.set_font("Arial", size=10)
    for row in table:
        line = " | ".join(str(x) for x in row)
        pdf.cell(0, 10, line, ln=1)
    pdf.output(filename)
    return filename