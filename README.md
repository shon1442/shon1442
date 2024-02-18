import PyPDF2

def count_points(pdf_file):
    occurrences = 0
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()
            occurrences += text.lower().count('.')
    return occurrences

pdf_file = 'example.pdf'  # כאן נכתוב את נתיב הקובץ ה-PDF
points_count = count_points(pdf_file)
print(f"The PDF file contains {points_count} points.")
