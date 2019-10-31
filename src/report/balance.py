import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer


class BalanceSheetAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)
        self.read_data()

        self.asset_df = np.NaN
        self.debt_df = np.NaN
        self.equity_df = np.NaN

    def prepare(self):
        df = self.numberic_df

        self.overall_df = df.loc[['流动资产合计(万元)',
                                  '非流动资产合计(万元)',
                                  '资产总计(万元)',
                                  '流动负债合计(万元)',
                                  '非流动负债合计(万元)',
                                  '负债合计(万元)',
                                  '所有者权益(或股东权益)合计(万元)']]

        # 滤除资产部分的数据
        self.asset_df = df.loc[['货币资金(万元)',
                                '应收票据(万元)',
                                '应收账款(万元)',
                                '预付款项(万元)',
                                '其他应收款(万元)',
                                '存货(万元)',
                                '其他流动资产(万元)',
                                '长期股权投资(万元)',
                                '其他长期投资(万元)',
                                '固定资产(万元)',
                                '在建工程(万元)',
                                '无形资产(万元)',
                                '商誉(万元)',
                                '递延所得税资产(万元)',
                                '其他非流动资产(万元)']]
        # print(self.asset_df)

        # 滤除负债部分的数据
        self.debt_df = df.loc[['负债合计(万元)',
                               '短期借款(万元)',
                               '应付票据(万元)',
                               '应付账款(万元)',
                               '预收账款(万元)',
                               '应付职工薪酬(万元)',
                               '应付利息(万元)',
                               '其他应付款(万元)',
                               '一年内到期的非流动负债(万元)',
                               '其他流动负债(万元)',
                               '长期借款(万元)',
                               '应付债券(万元)',
                               '长期递延收益(万元)',
                               '递延所得税负债(万元)',
                               '其他非流动负债(万元)']]
        # print(self.debt_df)

        # 滤除股东权益部分的数据
        self.equity_df = df['实收资本(或股本)(万元)':'所有者权益(或股东权益)合计(万元)']
        # print(self.equity_df)

    def plot_asset(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 选择资产部分超过一定百分比的项目，并作图
        asset_rate = self.asset_df[:] / self.numberic_df.loc['资产总计(万元)']
        asset_rate = asset_rate[asset_rate[asset_rate.columns[0]] > 0.05]
        asset_rate = asset_rate.T

        # 选择负债部分超过一定百分比的项目，并作图
        debt_rate = self.debt_df[:] / self.numberic_df.loc['资产总计(万元)']
        debt_rate = debt_rate[debt_rate[debt_rate.columns[0]] > 0.05]
        debt_rate = debt_rate.T

        fig, axes = plt.subplots(nrows=2, ncols=1)
        ap = asset_rate.plot(ax=axes[0], figsize=(8,6))        
        ap.set_ylabel("百分比")
        ap_vals = ap.get_yticks()
        ap.set_yticklabels(['{:,.2%}'.format(x) for x in ap_vals])

        dp = debt_rate.plot(ax=axes[1], figsize=(8,6))
        dp.set_xlabel("日期")
        dp.set_ylabel("百分比")
        dp_vals = dp.get_yticks()
        dp.set_yticklabels(['{:,.2%}'.format(x) for x in dp_vals])

        fig_whole, axes_whole = plt.subplots(nrows=2, ncols=1)
        overall_df = self.overall_df
        overall_rate_df = self.overall_df[:] / self.overall_df.loc['资产总计(万元)']

        op = overall_df.T.plot(ax=axes_whole[0], figsize=(8,6))
        op.set_ylabel("数值")

        opr = overall_rate_df.T.plot(ax=axes_whole[1], figsize=(8,6))
        opr.set_xlabel("日期")
        opr.set_ylabel("数值")
        plt.show()

    def plot_liability(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']



    def analyze(self):
        self.prepare()
        self.plot_asset()
        self.plot_liability()
