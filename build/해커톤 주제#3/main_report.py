from fpdf import FPDF
from io import BytesIO
import pandas as pd

def main_generate_pdf(df, onebool_2022, onebool_2023, cost_2022):
    # 열 이름 확인 및 올바른 열 이름으로 수정
    print(df.columns)  # 현재 데이터프레임의 열 이름 확인
    
    account_name = '지급수수료'  # 존재하는 열 이름으로 수정 필요
    selected_columns = ['2022년', '2023년']

    # 예를 들어 '계정명' 대신 'Account Name'이라는 열 이름이 있다면 아래와 같이 수정합니다.
    df_selected = df[df['계정명'] == account_name][selected_columns]
    onebool_2022_selected = onebool_2022[onebool_2022['계정명'] == account_name][selected_columns]
    onebool_2023_selected = onebool_2023[onebool_2023['계정명'] == account_name][selected_columns]
    cost_2022_selected = cost_2022[cost_2022['계정명'] == account_name][selected_columns]
    
    # 차이 계산
    df_difference = df_selected['2023년'].values[0] - df_selected['2022년'].values[0]
    onebool_2022_difference = onebool_2022_selected['2023년'].values[0] - onebool_2022_selected['2022년'].values[0]
    onebool_2023_difference = onebool_2023_selected['2023년'].values[0] - onebool_2023_selected['2022년'].values[0]
    cost_2022_difference = cost_2022_selected['2023년'].values[0] - cost_2022_selected['2022년'].values[0]

    # PDF 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # PDF에 결과 추가
    pdf.cell(200, 10, txt="Data Difference Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"{account_name} - DF Difference (2023 - 2022): {df_difference}", ln=True)
    pdf.cell(200, 10, txt=f"{account_name} - Onebool 2022 Difference (2023 - 2022): {onebool_2022_difference}", ln=True)
    pdf.cell(200, 10, txt=f"{account_name} - Onebool 2023 Difference (2023 - 2022): {onebool_2023_difference}", ln=True)
    pdf.cell(200, 10, txt=f"{account_name} - Cost 2022 Difference (2023 - 2022): {cost_2022_difference}", ln=True)
    
    # PDF 저장
    output = BytesIO()
    pdf.output(output)
    output.seek(0)

    return output
