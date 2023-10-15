import pandas as pd
import numpy as np


class Analyzer(object):
    def __init__(self, raw_data):
        self._raw_data = raw_data.set_index('报告日')
        self._numberic_df = pd.DataFrame()

    # 报表预处理时将其中包含'--'的字段统一替换为`0.0`
    def replace_to_zero(self, str):
        if '--' in str:
            return 0.0
        else:
            return str

    # 构建全新的年度数据用于计算
    # 1. 将没有3个有效数据（非NaN）的列视作无效列，丢弃
    # 2. 替换NaN为0，为后续数据统一类型做准备
    # 3. 将所有值转换为 float格式
    def convert_to_numeric(self, raw_df):
        #df = raw_df.dropna(axis=1, thresh=3).copy()
        print(raw_df.columns.values)
        df = raw_df.loc[:, ~raw_df.columns.isin(['数据源', '是否审计', '公告日期', '币种', '类型', '更新日期'])].copy()
        df.fillna(0, inplace=True)
        
        #df = df.applymap(self.replace_to_zero)
        for col in df:
            df[col] = pd.to_numeric(df[col])
        return df

    # 报表预处理，进行一些正式数据分析前的处理工作。
    def read_data(self):
        # 读取原始数据，并获取索引信息，用于之后的数据计算
        self._numberic_df = self.convert_to_numeric(self._raw_data)        

    def analyze(self):
        pass
