from fpdf import FPDF
from datetime import datetime
import pandas as pd
import openai
import os
from io import StringIO
#3

# 엑셀 파일 읽기 고객사 인터뷰 파일

def gPT(df_2):
    # DataFrame을 텍스트로 변환
    df_text_2 = df_2.to_csv(index=False)
    system_query = '''당신은 기업 경영 개선을 위한 분석을 논리적으로 도와주는 유용한 조수입니다.
    제공한 고객사 인터뷰 내용 중 맨위 두줄만 출력하시오
    '''

    user_query = f'''
        여기 CSV 형식으로 제조경비 대장을 제공합니다.:\n{df_text_2}
        '''
        
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_query},
            {"role": "user", "content": user_query}
        ]
    )

    # 응답에서 결과 추출
    final_result = completion.choices[0].message['content']
    return final_result


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.alias_nb_pages()  # 전체 페이지 수를 위한 예약 필드
        self.is_cover_page = False  # 표지 페이지 여부

    def header(self):
        if not self.is_cover_page:  # 표지 페이지가 아니면 헤더 추가
            self.image('image_1.png', 10, 8, 33)
            self.set_font('Nanum', 'B', 12)
            self.cell(0, 10, '기업 보고서', align='C', ln=True)
            self.ln(3)  # 헤더와 내용 사이 간격
            self.line(10, self.get_y(), 200, self.get_y())  # 상단 로고 아래 선 그리기
            self.ln(5)

    def footer(self):
        if not self.is_cover_page:  # 표지 페이지가 아니면 푸터 추가
            self.set_y(-15)
            self.set_draw_color(0, 0, 0)  # 검정색 줄
            self.line(10, self.get_y(), 200, self.get_y())  # 페이지 하단에 줄 긋기

            self.set_y(-10)
            self.set_font('Nanum', '', 8)
            page_number = f'Page {self.page_no()}'
            self.cell(0, 10, page_number, 0, 0, 'R')

def create_pdf_object():
    pdf = PDF()

    # 한글 폰트 추가 (폰트 파일 경로를 실제 경로로 변경해야 합니다)
    pdf.add_font('Nanum', '', 'NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothic-Bold.ttf', uni=True)

    return pdf

def generate_final_result_pdf(final_result):
    pdf = create_pdf_object()
    pdf.add_page()  # 새로운 페이지 추가

    # final_result 텍스트를 가운데에 출력
    pdf.set_font('Nanum', '', 12)
    
    # 텍스트의 높이를 측정하여 세로 중앙에 배치
    lines = final_result.split('\n')
    line_height = 10
    total_height = line_height * len(lines)
    start_y = (pdf.h - total_height) / 2  # 가운데 위치

    pdf.set_y(start_y)
    pdf.multi_cell(0, line_height, final_result, align='C')

    return pdf
