from io import BytesIO
from xhtml2pdf import pisa

# Open HTML file
with open('sign_verify_ok.html', 'r') as f:
    html_code = f.read()

# Convert HTML to PDF
pdf_file = BytesIO()
pisa.CreatePDF(html_code, pdf_file)

# Write PDF to file
with open('output.pdf', 'wb') as output_file:
    output_file.write(pdf_file.getvalue())
