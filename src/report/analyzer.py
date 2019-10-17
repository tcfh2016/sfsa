import pandas as pd
import numpy as np


class Analyzer(object):
    def __init__(self, file_name):
        self.filename = file_name

    # 报表预处理时将其中包含'--'的字段统一替换为`0.0`
    def replace_to_zero(self, str):
        if '--' in str:
            return 0.0
        else:
            return str

    # 构建全新的年度数据用于计算
    # 1. 将包含超过3个 NaN的列视作无效列，丢弃
    # 2. 替换`--`为0，为后续数据统一类型做准备
    # 3. 将所有值转换为 float格式
    def convert_to_numeric(self, raw_df):
        df = raw_df.dropna(axis=1, thresh=3)
        df = df.applymap(self.replace_to_zero)
        for col in df:
            df[col] = pd.to_numeric(df[col])
        return df

    # 报表预处理，进行一些正式数据分析前的处理工作。
    def read_data(self):
        # 读取原始数据，并获取索引信息，用于之后的数据计算
        df = pd.read_csv(self.filename,
                         encoding='utf-8-sig',
                         index_col=0,
                         header=0,
                         dtype=np.object)
        # print(df)
        self.numberic_df = self.convert_to_numeric(df)
        # print(self.numberic_df)

    def analyze(self):
        pass
