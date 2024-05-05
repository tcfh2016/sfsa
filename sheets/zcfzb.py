import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sheet

class ZcfzbAnalyzer():
    def __init__(self, raw_data):
        self._numberic_df = sheet.convert_to_numeric(raw_data) 

        self.asset_df = np.NaN
        self.debt_df = np.NaN
        self.equity_df = np.NaN

    @property
    def numberic_df(self):
        return self._numberic_df

    def prepare(self):
        # 滤除主要项目
        self.overall_df = self._numberic_df[[
            '流动资产合计',
            '非流动资产合计',
            '资产总计',
            '流动负债合计',
            '非流动负债合计',
            '负债合计',
            '所有者权益(或股东权益)合计']]

        # 滤除资产部分的数据
        self.asset_df = self._numberic_df[[
            '货币资金',
            '应收票据',
            '应收账款',
            '预付款项',
            '其他应收款',
            '存货',
            '其他流动资产',
            '长期股权投资',
            '其他长期投资',
            '固定资产净额',
            '在建工程',
            '无形资产',
            '商誉',
            '递延所得税资产',
            '其他非流动资产']]
        print(self.asset_df)

        # 滤除负债部分的数据
        self.debt_df = self._numberic_df[[
            '负债合计',
            '短期借款',
            '应付票据',
            '应付账款',
            '预收款项',
            '应付职工薪酬',
            '应付利息',
            '其他应付款',
            '一年内到期的非流动负债',
            '其他流动负债',
            '长期借款',
            '应付债券',
            '长期递延收益',
            '递延所得税负债',
            '其他非流动负债']]
        # print(self.debt_df)

        # 滤除股东权益部分的数据
        self.equity_df = self._numberic_df.loc[:, '实收资本(或股本)':'所有者权益(或股东权益)合计']
        # print(self.equity_df)

    def plot_asset(self):
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 选择资产部分在最近一个报告期超过一定百分比的项目，先需要进行转置（T）来方便选择特定列
        temp_df = self.asset_df.T
        temp_df = temp_df[temp_df.iloc[:, 0] / self._numberic_df['资产总计'].iloc[0] >  0.05]
        asset_df = temp_df.T
        #print(asset_df)
        sheet.plot(asset_df) 

        asset_rate = self.asset_df[:].div(self._numberic_df['资产总计'], axis=0).T      
        asset_rate = asset_rate[asset_rate.iloc[:, 0] > 0.05].copy()
        asset_rate = asset_rate.T
        #print(asset_rate)
        sheet.plot(asset_rate, True)

        # 选择负债部分超过一定百分比的项目
        temp_df = self.debt_df.T
        temp_df = temp_df[temp_df.iloc[:, 0] / self._numberic_df['资产总计'].iloc[0] >  0.05]
        debt_df = temp_df.T
        #print(debt_df)
        sheet.plot(debt_df) 

        debt_rate = self.debt_df[:].div(self._numberic_df['资产总计'], axis=0).T
        debt_rate = debt_rate[debt_rate.iloc[:, 0] > 0.05].copy()
        debt_rate = debt_rate.T
        #print(debt_rate)
        sheet.plot(debt_rate, True)

    def estimate_asset(self):
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 1.流动资产检查
        current_asset = self._numberic_df[[
            '货币资金',
            '存货',
            '流动资产合计',
            '流动负债合计']]
        sheet.plot(current_asset)

        # 2.流动资产价值与账面价值
        current_asset_value = pd.DataFrame(self._numberic_df['实收资本(或股本)'])
        current_asset_value['每股流动资产价值'] = (self._numberic_df['流动资产合计'] - self._numberic_df['流动负债合计']) / self._numberic_df['实收资本(或股本)']
        book_value = self._numberic_df['归属于母公司股东权益合计'] - self._numberic_df['无形资产'] - self._numberic_df['商誉']
        current_asset_value['每股账面价值'] = book_value / self._numberic_df['实收资本(或股本)']
        del current_asset_value['实收资本(或股本)']
        sheet.plot(current_asset_value)

    def analyze(self):
        self.prepare()
        #self.plot_asset()
        self.estimate_asset()

if __name__ == "__main__":
    code = '002304' # 洋河股份
    zcfzb = ZcfzbAnalyzer(sheet.Sheet(code).zcfzb)
    zcfzb.analyze()