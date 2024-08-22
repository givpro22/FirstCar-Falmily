from fpdf import FPDF
from datetime import datetime
import pandas as pd
from openai import OpenAI
import os

#=====================================================
client = OpenAI(api_key="============================================")

# 엑셀 파일 읽기
file_path = os.path.join('FirstCar-Family', '엑셀파일', '엑셀파일', '제조경비_대장_엑셀_2022_2023.xlsx')
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
df_filtered = df.loc[:, ['계정명', '등록일', '차변', '내용']]

# 등록일에서 년도만 추출
df_filtered.loc[:, '등록연도'] = pd.to_datetime(df_filtered['등록일']).dt.year

# 기존 '등록일' 열 제거
df_filtered = df_filtered.drop(columns=['등록일'])

#test copy.py 증감율 계산은 잠시뻬자
#print(df_filtered)

#==================================================

# 엑셀 파일 경로 설정
file_path_2 = os.path.join('FirstCar-Family', '엑셀파일', '엑셀파일', '고객사_인터뷰_데이터.xlsx')
df_2 = pd.read_excel(file_path_2)

# '증감 추이' 칼럼 제거
if '증감 추이' in df_2.columns:
    df_2 = df_2.drop(columns=['증감 추이'])

# '해당 연도' 칼럼에서 2022년 데이터가 있는 행 제거
if '해당 연도' in df_2.columns:
    df_2 = df_2[df_2['해당 연도'] != 2022]

df_2 = df_2.drop(columns=['해당 연도'])

# 결과 DataFrame 반환
#print(df_2)
#print(df_filtered)
#============================================================================
file_path = os.path.join('FirstCar-Family', '엑셀파일', '엑셀파일', '제조경비_대장_엑셀_2022_2023.xlsx')
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
df_filtered_2 = df.loc[:, ['계정명', '등록일', '차변']]

# 등록일에서 년도만 추출
df_filtered_2.loc[:, '년도'] = pd.to_datetime(df_filtered_2['등록일']).dt.year

# 2022년과 2023년의 데이터만 필터링
df_filtered_2 = df_filtered_2[df_filtered_2['년도'].isin([2022, 2023])]

# 계정명과 년도로 그룹화하여 차변 합산
df_grouped = df_filtered_2.groupby(['계정명', '년도'], as_index=False)['차변'].sum()

# 2022년과 2023년 데이터를 피벗 테이블로 변환
df_pivot = df_grouped.pivot(index='계정명', columns='년도', values='차변').fillna(0)

# 2022년, 2023년, 증감율 계산
df_pivot['전기대비 증감율'] = (df_pivot[2023] - df_pivot[2022]) / df_pivot[2022] * 100

# 결과 정렬 및 출력
df_pivot = df_pivot.rename(columns={2022: '2022년', 2023: '2023년'})
df_pivot = df_pivot[['2022년', '2023년', '전기대비 증감율']]

df_pivot = df_pivot[df_pivot['전기대비 증감율'].abs() >= 10]

#print(df_pivot)
#============================================================================

# df_pivot에 존재하는 계정명만 사용
df_pivot_accounts = df_pivot.index

final_dicts = []

# df_filtered의 '계정명'과 df_2의 '항목'에서 공통된 항목을 찾아 처리
for 계정명 in df_filtered['계정명'].unique():
    if 계정명 in df_pivot_accounts and 계정명 in df_2['항목'].values:
        # 공통된 계정명에 해당하는 데이터프레임 필터링
        df_filtered_sub = df_filtered[df_filtered['계정명'] == 계정명].reset_index(drop=True)
        df_filtered_sub.insert(0, '해당 행 번호', df_filtered_sub.index + 1)

        # 공통된 항목에 해당하는 df_2 부분 필터링
        df_2_sub = df_2[df_2['항목'] == 계정명].reset_index(drop=True)
        df_2_sub.insert(0, '해당 행 번호', df_2_sub.index + 1)

        # 딕셔너리 생성
        dic = {
            '계정명': 계정명,
            'data1': df_filtered_sub[['해당 행 번호', '계정명', '차변', '내용', '등록연도']],
            'data2': df_2_sub[['해당 행 번호', '항목', '고객사 인터뷰 내용']]
        }

        # 딕셔너리를 리스트에 추가
        final_dicts.append(dic)
#===================================================
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.alias_nb_pages()  # 전체 페이지 수를 위한 예약 필드
        self.is_cover_page = False  # 표지 페이지 여부

    def header(self):
        if not self.is_cover_page:  # 표지 페이지가 아니면 header 추가
            self.image('C:/Users/dhals/Desktop/pdf#3/FirstCar-Family/build/해커톤 주제#5/assets/frame0/image_1.png', 10, 8, 33)
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

            self.set_y(-10)
            self.set_font('Nanum', '', 8)
            page_number = f'Page {self.page_no()}'
            self.cell(0, 10, page_number, 0, 0, 'R')

    def get_string_height(self, text, w):
        # 주어진 너비(w)에서 텍스트가 차지하는 줄 수를 계산하고 높이를 반환합니다.
        lines = self.multi_cell(w, 10, text, split_only=True)  # split_only=True로 실제 출력은 하지 않고 줄만 나눕니다.
        line_count = len(lines)
        return line_count * 10  # 10은 한 줄의 높이입니다.

def create_pdf_object():
    pdf = PDF()

    # 한글 폰트 추가
    pdf.add_font('Nanum', '', 'C:/Users/dhals/OneDrive/바탕 화면/NanumGothic-Regular.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'C:/Users/dhals/OneDrive/바탕 화면/NanumGothic-Bold.ttf', uni=True)

    return pdf

def generate_pdf_from_results(final_dicts):
    pdf = create_pdf_object()
    pdf.add_page()

    for dic in final_dicts:
        계정명 = dic['계정명']
        
        # data1과 data2를 CSV 형식의 텍스트로 변환
        data1_text = dic['data1'].to_csv(index=False)
        data2_text = dic['data2'].to_csv(index=False)
        
        # GPT 모델에 전달할 메시지 작성
        user_query = f"""
        계정명: {계정명}
        data1 데이터:
        {data1_text}
        
        data2 데이터:
        {data2_text}
        
        위의 두 데이터셋 간의 연관성을 분석하고, 중요한 인사이트를 도출해주세요.
        """
        
        # GPT API 호출
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 두 데이터셋 간의 연관성을 분석하는 데이터 과학자입니다. 두줄로 간단히 분석하세요. 포인트는 전년도 대비 올해의 비용 변화가 어디서 일어났는지 중요하며, 예를들면 data2인터뷰 내용을 바탕으로 data1에서 작년엔 없었지만 올해 새로 생긴 비용 내용을 발견하거나 불필요하다고 느껴지는 비용(차변)끼리 더해서 숫자로 제시하시오.(신규항목이지만 제조기업의 성장이나 복지를 위해 불가피한 항목이라고 판단되면 그부분은 언급하지 말것.)"},
                {"role": "user", "content": user_query}
            ]
        )
        
        # 결과 추출
        result = completion.choices[0].message.content

        # 현재 페이지에 필요한 공간 계산
        needed_height = pdf.get_string_height(result, w=pdf.w - 20) + 20  # 20은 여유 공간을 위해 추가
        if pdf.get_y() + needed_height > pdf.h - 20:  # 20은 footer와의 여유 공간
            pdf.add_page()

        # 계정명 및 결과 출력
        pdf.set_font('Nanum', 'B', 14)
        pdf.cell(0, 10, f'계정명: {계정명}', ln=True, align='C')
        pdf.ln(5)

        pdf.set_font('Nanum', '', 12)
        pdf.multi_cell(0, 10, result)
        pdf.ln(10)  # 계정 간에 간격 추가

    return pdf

# 결과 PDF 생성 및 저장
pdf = generate_pdf_from_results(final_dicts)
pdf_output_path = "final_results_report.pdf"
pdf.output(pdf_output_path)

print(f"PDF 파일이 생성되었습니다: {pdf_output_path}")