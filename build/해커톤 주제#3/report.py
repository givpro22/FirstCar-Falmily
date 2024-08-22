# from fpdf import FPDF
# import pandas as pd

# def generate_pdf(dataframe):
#     pdf = FPDF()
#     pdf.add_page()
#     # 유니코드 폰트 추가
#     pdf.add_font('Nanum', '', "C:NanumGothic-Regular.ttf", uni=True)
#     pdf.set_font('Nanum', size=10)
    
#     # 테이블 헤더 작성
#     col_widths = [50, 30, 30, 50]  # 열 너비 설정
#     pdf.cell(col_widths[0], 10, '계정명', border=1, align='C')
#     pdf.cell(col_widths[1], 10, '2022년', border=1, align='C')
#     pdf.cell(col_widths[2], 10, '2023년', border=1, align='C')
#     pdf.cell(col_widths[3], 10, '전기대비 증감율', border=1, align='C')
#     pdf.ln()

#     # 데이터프레임의 각 행을 PDF에 추가
#     for index, row in dataframe.iterrows():
#         pdf.cell(col_widths[0], 10, str(row['계정명']), border=1)
#         pdf.cell(col_widths[1], 10, f"{int(row['2022년']):,}", border=1, align='R')
#         pdf.cell(col_widths[2], 10, f"{int(row['2023년']):,}", border=1, align='R')
#         pdf.cell(col_widths[3], 10, str(row['전기대비 증감율']), border=1, align='R')
#         pdf.ln()

#     return pdf

# def generate_pdf2(dataframe):
#     pdf = FPDF()
#     pdf.add_page()
#     # 유니코드 폰트 추가
#     pdf.add_font('Nanum', '', "C:NanumGothic-Regular.ttf", uni=True)
#     pdf.set_font('Nanum', size=10)
    
#     # 테이블 헤더 작성
#     col_widths = [50, 40, 50, 40]  # 열 너비 설정
#     pdf.cell(col_widths[0], 10, '원재료명', border=1, align='C')
#     pdf.cell(col_widths[1], 10, '2022 총 출고량', border=1, align='C')
#     pdf.cell(col_widths[2], 10, '원재료명', border=1, align='C')
#     pdf.cell(col_widths[3], 10, '2023 총 출고량', border=1, align='C')
#     pdf.ln()

#     # 데이터프레임의 각 행을 PDF에 추가
#     for index, row in dataframe.iterrows():
#         pdf.cell(col_widths[0], 10, str(row['원재료명']), border=1)
#         pdf.cell(col_widths[1], 10, str(row.get('2022 총 출고량', '')), border=1, align='R')
#         pdf.cell(col_widths[2], 10, str(row['원재료명']), border=1, align = "R")
#         pdf.cell(col_widths[3], 10, str(row.get('2023 총 출고량', '')), border=1, align='R')
#         pdf.ln()

#     return pdf

# def generate_pdf3(dataframe):
#     pdf = FPDF()
#     pdf.add_page()
    
#     # 유니코드 폰트 추가
#     pdf.add_font('Nanum', '', "C:/Users/jeong/OneDrive/바탕 화면/NanumGothic/NanumGothic-Regular.ttf", uni=True)
#     pdf.set_font('Nanum', size=10)
    
#     # 테이블 헤더 작성
#     col_widths = [60, 120]  # 열 너비 설정 (필요에 따라 조정)
#     pdf.cell(col_widths[0], 10, '항목', border=1, align='C')
#     pdf.cell(col_widths[1], 10, '증감 추이의 원인', border=1, align='C')
#     pdf.ln()

#     # 데이터프레임의 각 행을 PDF에 추가
#     for index, row in dataframe.iterrows():
#         pdf.cell(col_widths[0], 10, str(row['항목']), border=1)
#         pdf.cell(col_widths[1], 10, str(row['증감 추이의 원인']), border=1)
#         pdf.ln()

#     return pdf

from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # 로고 추가 (로고 파일 경로에 맞게 수정)
        self.image('image_1.png', 10, 8, 33)
        self.set_font('Nanum', 'B', 12)
        self.cell(0, 10, '기업 보고서', align='C', ln=True, border=False)
        self.ln(10)
    
    def footer(self):
        # 페이지 하단에 페이지 번호 추가
        self.set_y(-15)
        self.set_font('Nanum', '', 8)
        self.cell(0, 10, f'페이지 {self.page_no()}', 0, 0, 'C')

def create_pdf_object():
    pdf = PDF()
    
    # 한글 폰트 추가 및 설정
    # 경로는 실제 폰트 파일이 있는 경로로 수정해야 합니다.
    pdf.add_font('Nanum', '', 'NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothic-Bold.ttf', uni=True)
    
    pdf.add_page()
    pdf.set_font('Nanum', size=10)
    
    return pdf

def generate_pdf(dataframe):
    pdf = create_pdf_object()

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '재무 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [50, 30, 30, 50]  # 열 너비 설정
    pdf.set_font('Nanum', 'B', 10)
    pdf.cell(col_widths[0], 10, '계정명', border=1, align='C')
    pdf.cell(col_widths[1], 10, '2022년', border=1, align='C')
    pdf.cell(col_widths[2], 10, '2023년', border=1, align='C')
    pdf.cell(col_widths[3], 10, '전기대비 증감율', border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['계정명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row['2022년']):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['2023년']):,}", border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{row['전기대비 증감율']:.2f}%", border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf2(dataframe):
    pdf = create_pdf_object()

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '원재료 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [50, 40, 50, 40]  # 열 너비 설정
    pdf.set_font('Nanum', 'B', 10)
    pdf.cell(col_widths[0], 10, '원재료명 (2022)', border=1, align='C')
    pdf.cell(col_widths[1], 10, '총 출고량 (2022)', border=1, align='C')
    pdf.cell(col_widths[2], 10, '원재료명 (2023)', border=1, align='C')
    pdf.cell(col_widths[3], 10, '총 출고량 (2023)', border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['원재료명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row.get('2022 총 출고량', 0)):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, str(row['원재료명']), border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{int(row.get('2023 총 출고량', 0)):,}", border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf3(dataframe):
    pdf = create_pdf_object()

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '고객 인터뷰 요약', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [60, 120]  # 열 너비 설정
    pdf.set_font('Nanum', 'B', 10)
    pdf.cell(col_widths[0], 10, '항목', border=1, align='C')
    pdf.cell(col_widths[1], 10, '증감 추이의 원인', border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['항목']), border=1)
        pdf.cell(col_widths[1], 10, str(row['증감 추이의 원인']), border=1)
        pdf.ln()

    return pdf
