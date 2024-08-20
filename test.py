import pandas as pd
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# 한글 폰트 등록
pdfmetrics.registerFont(TTFont('MalgunGothic', 'malgun.ttf'))

# 엑셀 파일 읽기
excel_file = 'report_test1.xlsx'
df = pd.read_excel(excel_file)

# PDF 파일 설정
output_pdf = 'output.pdf'
pdf = SimpleDocTemplate(output_pdf, pagesize=A4)

# 스타일 설정
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Korean', fontName='MalgunGothic', fontSize=12))
style_normal = styles['Korean']

# 테이블 데이터 준비
data = [list(df.columns)]  # 엑셀 데이터의 헤더를 추가
for i in range(len(df)):
    data.append(list(df.iloc[i]))

# 테이블 생성
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'MalgunGothic'),  # 한글 폰트 설정
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

# PDF에 추가할 요소들
elements = []
elements.append(Paragraph('제품 데이터', style_normal))
elements.append(table)

# PDF 생성
pdf.build(elements)

print(f"PDF 파일이 {output_pdf}로 저장되었습니다.")
