import pandas as pd

def process_data(files):
    dfs = []
    for file in files:
        df = pd.read_excel(file)
        dfs.append(df)
    
    # 모든 데이터프레임을 병합한 단일 데이터프레임 생성
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df