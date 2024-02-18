import PyPDF2
import pandas as pd
from collections import Counter

def extract_points(pdf_file):
    points = []
    drawings_count = 0
    
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()
            
            dot_count_page = text.count('.')
            drawing_count_page = text.count('ציור')
            
            for i in range(dot_count_page):
                points.append('•')
            
            drawings_count += drawing_count_page
    
    return points, drawings_count

def create_excel(points, drawings_count, output_file='points_summary.xlsx'):
    df = pd.DataFrame({'Point': points})
    df['Count'] = 1
    summary_df = df.groupby('Point').sum().reset_index()
    summary_df = summary_df.rename(columns={'Point': 'Symbol', 'Count': 'Occurrences'})
    summary_df.loc[len(summary_df)] = ['Drawings', drawings_count]
    
    summary_df.to_excel(output_file, index=False)
    print(f"Excel file '{output_file}' created successfully.")

# כאן נכתוב את נתיב הקובץ ה-PDF
pdf_file = 'example.pdf'
points, drawings_count = extract_points(pdf_file)
create_excel(points, drawings_count)
