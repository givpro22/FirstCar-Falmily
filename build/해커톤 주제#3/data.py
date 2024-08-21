import pandas as pd


def process_data(files):
    # '결산_엑셀_'로 시작하는 파일만 필터링
    dfs = []
    for file in files:
        if file.filename.startswith('결산_엑셀_'):
            df = pd.read_excel(file)
            dfs.append(df)
    
    # '제품명' 기준으로 병합
    if dfs:
        merged_df = dfs[0]  # 첫 번째 데이터프레임을 기준으로 초기화
        for df in dfs[1:]:
            merged_df = pd.merge(merged_df, df, on='제품명', how='outer')  # outer join으로 병합
    else:
        merged_df = pd.DataFrame()  # 필터링된 파일이 없는 경우 빈 데이터프레임 반환
    
    return merged_df