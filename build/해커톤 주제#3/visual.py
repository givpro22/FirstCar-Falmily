import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_pie_chart(data, year, title):
        # 비율 계산
        total = data.sum()
        percentages = (data / total) * 100
        
        # 3% 이하 항목을 "기타"로 묶기
        data_with_other = data.copy()
        other = data_with_other[percentages < 3]
        data_with_other = data_with_other[percentages >= 3]
        data_with_other['기타'] = other.sum()
        
        # 정렬 (큰 퍼센트부터)
        data_with_other = data_with_other.sort_values(ascending=False)
        
        # 원형 차트 생성
        plt.figure(figsize=(12, 8))
        wedges, texts, autotexts = plt.pie(
            data_with_other,
            labels=data_with_other.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette("husl", len(data_with_other)),
            counterclock=False,  # 시계방향
            wedgeprops=dict(width=0.4, edgecolor='w'),
            textprops={'color': 'black', 'fontsize': 12}
        )
        plt.title(title, fontsize=16, color='black')
        
        # 스타일 설정
        for text in texts:
            text.set_fontsize(10)
            text.set_color('black')
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontsize(12)
        
        # 원형 차트의 원형을 일정하게 유지하기 위해 `equal` aspect ratio 설정
        plt.gca().set_aspect('equal', adjustable='box')

        plt.show()

def visual(df_pivot):
    # 스타일 설정
    sns.set(style="whitegrid")

    # 데이터 변환
    df_melted = df_pivot.reset_index().melt(id_vars='계정명', value_vars=['2022년', '2023년'], var_name='년도', value_name='차변')

    # 데이터 정렬
    df_pivot_sorted_2022 = df_pivot.sort_values(by='2022년', ascending=False)
    df_pivot_sorted_2023 = df_pivot.sort_values(by='2023년', ascending=False)

    # 막대 그래프 생성
    plt.figure(figsize=(14, 8))
    bar_plot = sns.barplot(data=df_melted, x='계정명', y='차변', hue='년도', palette='viridis')
    plt.title('2022년과 2023년 차변 비교', fontsize=16, color='black')
    plt.xlabel('계정명', fontsize=14, color='black')
    plt.ylabel('차변', fontsize=14, color='black')
    plt.xticks(rotation=90, fontsize=12, color='black')
    plt.yticks(fontsize=12, color='black')
    plt.legend(title='년도', title_fontsize='13', fontsize='12', frameon=False, loc='best')
    plt.tight_layout()
    plt.show()

    # 데이터 정렬 및 기타 항목 처리
    

    # 2022년도 원형 차트
    plot_pie_chart(df_pivot_sorted_2022['2022년'], 2022, '2022년도 차변 분포')

    # 2023년도 원형 차트
    plot_pie_chart(df_pivot_sorted_2023['2023년'], 2023, '2023년도 차변 분포')
