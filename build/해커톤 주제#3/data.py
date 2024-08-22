import pandas as pd
import openai


def process_data(files):
    # '결산_엑셀_'로 시작하는 파일만 필터링
    dfs = []
    for file in files:
        if file.filename.startswith('제조경비_대장_엑셀_2022_2023'):
            df = pd.read_excel(file)
            dfs.append(df)
    return dfs

def process_2data(files):
    afs = []
    for file in files:
        if file.filename.startswith('원불자재수불부_엑셀_2022'):
            af = pd.read_excel(file)
            afs.append(af)
    return afs

def process_3data(files):
    afs = []
    for file in files:
        if file.filename.startswith('원불자재수불부_엑셀_2023'):
            af = pd.read_excel(file)
            afs.append(af)
    return afs

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis model."},
            {"role": "user", "content": f"Analyze the following text and determine whether the change described in the text is more indicative of an 'increase' or a 'decrease': '{text}'"}
        ]
    )
    analysis = response['choices'][0]['message']['content']
    
    if "increase" in analysis.lower():
        return "증가"
    elif "decrease" in analysis.lower():
        return "감소"
    else:
        return "변동"
    
def process_cause(files):
    result = []

    for file in files:
        if file.filename.startswith('고객사_인터뷰_데이터'):
            af = pd.read_excel(file)
            
            # '증감 추이'가 '변동'인 경우, '고객사 인터뷰 내용'을 분석하여 '증가' 또는 '감소'로 업데이트
            for i, row in af.iterrows():
                if row['증감 추이'] == '변동':
                    sentiment = analyze_sentiment(row['고객사 인터뷰 내용'])
                    af.at[i, '증감 추이'] = sentiment
            
            # 조건에 맞는 새로운 데이터프레임 생성
            filtered_df = af[(af['증감 추이'] == '증가') & (af['해당 연도'] == 2023)]
            
            # 필요한 정보만 추출하여 결과 리스트에 추가
            for _, row in filtered_df.iterrows():
                result.append({
                    '항목': row['항목'],
                    '증감 추이의 원인': f"{row['고객사 인터뷰 내용']}입니다."
                })
    
    # 결과를 데이터프레임으로 변환하여 반환
    result_df = pd.DataFrame(result)
    return result_df