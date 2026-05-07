from app.services.pdf_service import extract_pdf_text

text = extract_pdf_text("uploads/sample.pdf")

print(text)