from fpdf import FPDF

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

def main_generate_pdf(*dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 내용 시작할 페이지 추가

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '원가분석 결과', ln=True, align='C')
    pdf.ln(10)

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 12)

    # 합계 행에서 2023년과 2022년의 차이 계산
    total_2022 = dataframe[0].loc[dataframe[0]['계정명'] == '합계', '2022년'].values[0]
    total_2023 = dataframe[0].loc[dataframe[0]['계정명'] == '합계', '2023년'].values[0]
    difference = total_2023 - total_2022

    # 차이값을 텍스트로 표현
    pdf.cell(0, 10, f"2023년 합계에서 2022년 제조경비(노무비 + 경비) 합계를 뺀 값: {difference:,} 원", ln=True, align='C')
    
    #2022년 2023년 제조원가(당기제품 총 생산원가) 합계를 뺀 값
    
    
    return pdf
