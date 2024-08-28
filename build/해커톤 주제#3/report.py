from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.alias_nb_pages()  # 전체 페이지 수를 위한 예약 필드
        self.is_cover_page = False  # 표지 페이지 여부

    def header(self):
        if not self.is_cover_page:  # 표지 페이지가 아니면 header 추가
            self.image('image_1.png', 10, 8, 33)
            self.set_font('Nanum', 'B', 16)
            self.set_text_color(0, 149, 219)  # 이미지에서 파란색으로 설정
            self.cell(0, 10, '기업 보고서', align='C', ln=True)
            self.ln(5)  # 헤더와 내용 사이 간격
            self.line(10, self.get_y(), 200, self.get_y())  # 상단 로고 아래 선 그리기
            self.ln(10)

    def footer(self):
        if not self.is_cover_page:  # 표지 페이지가 아니면 footer 추가
            self.set_y(-15)
            self.set_draw_color(0, 0, 0)  # 검정색 줄
            self.line(10, self.get_y(), 200, self.get_y())  # 페이지 하단에 줄 긋기

            # self.set_y(-10)
            # self.set_font('Nanum', '', 8)
            # page_number = f'Page {self.page_no()}'
            # self.cell(0, 10, page_number, 0, 0, 'R')

def create_pdf_object():
    pdf = PDF()

    # 한글 폰트 추가
    pdf.add_font('Nanum', '', 'NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothic-Bold.ttf', uni=True)

    return pdf

def add_cover_page(pdf):
    pdf.is_cover_page = True  # 표지 페이지 시작
    pdf.add_page()

    # 로고 이미지 중앙에 배치
    logo_path = 'image_1.png'
    logo_width, logo_height = 50, 30  # 로고 크기 조정
    pdf.image(logo_path, x=(pdf.w - logo_width) / 2, y=(pdf.h - logo_height) / 2 - 60, w=logo_width, h=logo_height)

    pdf.set_y(pdf.h / 2 + 10)  # 로고 아래로 위치 설정
    pdf.set_font('Nanum', 'B', 30)
    pdf.cell(0, 20, '기업 경영 AI 분석 보고서', ln=True, align='C')

    pdf.set_font('Nanum', '', 13)
    pdf.cell(0, 10, '보고서 작성일:', ln=True, align='C')
    pdf.cell(0, 10, datetime.now().strftime('%Y-%m-%d'), ln=True, align='C')

    pdf.ln(20)
    pdf.set_font('Nanum', '', 12)
    pdf.multi_cell(0, 10, '\n\n이 보고서는 회사의 재무 상태와 주요 원재료 출고량, 고객 인터뷰 등을 포함한 종합 보고서입니다. \n회사 내부 자료로만 사용되며 외부 유출을 금합니다.', align='C')
    pdf.is_cover_page = False  # 표지 페이지 종료

def generate_pdf(dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 페이지 추가 시 header와 footer가 자동으로 적용됩니다.

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '재무 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    # 테이블 헤더 설정 (페이지 여백과 일치하도록 열 너비 조정)
    margin_x = 10  # 좌우 여백
    table_width = pdf.w - 2 * margin_x  # 여백을 뺀 테이블 전체 너비
    col_widths = [table_width * 0.35, table_width * 0.2, table_width * 0.2, table_width * 0.25]  # 열 너비 설정

    pdf.set_x(margin_x)
    pdf.set_font('Nanum', 'B', 12)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색 배경
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트

    headers = ['계정명', '2022년', '2023년', '전기대비 증감율']
    for width, header in zip(col_widths, headers):
        pdf.cell(width, 10, header, border=1, align='C', fill=True)
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    pdf.set_text_color(0, 0, 0)  # 검은색 텍스트로 초기화
    for index, row in dataframe.iterrows():
        pdf.set_x(margin_x)
        pdf.cell(col_widths[0], 10, str(row['계정명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row['2022년']):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['2023년']):,}", border=1, align='R')
        
        # 증감율 계산 및 화살표와 색상 설정
        change = row['전기대비 증감율']
        if change < 0:
            arrow = '▼'
            pdf.set_text_color(255, 0, 0)  # 감소일 경우 빨간색
        else:
            arrow = '▲'
            pdf.set_text_color(0, 0, 255)  # 증가일 경우 파란색

        pdf.cell(col_widths[3], 10, f"{arrow} {abs(change):.2f}%", border=1, align='R')
        pdf.set_text_color(0, 0, 0)  # 다음 행을 위해 텍스트 색상을 검정으로 초기화
        pdf.ln()

    return pdf

def generate_pdf2(dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 페이지 추가 시 header와 footer가 자동으로 적용됩니다.

    # 테이블 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '원재료 요약 (2022년 vs 2023년)', ln=True, align='C')
    pdf.ln(10)

    margin_x = 10  # 좌우 여백
    table_width = pdf.w - 2 * margin_x  # 여백을 뺀 테이블 전체 너비
    col_widths = [table_width * 0.275, table_width * 0.225, table_width * 0.275, table_width * 0.225]  # 열 너비 설정

    # 테이블 헤더 설정
    pdf.set_font('Nanum', 'B', 12)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색 배경
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트

    pdf.set_x(margin_x)
    headers = ['원재료명 (2022)', '총 출고량 (2022)', '원재료명 (2023)', '총 출고량 (2023)']
    for width, header in zip(col_widths, headers):
        pdf.cell(width, 10, header, border=1, align='C', fill=True)
    pdf.ln()

    # 테이블 내용 추가
    pdf.set_font('Nanum', '', 10)
    pdf.set_text_color(0, 0, 0)  # 검은색 텍스트로 초기화
    for index, row in dataframe.iterrows():
        pdf.set_x(margin_x)
        pdf.cell(col_widths[0], 10, str(row['원재료명']), border=1)
        pdf.cell(col_widths[1], 10, f"{int(row.get('2022 총 출고량', 0)):,}", border=1, align='R')
        pdf.cell(col_widths[2], 10, str(row['원재료명']), border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{int(row.get('2023 총 출고량', 0)):,}", border=1, align='R')
        pdf.ln()

    # 이미지 삽입 부분
    pdf.ln()  # 테이블과 이미지 사이의 간격

    # 이미지 제목 추가
    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '2022년과 2023년 차변 비교', ln=True, align='C')
    pdf.ln(5)

    # 첫 번째 이미지 삽입 (bar_plot.png)
    pdf.image('picture/bar_plot.png', x=margin_x, y=None, w=table_width)

    # 두 번째 이미지 삽입 (pie_charts.png)
    pdf.ln(10)  # 두 이미지 사이의 간격

    pdf.set_font('Nanum', 'B', 14)
    pdf.cell(0, 10, '2022년 차변 분포 / 2023년 차변 분포', ln=True, align='C')
    pdf.ln(5)
    pdf.image('picture/pie_charts.png', x=margin_x, y=None, w=table_width)

    return pdf

def generate_pdf3(dataframe):
    pdf = create_pdf_object()
    pdf.add_page()  # 새로운 페이지 추가

    # 보고서 제목 설정
    pdf.set_font('Nanum', 'B', 20)
    pdf.cell(0, 10, 'FY2023 원가율 WORST 20', ln=True, align='C')
    pdf.set_font('Nanum', '', 12)
    pdf.cell(0, 10, '(단위: 원)', ln=True, align='R')
    pdf.ln(10)

    margin_x = 10  # 좌우 여백
    table_width = pdf.w - 2 * margin_x  # 여백을 뺀 테이블 전체 너비
    col_widths = [table_width * 0.2, table_width * 0.15, table_width * 0.25, table_width * 0.2, table_width * 0.2]  # 열 너비 설정

    # WORST 10 테이블 헤더
    pdf.set_font('Nanum', 'B', 12)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색 배경
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트
    pdf.set_x(margin_x)
    headers = ['제품명', '당기생산수량', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율']
    for width, header in zip(col_widths, headers):
        pdf.cell(width, 10, header, border=1, align='C', fill=True)
    pdf.ln()

    # WORST 10 테이블 내용
    pdf.set_font('Nanum', '', 10)
    pdf.set_text_color(0, 0, 0)  # 검은색 텍스트
    for index, row in dataframe.iterrows():
        pdf.set_x(margin_x)
        pdf.cell(col_widths[0], 10, str(row['제품명']), border=1)
        pdf.cell(col_widths[1], 10, str(row['당기생산수량']), border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['제품 단위별 생산원가']):,}", border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{int(row['제품 단위별 판매단가']):,}", border=1, align='R')
        pdf.cell(col_widths[4], 10, f"{row['제품 단위별 원가율']:.2f}%", border=1, align='R')
        pdf.ln()

    return pdf

def generate_pdf4(dataframe):
    pdf = create_pdf_object()
    add_cover_page(pdf)  # 표지 추가, 한 번만 호출
    pdf.add_page()  # 페이지 추가 시 header와 footer가 자동으로 적용됩니다.

    # 보고서 제목 설정
    pdf.set_font('Nanum', 'B', 20)
    pdf.cell(0, 10, 'FY2023 원가율 BEST 20', ln=True, align='C')
    pdf.set_font('Nanum', '', 12)
    pdf.cell(0, 10, '(단위: 원)', ln=True, align='R')
    pdf.ln(10)

    margin_x = 10  # 좌우 여백
    table_width = pdf.w - 2 * margin_x  # 여백을 뺀 테이블 전체 너비
    col_widths = [table_width * 0.2, table_width * 0.15, table_width * 0.25, table_width * 0.2, table_width * 0.2]  # 열 너비 설정

    # BEST 10 테이블 헤더
    pdf.set_font('Nanum', 'B', 12)
    pdf.set_fill_color(128, 0, 0)  # 어두운 빨간색 배경
    pdf.set_text_color(255, 255, 255)  # 흰색 텍스트
    pdf.set_x(margin_x)
    headers = ['제품명', '당기생산수량', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율']
    for width, header in zip(col_widths, headers):
        pdf.cell(width, 10, header, border=1, align='C', fill=True)
    pdf.ln()

    # BEST 10 테이블 내용
    pdf.set_font('Nanum', '', 10)
    pdf.set_text_color(0, 0, 0)  # 검은색 텍스트
    for index, row in dataframe.iterrows():
        pdf.set_x(margin_x)
        pdf.cell(col_widths[0], 10, str(row['제품명']), border=1)
        pdf.cell(col_widths[1], 10, str(row['당기생산수량']), border=1, align='R')
        pdf.cell(col_widths[2], 10, f"{int(row['제품 단위별 생산원가']):,}", border=1, align='R')
        pdf.cell(col_widths[3], 10, f"{int(row['제품 단위별 판매단가']):,}", border=1, align='R')
        pdf.cell(col_widths[4], 10, f"{row['제품 단위별 원가율']:.2f}%", border=1, align='R')
        pdf.ln()

    return pdf
