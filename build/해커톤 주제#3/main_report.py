from fpdf import FPDF
from io import BytesIO
import pandas as pd


def main_generate_pdf(df, onebool_2022, onebool_2023, cost_2022):
    # 2022년 합계와 2023년 합계를 추출
    total_2022 = df.loc[df['계정명'] == '합계', '2022년'].values[0]
    total_2023 = df.loc[df['계정명'] == '합계', '2023년'].values[0]
    
    # 2023년 합계에서 2022년 합계를 뺀 값을 계산
    difference = total_2023 - total_2022
    
    # 결과 출력 (PDF 생성 등 추가 코드 작성 가능)
    print(f"2023년 합계 - 2022년 합계 = {difference}")
    
    # PDF 생성 (예시 코드)
    pdf = FPDF()
    pdf.add_page()
    
    # PDF에 계산된 값을 추가
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"2023년 합계 - 2022년 합계 = {difference}", ln=True, align='C')
    
    # PDF 파일을 BytesIO 객체에 저장
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    
    # PDF 데이터를 반환
    return pdf_output.getvalue()