import PyPDF2

def pdf_to_string(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

pdf_path = 'talk_n_chat_with_pdf\Julius-Caesar-PDF.pdf'
pdf_text = pdf_to_string(pdf_path)
print(pdf_text)