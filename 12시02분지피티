import pandas as pd
from openai import OpenAI
import os
from io import StringIO

# 엑셀 파일 읽기 고객사 인터뷰 파일
file_path_2 = os.path.join('엑셀파일', '엑셀파일', '고객사_인터뷰_데이터.xlsx')
df_2 = pd.read_excel(file_path_2)

# DataFrame을 텍스트로 변환
df_text_2 = df_2.to_csv(index=False)



# OpenAI API 클라이언트 초기화
client = OpenAI(api_key="api")

system_query = '''당신은 기업 경영 개선을 위한 분석을 논리적으로 도와주는 유용한 조수입니다.
제공한 고객사 인터뷰 내용 중 맨위 두줄만 출력하시오
'''


user_query = f'''
    여기 CSV 형식으로 제조경비 대장을 제공합니다.:\n{df_text_2}
    '''
    
completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": system_query},
    {"role": "user", "content": user_query}
  ]
)

# 응답에서 결과 추출
final_result = completion.choices[0].message.content

print(final_result)
