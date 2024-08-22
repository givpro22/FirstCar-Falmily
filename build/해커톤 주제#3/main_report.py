from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.alias_nb_pages()

    def header(self):
        # 페이지 헤더 설정
        self.image('image_1.png', 10, 8, 33)  # 로고 이미지 경로로 변경 필요
        self.set_font('Nanum', 'B', 16)
        self.set_text_color(0, 149, 219)  # 이미지에서 파란색으로 설정
        self.cell(0, 10, '기업 보고서', align='C', ln=True)
        self.ln(5)
        self.set_draw_color(0, 0, 0)  # 검정색 줄
        self.line(10, self.get_y(), 200, self.get_y())  # 상단 로고 아래 선 그리기
        self.ln(10)

    def footer(self):
        # 페이지 푸터 설정
        self.set_y(-15)
        self.set_draw_color(0, 0, 0)  # 검정색 줄
        self.line(10, self.get_y(), 200, self.get_y())  # 페이지 하단에 줄 긋기

        self.set_y(-10)
        self.set_font('Nanum', '', 8)
        self.set_text_color(0, 0, 0)  # 검정색 텍스트
        page_number = f'Page {self.page_no()}'
        self.cell(0, 10, page_number, 0, 0, 'R')

def create_pdf_object():
    pdf = PDF()

    # 한글 폰트 추가 (폰트 파일 경로를 실제 경로로 변경해야 합니다)
    pdf.add_font('Nanum', '', 'NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothic-Bold.ttf', uni=True)

    return pdf

def main_generate_pdf(*dataframe):
    pdf = create_pdf_object()
    pdf.add_page()

    # 보고서 제목
    pdf.set_font('Nanum', 'B', 18)
    pdf.set_text_color(178, 34, 34)  # 다크 레드 색상
    pdf.cell(0, 10, '2023년 원가 분석 결과', ln=True, align='C')
    pdf.ln(10)

    # 제조경비 비교 섹션
    pdf.set_font('Nanum', 'B', 14)
    pdf.set_text_color(0, 0, 0)  # 검정색
    pdf.cell(0, 10, '제조경비 비교 (2022년 vs 2023년)', ln=True, align='L')
    pdf.ln(8)

    total_2022 = dataframe[0].loc[dataframe[0]['계정명'] == '합계', '2022년'].values[0]
    total_2023 = dataframe[0].loc[dataframe[0]['계정명'] == '합계', '2023년'].values[0]
    difference = total_2022 - total_2023

    pdf.set_font('Nanum', '', 12)
    pdf.set_text_color(0, 0, 0)  # 검정색 텍스트
    pdf.cell(0, 10, f"2023 - 2022 제조경비(노무비 + 경비) 차: {difference:,} 원", ln=True, align='C')

    if difference > 0:
        pdf.cell(0, 10, f"2023년 제조경비(노무비 + 경비) 합계는 2022년 대비 {difference:,} 원 증가했습니다.", ln=True, align='C')
    else:
        pdf.cell(0, 10, f"2023년 제조경비(노무비 + 경비) 합계는 2022년 대비 {abs(difference):,} 원 감소했습니다.", ln=True, align='C')

    pdf.ln(15)

    # 제품 원가율 Best5 섹션
    pdf.set_font('Nanum', 'B', 14)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트
    pdf.cell(0, 10, '제품의 원가율 Best 5', align='C', fill=True, ln=True)
    pdf.ln(8)

    pdf.set_font('Nanum', '', 12)
    pdf.set_text_color(0, 0, 0)  # 검정색 텍스트로 변경
    for i, (index, row) in enumerate(dataframe[3].head(5).iterrows(), start=1):
        product_name = row['제품명']
        product_cost_rate = row['제품 단위별 원가율']
        pdf.cell(0, 10, f"{i}등: {product_name} - 원가율: {product_cost_rate:.2f}%", ln=True, align='L')

    pdf.cell(0, 20, "기업 매출 증가를 위해 해당 제품들은 생산량 확대를 적극적으로 고려해야 함", ln=True, align='C')
    pdf.ln(15)

    # 제품 원가율 Worst5 섹션
    pdf.set_font('Nanum', 'B', 14)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트
    pdf.cell(0, 10, '제품의 원가율 Worst 5', align='C', fill=True, ln=True)
    pdf.ln(8)

    pdf.set_font('Nanum', '', 12)
    pdf.set_text_color(0, 0, 0)  # 검정색 텍스트로 변경
    for i, (index, row) in enumerate(dataframe[4].head(5).iterrows(), start=1):
        product_name = row['제품명']
        product_cost_rate = row['제품 단위별 원가율']
        pdf.cell(0, 10, f"{i}등: {product_name} - 원가율: {product_cost_rate:.2f}%", ln=True, align='L')

    pdf.cell(0, 20, "기업의 재정 불안정을 초래할 수 있으니 해당 제품들은 생산량 축소 및 제조 원가 조정이 필수적입니다.", ln=True, align='C')
    
    pdf.ln(15)

    # 총 제조 원가 차이 계산 및 표시 섹션
    pdf.set_font('Nanum', 'B', 14)
    pdf.set_fill_color(178, 34, 34)  # 다크 레드
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트
    pdf.cell(0, 10, '제조 원가 분석 (2022년 vs 2023년)', align='C', fill=True, ln=True)
    pdf.ln(8)

    pdf.set_font('Nanum', '', 12)
    pdf.set_text_color(0, 0, 0)  # 검정색 텍스트로 변경
    Atotal_2023 = dataframe[4]['당기제품 총생산원가'].sum()
    Atotal_2022 = dataframe[5]['당기제품 총생산원가'].sum()
    Adifference = Atotal_2022 - Atotal_2023
    pdf.cell(0, 10, f"2023 - 2022 제조 원가(당기제품 총생산원가) 차: {Adifference:,} 원", ln=True, align='C')

    if Adifference > 0:
        pdf.cell(0, 10, f"2023년 제조 원가(당기제품 총생산원가) 합계는 2022년 대비 {Adifference:,} 원 증가했습니다.", ln=True, align='C')
    else:
        pdf.cell(0, 10, f"2023년 제조 원가(당기제품 총생산원가) 합계는 2022년 대비 {abs(Adifference):,} 원 감소했습니다.", ln=True, align='C')

    return pdf
