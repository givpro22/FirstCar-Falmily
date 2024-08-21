from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from data import * #여기서 data.py에서 파일
from data import process_data
from xlsxwriter import *
from sum import process_1data
#민혁 hi aaaaa
#수정 test 채민

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # 업로드된 파일들 가져오기
        df = process_data(files)  # 데이터 전처리 함수 호출 data.py에 있는 함수
        df = process_1data(df)  # 데이터 가공 함수 호출 sum.py에 있는 함수
        # 엑셀 파일을 메모리에 저장
        output = BytesIO()
        
        
        
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)  # 파일 포인터를 시작 위치로 이동

        # 생성된 엑셀 파일을 다운로드할 수 있게 반환
        return send_file(output, as_attachment=True, download_name='processed_data.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    return render_template('index.html')

@app.route('/FirstCar', methods=['GET'])
def first_car():
    return render_template('first_car.html')  # /FirstCar에 대한 템플릿 렌더링


if __name__ == '__main__':
    app.run(debug=True)