import pandas as pd

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
def process_1data(df):
    df_filtered = df[0].loc[:, ['계정명', '등록일', '차변']]

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

    # 인덱스를 컬럼으로 변환
    df_pivot = df_pivot.rename(columns={2022: '2022년', 2023: '2023년'}).reset_index()

    # 결과 정렬 및 출력
    df_pivot = df_pivot[['계정명', '2022년', '2023년', '전기대비 증감율']]

    return df_pivot
