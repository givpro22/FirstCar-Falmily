import pandas as pd

# def manufacturing_4_worstdata(df):
#     # 실제 열 이름으로 수정
#     required_columns = ['제품명', '당기생산수량', '제품별가중치', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율', '당기제품 총생산원가']
    
#     # 주어진 데이터프레임에서 필요한 열만 추출
#     df_filtered = df[0][required_columns]
    
#     # '제품단위별원가율'로 정렬
#     df_sorted = df_filtered.sort_values(by='제품 단위별 원가율', ascending=False)
    
#     # 제품별 가중치가 0.5 이하인 것들을 모두 삭제
#     df_filtered_weight = df_sorted[df_sorted['제품별가중치'] > 0.0005]
    
#     # 상위 5개의 데이터만 반환
#     df_top5 = df_filtered_weight.head(30)
    
#     # 결과 데이터 프레임 반환
#     return df_top5
def manufacturing_4_worstdata(df):
    required_columns = ['제품명', '당기생산수량', '제품별가중치', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율']
    
    # 주어진 데이터프레임에서 필요한 열만 추출
    df = df[0]
    df_filtered = df[required_columns]
    
    # '제품 단위별 원가율'이 0%인 데이터는 제거
    df_filtered_non_zero_cost = df_filtered[df_filtered['제품 단위별 원가율'] > 0]
    
    # 피벗 테이블로 변환 (피벗이 필요없다면 이 단계는 생략 가능)
    df_pivot = df_filtered_non_zero_cost.pivot_table(index='제품명', values=required_columns[1:], aggfunc='sum')
    
    # '제품 단위별 원가율'로 정렬
    df_pivot_sorted = df_pivot.sort_values(by='제품 단위별 원가율', ascending=False)
    
    # 제품별 가중치가 0.5 이하인 것들을 모두 삭제
    df_filtered_weight = df_pivot_sorted[df_pivot_sorted['제품별가중치'] > 0.5]
    
    # 상위 5개의 데이터만 반환
    df_top5 = df_filtered_weight.head(5)
    
    # 결과 데이터 프레임 반환
    return df_top5


#d여기 수정해야함 0822/20:24 기준
def manufacturing_5_bestdata(df):
    # 실제 열 이름으로 수정
    required_columns = ['제품명', '당기생산수량', '제품별가중치', '제품 단위별 생산원가', '제품 단위별 판매단가', '제품 단위별 원가율', '당기제품 총생산원가']
    
    # 주어진 데이터프레임에서 필요한 열만 추출
    df_filtered = df[0][required_columns]
    
    # '제품단위별원가율'로 정렬
    df_sorted = df_filtered.sort_values(by='제품 단위별 원가율', ascending=True)
    
    # 제품별 가중치가 0.5 이하인 것들을 모두 삭제
    df_filtered_weight = df_sorted[df_sorted['제품별가중치'] > 0.0005]
    
    # 상위 5개의 데이터만 반환
    df_top5 = df_filtered_weight.head(30)
    
    # 결과 데이터 프레임 반환
    return df_top5



