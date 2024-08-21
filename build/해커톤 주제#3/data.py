import pandas as pd


def process_data(file):
    # CSV 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(file)
    
    # 1. 결측값 제거
    df = df.dropna()
    
    # 2. 특정 열의 이상치 제거 (예: 'Category' 열을 기준으로 IQR 방법 사용)
    # 여기서는 임의로 'Category' 열의 숫자형 데이터를 처리한다고 가정합니다.
    
    if 'Category' in df.columns:
        # 'Category' 열이 숫자형 데이터일 경우
        if pd.api.types.is_numeric_dtype(df['Category']):
            Q1 = df['Category'].quantile(0.25)
            Q3 = df['Category'].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # 이상치 제거
            df = df[(df['Category'] >= lower_bound) & (df['Category'] <= upper_bound)]

    # 3. 'Category' 열을 문자열 타입으로 변환
    df['Category'] = df['Category'].astype(str)
    
    return df