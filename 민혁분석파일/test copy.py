'''import pandas as pd

# 엑셀 파일 읽기
file_path = 'C:/Users/dhals/Desktop/pdf#3/엑셀파일/제조경비_대장_엑셀_2022_2023.xlsx'  # 엑셀 파일 경로를 입력하세요.
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택
df_filtered = df[['계정명', '차변']]

# 계정명으로 그룹화하여 차변 합산
df_grouped = df_filtered.groupby('계정명', as_index=False).sum()

# 결과 출력
print(df_grouped)

# 필요한 경우, 결과를 새로운 엑셀 파일로 저장
output_path = 'C:/Users/dhals/Desktop/pdf#3/엑셀파일/output_file.xlsx'  # 저장할 파일 경로를 입력하세요.
df_grouped.to_excel(output_path, index=False)'''


import pandas as pd
import os

# 엑셀 파일 읽기
file_path = os.path.join('엑셀파일', '엑셀파일', '제조경비_대장_엑셀_2022_2023.xlsx')
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
df_filtered = df.loc[:, ['계정명', '등록일', '차변']]

# 등록일에서 년도만 추출
df_filtered.loc[:, '년도'] = pd.to_datetime(df_filtered['등록일']).dt.year

# 2022년과 2023년의 데이터만 필터링
df_filtered = df_filtered[df_filtered['년도'].isin([2022, 2023])]

# 계정명과 년도로 그룹화하여 차변 합산
df_grouped = df_filtered.groupby(['계정명', '년도'], as_index=False)['차변'].sum()

# 2022년과 2023년 데이터를 피벗 테이블로 변환
df_pivot = df_grouped.pivot(index='계정명', columns='년도', values='차변').fillna(0)

# 2022년, 2023년, 증감율 계산
df_pivot['전기대비 증감율'] = (df_pivot[2023] - df_pivot[2022]) / df_pivot[2022] * 100

# 결과 정렬 및 출력
df_pivot = df_pivot.rename(columns={2022: '2022년', 2023: '2023년'})
df_pivot = df_pivot[['2022년', '2023년', '전기대비 증감율']]

print(df_pivot)

# 필요한 경우, 결과를 새로운 엑셀 파일로 저장
output_path = os.path.join('분석결과 엑셀', 'output_file.xlsx')
df_pivot.to_excel(output_path)
