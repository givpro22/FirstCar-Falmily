import pandas as pd

def manufacturing_4_worstdata(df):
    # 실제 열 이름으로 수정
    required_columns = ['제품명', '당기생산수량', '제품별가중치', '제품 단위별 생산원가', '제품 단위별 판매단가', '당기제품 총생산원가']
    
    # 주어진 데이터프레임에서 필요한 열만 추출
    df_filtered = df[0][required_columns]
    
    # '제품 단위별 판매단가'가 0인 행을 제거
    df_filtered = df_filtered[df_filtered['제품 단위별 판매단가'] > 0]
    
    # '제품별 가중치'가 0.5% 미만인 항목 제거
    df_filtered = df_filtered[df_filtered['제품별가중치'] >= 0.005]
    
    # '제품 단위별 원가율' 계산하여 열로 추가 (백분율로 표현)
    df_filtered['제품 단위별 원가율'] = (df_filtered['제품 단위별 생산원가'] / df_filtered['제품 단위별 판매단가']) * 100
    
    # '제품 단위별 원가율'로 내림차순 정렬
    df_sorted = df_filtered.sort_values(by='제품 단위별 원가율', ascending=False)
    
    # 상위 10개의 데이터만 반환
    df_top10 = df_sorted.head(20)
    
    # 결과 데이터 프레임 반환
    return df_top10

#d여기 수정해야함 0822/20:24 기준
def manufacturing_5_bestdata(df):
    # 실제 열 이름으로 수정
    required_columns = ['제품명', '당기생산수량', '제품별가중치', '제품 단위별 생산원가', '제품 단위별 판매단가', '당기제품 총생산원가']
    
    # 주어진 데이터프레임에서 필요한 열만 추출
    df_filtered = df[0][required_columns]

    df_filtered = df_filtered[df_filtered['제품 단위별 판매단가'] > 0]
    
    df_filtered['제품 단위별 원가율'] = df_filtered['제품 단위별 생산원가'] / df_filtered['제품 단위별 판매단가'] *100
    # '제품단위별원가율'로 정렬
    df_sorted = df_filtered.sort_values(by='제품 단위별 원가율', ascending=True)
    
    df_top5 = df_sorted.head(20)
    
    # 결과 데이터 프레임 반환
    return df_top5



