import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 폰트 경로를 설정
font_path = 'NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

# Matplotlib에 폰트를 설정
plt.rc('font', family=fontprop.get_name())

# 기본적으로 음수 기호가 네모로 나오는 경우가 있어 이를 해결
plt.rcParams['axes.unicode_minus'] = False

# 이미지 저장 폴더 설정
output_dir = 'picture'

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # 첫 번째 원형 차트 (2022년도)
    wedges, texts, autotexts = ax1.pie(
        data_2022_processed,
        labels=data_2022_processed.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("husl", len(data_2022_processed)),
        counterclock=False,
        textprops={'color': 'black', 'fontsize': 12, 'fontproperties': fontprop}
    )
    ax1.set_title(title1, fontsize=16, fontproperties=fontprop)

    # 두 번째 원형 차트 (2023년도)
    wedges, texts, autotexts = ax2.pie(
        data_2023_processed,
        labels=data_2023_processed.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("husl", len(data_2023_processed)),
        counterclock=False,
        textprops={'color': 'black', 'fontsize': 12, 'fontproperties': fontprop}
    )
    ax2.set_title(title2, fontsize=16, fontproperties=fontprop)

    # 두 차트가 원형을 유지하도록 설정
    ax1.set_aspect('equal', adjustable='box')
    ax2.set_aspect('equal', adjustable='box')

    plt.tight_layout()

    # 원형 차트 이미지로 저장
    plt.savefig(os.path.join(output_dir, 'pie_charts.png'), dpi=300, bbox_inches='tight')
   

def visual(df_pivot):
    sns.set(style="whitegrid")

    df_melted = df_pivot.reset_index().melt(id_vars='계정명', value_vars=['2022년', '2023년'], var_name='년도', value_name='차변')

    df_pivot_sorted_2022 = df_pivot.sort_values(by='2022년', ascending=False)
    df_pivot_sorted_2023 = df_pivot.sort_values(by='2023년', ascending=False)

    plt.figure(figsize=(10, 6))
    bar_plot = sns.barplot(data=df_melted, x='계정명', y='차변', hue='년도', palette='viridis')
    plt.title('2022년과 2023년 차변 비교', fontsize=16, fontproperties=fontprop)
    plt.xlabel('계정명', fontsize=14, fontproperties=fontprop)
    plt.ylabel('차변 금액', fontsize=14, fontproperties=fontprop)
    plt.xticks(rotation=90, fontsize=12, fontproperties=fontprop)
    plt.yticks(fontsize=12, fontproperties=fontprop)

    plt.legend(title='년도', title_fontsize='13', fontsize='12', frameon=True, loc='best', borderaxespad=1, edgecolor='black')

    plt.tight_layout()

    plt.savefig(os.path.join(output_dir, 'bar_plot.png'), dpi=300, bbox_inches='tight')
    plot_pie_charts(df_pivot_sorted_2022['2022년'], df_pivot_sorted_2023['2023년'], '2022년 차변 분포', '2023년 차변 분포')
