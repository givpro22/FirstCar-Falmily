import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 엑셀 파일 읽기
file_path = 'C:/Users/214484/Desktop/github/FirstCar-Family/제조경비_대장_엑셀_2022_2023.xlsx'
df = pd.read_excel(file_path)

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
df_filtered = df.loc[:, ['계정명', '등록일', '차변']]

# 등록일에서 년도만 추출
df_filtered['년도'] = pd.to_datetime(df_filtered['등록일']).dt.year

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

# 스타일 설정
sns.set(style="whitegrid")

# 데이터 변환
df_melted = df_pivot.reset_index().melt(id_vars='계정명', value_vars=['2022년', '2023년'], var_name='년도', value_name='차변')

# 데이터 정렬
df_pivot_sorted_2022 = df_pivot.sort_values(by='2022년', ascending=False)
df_pivot_sorted_2023 = df_pivot.sort_values(by='2023년', ascending=False)

# 막대 그래프 생성
plt.figure(figsize=(8, 4))
bar_plot = sns.barplot(data=df_melted, x='계정명', y='차변', hue='년도', palette='viridis')
plt.title('2022년과 2023년 차변 비교', fontsize=16, color='black')
plt.xlabel('계정명', fontsize=14, color='black')
plt.ylabel('차변', fontsize=14, color='black')
plt.xticks(rotation=90, fontsize=12, color='black')
plt.yticks(fontsize=12, color='black')

# 범례를 사각형 테두리로 감싸기
plt.legend(title='년도', title_fontsize='13', fontsize='12', frameon=True, loc='best', borderaxespad=1, edgecolor='black')

plt.tight_layout()
plt.show()

# 데이터 정렬 및 기타 항목 처리
def plot_pie_charts(data_2022, data_2023, title1, title2):
    # 3% 이하 항목을 "기타"로 묶기
    def process_data(data):
        total = data.sum()
        percentages = (data / total) * 100
        data_with_other = data.copy()
        other = data_with_other[percentages < 3]
        data_with_other = data_with_other[percentages >= 3]
        data_with_other['기타'] = other.sum()
        data_with_other = data_with_other.sort_values(ascending=False)
        if '기타' in data_with_other.index:
            기타_value = data_with_other.pop('기타')
            data_with_other['기타'] = 기타_value
        return data_with_other

    # 데이터 처리
    data_2022_processed = process_data(data_2022)
    data_2023_processed = process_data(data_2023)

    # 두 개의 원형 차트를 한 프레임에 표시
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    # 첫 번째 원형 차트 (2022년도)
    wedges, texts, autotexts = ax1.pie(
        data_2022_processed,
        labels=data_2022_processed.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("husl", len(data_2022_processed)),
        counterclock=False,  # 시계방향
        textprops={'color': 'black', 'fontsize': 12}
    )
    ax1.set_title(title1, fontsize=16)

    # 두 번째 원형 차트 (2023년도)
    wedges, texts, autotexts = ax2.pie(
        data_2023_processed,
        labels=data_2023_processed.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("husl", len(data_2023_processed)),
        counterclock=False,  # 시계방향
        textprops={'color': 'black', 'fontsize': 12}
    )
    ax2.set_title(title2, fontsize=16)

    # 두 차트가 원형을 유지하도록 설정
    ax1.set_aspect('equal', adjustable='box')
    ax2.set_aspect('equal', adjustable='box')

    plt.tight_layout()
    plt.show()

# 2022년도와 2023년도 원형 차트를 한 프레임에 표시
plot_pie_charts(df_pivot_sorted_2022['2022년'], df_pivot_sorted_2023['2023년'], '2022년도 차변 분포', '2023년도 차변 분포')