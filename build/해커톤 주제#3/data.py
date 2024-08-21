import pandas as pd

def process_data(file):
    df = pd.read_csv(file)
    df['Category'] = df['Category'].astype(str)
    return df