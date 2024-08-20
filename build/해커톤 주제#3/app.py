from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from report import generate_report

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 데이터 업로드 및 분석
        file = request.files['file']
        df = pd.read_csv(file)
        
        # 임의의 데이터 분석 예시 (실제 분석은 기업 데이터에 맞게 수행)
        df['Category'] = df['Category'].astype(str)                      #여기 부분을 data.py 파일에 넣어서 나눠야 할듯 
        report = generate_report(df)                                     
                                                    
        return send_file(report, as_attachment=True, download_name='report.pdf')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
