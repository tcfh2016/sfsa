import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sheet
from sheet import convert_to_numeric


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

class LrbAnalyzer():
    def __init__(self, raw_lrb):
        self._income_df = convert_to_numeric(raw_lrb)        

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

    def plot(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        df = self._df.copy()

        df['营业费用'] = df['销售费用'] + df['管理费用'] + df['财务费用']
        df['核心利润'] = df['营业总收入'] - df['营业总成本']
        df['毛利润'] = df['营业收入'] - df['营业成本']

        # Two sub-diagrames are needed: value and percentage
        # 1. 数值
        #   - 营业总收入
        #   - 营业收入
        #   - 营业成本
        #   - 营业费用
        #   - 核心利润
        #   - 营业利润
        value_items = df[[
            '营业总收入',
            '营业收入',
            '营业成本',
            '营业费用',
            '核心利润',
            '营业利润',
            '净利润']]
        print(value_items)

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
        print(percent_items)

        fig, axes = plt.subplots(nrows=2, ncols=1)
        value_plot = value_items.plot(ax=axes[0], figsize=(8, 6))
        value_plot.set_ylabel("数值")
        value_plot.legend(value_items.columns)

        percent_plot = percent_items.plot(ax=axes[1], figsize=(8, 6))
        percent_plot.set_xlabel("日期")
        percent_plot.set_ylabel("百分比")
        vals = percent_plot.get_yticks()
        percent_plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
        percent_plot.legend(percent_items.columns)

    def analyze(self):        
        self.plot()

if __name__ == "__main__":
    code = '002304' # 洋河股份
    zcfzb = LrbAnalyzer(sheet.Sheet(code).lrb)
    zcfzb.analyze()