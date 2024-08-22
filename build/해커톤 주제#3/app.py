from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from fpdf import FPDF 
from PyPDF2 import PdfMerger
from xlsxwriter import *

from data import process_data, process_2data, process_3data, process_4data, process_5data, process_6data

from sum.mf_exp_sum import manufacturing_1data, manufacturing_0data
from sum.raw_ma_sum import manufacturing_2data, manufacturing_3data
from sum.cost_sum import manufacturing_4_worstdata, manufacturing_5_bestdata

from visual import visual

from pdf_merge import merge_pdfs

from report import generate_pdf, generate_pdf2, generate_pdf3, generate_pdf4
from main_report import main_generate_pdf

from example import example #여기는 이제 example 예시라 나중에 삭제 해야함

from GPT import gpt11, gPT12, gpt13, gpt14, generate_pdf_from_results

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # 업로드된 파일들 가져오기
        df = process_data(files)  # 데이터 전처리 함수 호출 data.py에 있는 함수. finish
        gpt2=gpt11(df[0])
        
        
        df1 = manufacturing_0data(df) # matplotlib 시각화를 위한 전처리 코드
        visual(df1) #데이터를 시각화 해주는 matplot 호출 함수 visual.py에 있는 함수
        df2 = manufacturing_1data(df)  # 데이터 가공 함수 호출 mf_exp_sum.py에 있는 함수
        

        
        # 엑셀 파일을 메모리에 저장
        onebool_2022 = process_2data(files)
        onebool_2022 = manufacturing_2data(onebool_2022)

        onebool_2023 = process_3data(files)
        onebool_2023 = manufacturing_3data(onebool_2023)
        
        
        merged_df = pd.merge(onebool_2022, onebool_2023)
 
        cost_2023 = process_4data(files)
        cost_2023_worst = manufacturing_4_worstdata(cost_2023)
        
        cost_2023 = process_4data(files)                             
        cost_2023_best = manufacturing_5_bestdata(cost_2023)

        cost_2022 = process_5data(files)

        interview = process_6data(files)
        
        
        gPT1 = gPT12(interview[0])
        gPT2 = gpt13(df[0])
        gpt3 = gpt14(gPT2, gpt2, gPT1)
        
        
        
        
        pdf5 = generate_pdf_from_results(gpt3)

        #여기는 pdf 만드는 함수 호출
        pdf1 = generate_pdf(df2)
        pdf2 = generate_pdf2(merged_df)
        pdf3 = generate_pdf3(cost_2023_worst) 
        pdf4 = generate_pdf4(cost_2023_best)     
        main_pdf = main_generate_pdf(df2,onebool_2022,onebool_2023,cost_2023_worst,cost_2023[0], cost_2022[0])
        
        # pdf 병합 
        #merged_pdf_buffer = merge_pdfs(pdf3, pdf1, pdf2, main_pdf)        이거 구현해야 함(채민이 부분)
        merged_pdf_buffer = merge_pdfs(pdf4, pdf3, pdf1, pdf2, main_pdf, pdf5) #위에 만들어지면 지우고
        

          # 파일 포인터를 시작 위치로 이동
        # 생성된 PDF 파일을 다운로드할 수 있게 반환
        return send_file(merged_pdf_buffer, as_attachment=True, download_name='processed_data.pdf', mimetype='application/pdf')
    
    
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)