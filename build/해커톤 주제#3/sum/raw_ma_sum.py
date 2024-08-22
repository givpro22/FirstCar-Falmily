import pandas as pd
import os

def manufacturing_2data(df):
    # 필요한 칼럼만 선택 (원재료명, 총 출고금액)
    df_filtered = df[0][['원재료명', '총 출고량']]

    # 총 출고금액이 0이 아닌 행만 선택
    df_filtered = df_filtered[df_filtered['총 출고량'] != 0]

    # 총 출고금액 기준으로 내림차순 정렬하고 상위 10개만 선택
    df_sorted = df_filtered.sort_values(by='총 출고량', ascending=False).head(10)

    # 총 출고금액 칼럼명 변경
    df_sorted = df_sorted.rename(columns={'총 출고량': '2022 총 출고량'})

    return df_sorted

def manufacturing_3data(df):
    # 필요한 칼럼만 선택 (원재료명, 총 출고금액)
    df_filtered = df[0][['원재료명', '총 출고량']]

    # 총 출고금액이 0이 아닌 행만 선택
    df_filtered = df_filtered[df_filtered['총 출고량'] != 0]

    # 총 출고금액 기준으로 내림차순 정렬하고 상위 10개만 선택
    df_sorted = df_filtered.sort_values(by='총 출고량', ascending=False).head(10)

    # 총 출고금액 칼럼명 변경
    df_sorted = df_sorted.rename(columns={'총 출고량': '2023 총 출고량'})

    return df_sorted