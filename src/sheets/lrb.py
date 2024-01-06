import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sheet

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

class LrbAnalyzer():
    def __init__(self, raw_lrb):
        self._income_df = sheet.convert_to_numeric(raw_lrb)        

        # Prepared items to be displayed
        # 1. 营业总收入
        # 2. 营业收入
        # 3. 营业成本
        # 4. 营业费用 （销售费用、管理费用、财务费用）
        # 5. 核心利润 （营业总收入 - 营业总成本）
        # 6. 营业利润 （营业总收入 - 营业总成本 + 其他收益）
        # 7. 净利润 （营业利润 + 营业外收支 - 税收）
        self._df = self._income_df[[
            '营业总收入',
            '营业收入',
            '营业总成本',
            '营业成本',
            '销售费用',
            '管理费用',
            '财务费用',
            '营业利润',
            '净利润']]
        print(self._df)

    @property
    def numberic_df(self):
        return self._income_df
    
    def plot_df(self, values, percent = False):
        fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True)
        df = values.T

        s_1st = df.loc[:, df.columns.str.contains('0331')].T
        plot = s_1st.plot(ax=axes[0, 0], figsize=(8, 6))
        
        s_2nd = df.loc[:, df.columns.str.contains('0630')].T
        plot = s_2nd.plot(ax=axes[0, 1], figsize=(8, 6))

        s_3rd = df.loc[:, df.columns.str.contains('0930')].T
        plot = s_3rd.plot(ax=axes[1, 0], figsize=(8, 6))

        s_4st = df.loc[:, df.columns.str.contains('1231')].T
        plot = s_4st.plot(ax=axes[1, 1], figsize=(8, 6))
        plot.legend(s_4st.columns)

        if percent:
            vals = plot.get_yticks()
            plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

    def plot(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        df = self._df.copy()

        df['营业费用'] = df['销售费用'] + df['管理费用'] + df['财务费用']
        df['核心利润'] = df['营业总收入'] - df['营业总成本']
        df['毛利润'] = df['营业收入'] - df['营业成本']

        value_items = df[[
            '营业总收入',
            '营业收入',
            '营业成本',
            '营业费用',
            '核心利润',
            '营业利润',
            '净利润']]
        self.plot_df(value_items)        

        # 2. 百分比
        #   - 毛利率
        #   - 费用率 （营业费用 / 营业收入）
        #   - 核心利润率 （核心利润 / 营业收入）
        #   - 营业利润率 （营业利润 / 营业收入）
        percent_items = df[[
            '营业收入',
            '毛利润',
            '营业费用',
            '核心利润',
            '营业利润',
            '净利润']]
        percent_items = percent_items[:].div(percent_items['营业收入'], axis=0)
        percent_items = percent_items.iloc[:, 1:]        
        self.plot_df(percent_items, True)

    def analyze(self):
        self.plot()

if __name__ == "__main__":
    code = '002304' # 洋河股份
    zcfzb = LrbAnalyzer(sheet.Sheet(code).lrb)
    zcfzb.analyze()