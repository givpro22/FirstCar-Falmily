from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from fpdf import FPDF  # fpdf2 라이브러리에서 'fpdf' 모듈을 사용
from pdf_merge import merge_pdfs

from data import process_data, process_2data, process_3data, process_cause, analyze

from xlsxwriter import *
from mf_exp_sum import manufacturing_1data
from raw_ma_sum import manufacturing_2data, manufacturing_3data
from visual import visual
from report import generate_pdf, generate_pdf2, generate_pdf3


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # 업로드된 파일들 가져오기
        df = process_data(files)  # 데이터 전처리 함수 호출 data.py에 있는 함수. finish
        df = manufacturing_1data(df)  # 데이터 가공 함수 호출 mf_exp_sum.py에 있는 함수
        # 엑셀 파일을 메모리에 저장
        onebool_2022 = process_2data(files)
        onebool_2022 = manufacturing_2data(onebool_2022)

        onebool_2023 = process_3data(files)
        onebool_2023 = manufacturing_3data(onebool_2023)
        #visual(df) #데이터를 시각화 해주는 matplot 호출 함수 visual.py에 있는 함수
        merged_df = pd.merge(onebool_2022, onebool_2023)
        


        pdf1 = generate_pdf(df)
        pdf2 = generate_pdf2(merged_df)
        
        # pdf 병합
        merged_pdf_buffer = merge_pdfs(pdf1, pdf2)

          # 파일 포인터를 시작 위치로 이동
        # 생성된 PDF 파일을 다운로드할 수 있게 반환
        return send_file(merged_pdf_buffer, as_attachment=True, download_name='processed_data.pdf', mimetype='application/pdf')
    
    
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)