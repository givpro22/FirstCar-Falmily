import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

# 경영 개선 리포트 생성 함수
def generate_report(data):
    # 데이터 분석 및 시각화
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Value', data=data)
    plt.title('Category vs Value')
    
    # 그래프를 메모리에 저장
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    
    # PDF 리포트 생성
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Management Improvement Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # 이미지 추가
    elements.append(Image(img_buf))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Based on the analysis of the raw data, the following insights were found...", styles['Normal']))

    pdf.build(elements)
    buffer.seek(0)
    #수정중입니다 0821 1:07

    return buffer