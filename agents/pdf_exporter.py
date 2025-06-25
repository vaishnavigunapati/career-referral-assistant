# agents/pdf_exporter.py

from fpdf import FPDF
import os

def save_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # ✅ Convert non-latin characters to a safe placeholder
    safe_text = text.encode("latin-1", "replace").decode("latin-1")

    # ✅ Split into lines so long paragraphs don’t break layout
    lines = safe_text.split("\n")
    for line in lines:
        pdf.multi_cell(0, 10, line)

    # ✅ Save PDF to 'data/' directory
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", f"{filename}.pdf")
    pdf.output(path)
    return path
