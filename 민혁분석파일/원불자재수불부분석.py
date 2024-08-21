import pandas as pd
import os

# 상위 폴더에 있는 엑셀 파일 경로 설정
file_path = os.path.join('엑셀파일', '엑셀파일', '원부자재수불부_엑셀_2022.xlsx')#엑셀파일\엑셀파일\원부자재수불부_엑셀_2022.xlsx

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택 (원재료명, 생산 출고금액)
df_filtered = df[['원재료명', '생산 출고금액']]

# 생산 출고금액이 0이 아닌 행만 선택
df_filtered = df_filtered[df_filtered['생산 출고금액'] != 0]

# 생산 출고금액 기준으로 내림차순 정렬
df_sorted = df_filtered.sort_values(by='생산 출고금액', ascending=False)

# 분석 결과 엑셀 파일에 저장
output_path = os.path.join('분석결과 엑셀', 'sorted_output_file.xlsx')
df_sorted.to_excel(output_path, index=False)

print(f"최종 데이터가 '{output_path}' 파일로 저장되었습니다.")
