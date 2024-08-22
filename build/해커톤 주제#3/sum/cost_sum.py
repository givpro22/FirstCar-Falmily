import pandas as pd

def manufacturing_4data(df):
    # 필요한 열만 선택
    required_columns = ['제품명', '당기생산수량', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율']
    
    # 주어진 데이터프레임에서 필요한 열만 추출
    df = df[0]
    df_filtered = df[required_columns]
    
    # 피벗 테이블로 변환 (피벗이 필요없다면 이 단계는 생략 가능)
    df_pivot = df_filtered.pivot_table(index='제품명', values=required_columns[1:], aggfunc='sum')
    
    # '제품 단위별 원가율'로 정렬
    df_pivot_sorted = df_pivot.sort_values(by='제품 단위별 원가율', ascending=False)
    
    # 결과 데이터 프레임 반환
    return df_pivot_sorted
