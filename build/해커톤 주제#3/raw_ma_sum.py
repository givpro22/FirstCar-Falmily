import pandas as pd
import os

def manufacturing_2data(af):
    # 상위 폴더에 있는 엑셀 파일 경로 설정
 
    # 필요한 칼럼만 선택 (원재료명, 생산 출고금액)
    df_filtered = af[0][['원재료명', '생산 출고금액']]

    # 생산 출고금액이 0이 아닌 행만 선택
    df_filtered = df_filtered[df_filtered['생산 출고금액'] != 0]

    # 생산 출고금액 기준으로 내림차순 정렬
    df_sorted = df_filtered.sort_values(by='생산 출고금액', ascending=False)

    return df_sorted