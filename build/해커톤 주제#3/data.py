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

def process_4data(files):
    afs = []
    for file in files:
        if file.filename.startswith('결산_엑셀_2023'):
            af = pd.read_excel(file)
            afs.append(af)
    return afs

def process_5data(files):
    afs = []
    for file in files:
        if file.filename.startswith('결산_엑셀_2022'):
            af = pd.read_excel(file)
            afs.append(af)
    return afs

def process_6data(files):
    afs = []
    for file in files:
        if file.filename.startswith('고객사_인터뷰_데이터'):
            af = pd.read_excel(file)
            afs.append(af)
    return afs