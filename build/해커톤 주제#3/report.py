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
from datetime import datetime

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.alias_nb_pages()  # 전체 페이지 수를 위한 예약 필드

    def header(self):
        if self.page_no() != 1:  # 첫 페이지(표지) 이후에만 헤더 추가
            self.image('image_1.png', 10, 8, 33)
            self.set_font('Nanum', 'B', 12)
            self.cell(0, 10, '기업 보고서', align='C', ln=True)
            self.ln(3)  # 헤더와 내용 사이 간격
            self.line(10, self.get_y(), 200, self.get_y())  # 상단 로고 아래 선 그리기
            self.ln(5)

    def footer(self):
        if self.page_no() != 1:  # 첫 페이지(표지) 이후에만 푸터 추가
            self.set_y(-15)
            self.set_draw_color(0, 0, 0)  # 검정색 줄
            self.line(10, self.get_y(), 200, self.get_y())  # 페이지 하단에 줄 긋기

            self.set_y(-10)
            self.set_font('Nanum', '', 8)
            page_number = f'Page {self.page_no()} of {{nb}}'
            self.cell(0, 10, page_number, 0, 0, 'R')

def create_pdf_object():
    pdf = PDF()

    # 한글 폰트 추가 (폰트 파일 경로를 실제 경로로 변경해야 합니다)
    pdf.add_font('Nanum', '', 'NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothic-Bold.ttf', uni=True)

    return pdf

def add_cover_page(pdf):
    pdf.add_page()

    # 로고 이미지 중앙에 배치
    logo_path = 'image_1.png'
    logo_width, logo_height = 50, 30  # 로고 크기 조정
    pdf.image(logo_path, x=(pdf.w - logo_width) / 2, y=(pdf.h - logo_height) / 2 - 60, w=logo_width, h=logo_height)

    pdf.set_y(pdf.h / 2 + 10)  # 로고 아래로 위치 설정
    pdf.set_font('Nanum', 'B', 24)
    pdf.cell(0, 20, '기업 보고서', ln=True, align='C')

    pdf.set_font('Nanum', '', 16)
    pdf.cell(0, 10, '보고서 작성일:', ln=True, align='C')
    pdf.cell(0, 10, datetime.now().strftime('%Y-%m-%d'), ln=True, align='C')

    pdf.ln(20)

    pdf.set_font('Nanum', '', 12)
    pdf.multi_cell(0, 10, '이 보고서는 회사의 재무 상태와 주요 원재료 출고량, 고객 인터뷰 등을 포함한 종합 보고서입니다. 회사 내부 자료로만 사용되며 외부 유출을 금합니다.', align='C')

def generate_pdf(dataframe):
    pdf = create_pdf_object()
    add_cover_page(pdf)  # 표지 추가, 한 번만 호출

    pdf.add_page()  # 내용 시작할 페이지 추가

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '재무 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [50, 30, 30, 50]  # 열 너비 설정

    table_width = sum(col_widths)
    start_x = (pdf.w - table_width) / 2  # 테이블을 중앙에 배치하기 위한 시작 x 좌표
    pdf.set_x(start_x)

    pdf.set_font('Nanum', 'B', 10)
    headers = ['계정명', '2022년', '2023년', '전기대비 증감율']
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.set_x(start_x)
        pdf.cell(col_widths[0], 10, str(row['계정명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row['2022년']):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['2023년']):,}", border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{row['전기대비 증감율']:.2f}%", border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf2(dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 내용 시작할 페이지 추가

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '원재료 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [50, 40, 50, 40]  # 열 너비 설정

    table_width = sum(col_widths)
    start_x = (pdf.w - table_width) / 2  # 테이블을 중앙에 배치하기 위한 시작 x 좌표
    pdf.set_x(start_x)

    pdf.set_font('Nanum', 'B', 10)
    headers = ['원재료명 (2022)', '총 출고량 (2022)', '원재료명 (2023)', '총 출고량 (2023)']
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.set_x(start_x)
        pdf.cell(col_widths[0], 10, str(row['원재료명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row.get('2022 총 출고량', 0)):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, str(row['원재료명']), border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{int(row.get('2023 총 출고량', 0)):,}", border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf3(dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 내용 시작할 페이지 추가

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '고객 인터뷰 요약', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정
    col_widths = [60, 120]  # 열 너비 설정

    table_width = sum(col_widths)
    start_x = (pdf.w - table_width) / 2  # 테이블을 중앙에 배치하기 위한 시작 x 좌표
    pdf.set_x(start_x)

    pdf.set_font('Nanum', 'B', 10)
    headers = ['항목', '증감 추이의 원인']
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align='C')
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    for index, row in dataframe.iterrows():
        pdf.set_x(start_x)
        pdf.cell(col_widths[0], 10, str(row['항목']), border=1)
        pdf.multi_cell(col_widths[1], 10, str(row['증감 추이의 원인']), border=1)

    return pdf