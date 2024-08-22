from fpdf import FPDF
import pandas as pd

def generate_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    # 유니코드 폰트 추가
    pdf.add_font('Nanum', '', "C:/Users/jeong/OneDrive/바탕 화면/NanumGothic/NanumGothic-Regular.ttf", uni=True)
    pdf.set_font('Nanum', size=10)
    
    # 테이블 헤더 작성
    col_widths = [50, 30, 30, 50]  # 열 너비 설정
    pdf.cell(col_widths[0], 10, '계정명', border=1, align='C')
    pdf.cell(col_widths[1], 10, '2022년', border=1, align='C')
    pdf.cell(col_widths[2], 10, '2023년', border=1, align='C')
    pdf.cell(col_widths[3], 10, '전기대비 증감율', border=1, align='C')
    pdf.ln()

    # 데이터프레임의 각 행을 PDF에 추가
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['계정명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row['2022년']):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['2023년']):,}", border=1, align='R')
        pdf.cell(col_widths[3], 10, str(row['전기대비 증감율']), border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf2(dataframe):
    pdf = FPDF()
    pdf.add_page()
    # 유니코드 폰트 추가
    pdf.add_font('Nanum', '', "C:/Users/jeong/OneDrive/바탕 화면/NanumGothic/NanumGothic-Regular.ttf", uni=True)
    pdf.set_font('Nanum', size=10)
    
    # 테이블 헤더 작성
    col_widths = [50, 40, 50, 40]  # 열 너비 설정
    pdf.cell(col_widths[0], 10, '원재료명', border=1, align='C')
    pdf.cell(col_widths[1], 10, '2022 총 출고량', border=1, align='C')
    pdf.cell(col_widths[2], 10, '원재료명', border=1, align='C')
    pdf.cell(col_widths[3], 10, '2023 총 출고량', border=1, align='C')
    pdf.ln()

    # 데이터프레임의 각 행을 PDF에 추가
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['원재료명']), border=1)
        pdf.cell(col_widths[1], 10, str(row.get('2022 총 출고량', '')), border=1, align='R')
        pdf.cell(col_widths[2], 10, str(row['원재료명']), border=1, align = "R")
        pdf.cell(col_widths[3], 10, str(row.get('2023 총 출고량', '')), border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf3(dataframe):
    pdf = FPDF()
    pdf.add_page()
    
    # 유니코드 폰트 추가
    pdf.add_font('Nanum', '', "C:/Users/jeong/OneDrive/바탕 화면/NanumGothic/NanumGothic-Regular.ttf", uni=True)
    pdf.set_font('Nanum', size=10)
    
    # 테이블 헤더 작성
    col_widths = [60, 120]  # 열 너비 설정 (필요에 따라 조정)
    pdf.cell(col_widths[0], 10, '항목', border=1, align='C')
    pdf.cell(col_widths[1], 10, '증감 추이의 원인', border=1, align='C')
    pdf.ln()

    # 데이터프레임의 각 행을 PDF에 추가
    for index, row in dataframe.iterrows():
        pdf.cell(col_widths[0], 10, str(row['항목']), border=1)
        pdf.cell(col_widths[1], 10, str(row['증감 추이의 원인']), border=1)
        pdf.ln()

    return pdf