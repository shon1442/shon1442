import tkinter as tk
from tkinter import filedialog
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

def choose_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        points_count = count_points(file_path)
        result_label.config(text=f"כמות הנקודות בקובץ ה-PDF היא: {points_count}", wraplength=300)

root = tk.Tk()
root.title("ספירת נקודות בקובץ PDF")

choose_file_button = tk.Button(root, text="בחר קובץ PDF", command=choose_pdf_file)
choose_file_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
result_label.pack()

root.mainloop()def count_dots(text):
    dot_count = 0
    for char in text:
        if char == '.':
            dot_count += 1
    return dot_count

text = "הנה טקסט עם נקודה אחת. וכאן נקודה נוספת."
dots = count_dots(text)
print(f"The text contains {dots} dots.")
