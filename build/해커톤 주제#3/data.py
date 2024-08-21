import pandas as pd

def process_data(files):
    # 여러 파일을 병합하여 처리하는 함수
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)
    
    # 제품명을 기준으로 병합 (inner join)
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = pd.merge(merged_df, df, on='제품명', how='inner', suffixes=('_left', '_right'))
    
    # 결측값 제거
    merged_df = merged_df.dropna()
    
    # 이상치 제거 및 기타 처리 (위에서 작성한 코드 활용)
    # 예: 'Category' 열이 있다면 처리
    # ... (이전 코드 유지)

    return merged_df