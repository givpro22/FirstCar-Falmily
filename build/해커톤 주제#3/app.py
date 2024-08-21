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
from data import * #여기서 data.py에서 파일
from data import process_data
#민혁 hi aaaaa
#수정 test 채민

app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')  # 여러 파일 가져오기
        if not files or len(files) < 2:
            return "Please upload at least two files", 400
        
        df = process_data(files) 
        report = generate_report(df)
        return send_file(report, as_attachment=True, download_name='report.pdf')
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)