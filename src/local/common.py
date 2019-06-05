import pandas as pd

def replace_to_zero(str):
    if '--' in str:
        return 0.0
    else:
        return str

def convert_to_numeric(raw_df):
    # 构建全新的年度数据用于计算
    # 1. 将包含超过3个 NaN的列视作无效列，丢弃
    # 2. 替换`--`为0，为后续数据统一类型做准备
    # 3. 将所有值转换为 float格式
    df = raw_df.dropna(axis=1, thresh=3)
    df = df.applymap(replace_to_zero)
    for col in df:
        df[col] = pd.to_numeric(df[col])
    return df
