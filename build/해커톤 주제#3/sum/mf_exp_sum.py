import pandas as pd

def manufacturing_0data(df):
    # 만약 df가 리스트로 전달되었다면 df[0]을 사용하고, 그렇지 않다면 df를 사용
    if isinstance(df, list):
        df_filtered = df[0].loc[:, ['계정명', '등록일', '차변']]
    else:
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
    return df_pivot

# 필요한 칼럼만 선택 (계정명, 등록일, 차변)
def manufacturing_1data(df):
    # 만약 df가 리스트로 전달되었다면 df[0]을 사용하고, 그렇지 않다면 df를 사용
    if isinstance(df, list):
        df_filtered = df[0].loc[:, ['계정명', '등록일', '차변']]
    else:
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

    # 인덱스를 컬럼으로 변환
    df_pivot = df_pivot.rename(columns={2022: '2022년', 2023: '2023년'}).reset_index()

    # 2022년과 2023년 합계 계산
    total_2022 = df_pivot['2022년'].sum()
    total_2023 = df_pivot['2023년'].sum()

    # 합계 행 추가
    total_row = pd.DataFrame([['합계', total_2022, total_2023, None]], columns=['계정명', '2022년', '2023년', '전기대비 증감율'])
    df_pivot = pd.concat([df_pivot, total_row], ignore_index=True)

    # 결과 정렬 및 출력
    df_pivot = df_pivot[['계정명', '2022년', '2023년', '전기대비 증감율']]
    return df_pivot
