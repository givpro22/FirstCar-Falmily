import os
import pandas as pd

def example(df):
    # 현재 작업 디렉토리 기준으로 'example' 폴더 경로 지정
    folder_path = './example'
    
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # 엑셀 파일의 경로 및 파일명 지정
    output_path = os.path.join(folder_path, 'example_output.xlsx')

    # DataFrame을 엑셀 파일로 저장
    df.to_excel(output_path, index=False)

    # 파일 경로 반환
    return output_path

# 사용 예시
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# file_path = example(df)
# print(f"엑셀 파일이 {file_path}에 저장되었습니다.")
