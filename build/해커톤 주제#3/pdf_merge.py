from PyPDF2 import PdfMerger
from io import BytesIO
from fpdf import FPDF
# hello
def merge_pdfs(*pdfs):
    output = BytesIO()  # 병합된 PDF를 저장할 BytesIO 객체
    merger = PdfMerger()

    for pdf in pdfs:
        pdf_buffer = BytesIO()
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)
        merger.append(pdf_buffer)
    
    merger.write(output)  # 병합된 PDF를 output에 저장
    output.seek(0)
    merger.close()

    return output  # 병합된 PDF 객체를 반환
