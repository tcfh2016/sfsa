import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer

class BalanceSheetAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)

        self.asset_df = np.NaN
        self.debt_df = np.NaN
        self.equity_df = np.NaN

    def choose_items(self):
        # 选择最近一年 > 0的那些项目。
        df = self.numberic_df
        df = df[df[df.columns[0]] > 0]
        #print(df)

        # 滤除资产部分的数据
        self.asset_df = df['货币资金(万元)':'资产总计(万元)']
        #print(self.asset_df)
        # 滤除负债部分的数据
        self.debt_df = df['短期借款(万元)':'负债合计(万元)']
        #print(self.debt_df)
        # 滤除股东权益部分的数据
        self.equity_df = df['实收资本(或股本)(万元)':'所有者权益(或股东权益)合计(万元)']
        print(self.equity_df)

    def plot(self, percent_filter):
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 选择资产部分超过一定百分比的项目，并作图
        asset_df_percentage = self.asset_df[:] / self.asset_df.loc['资产总计(万元)']
        asset_df_forplot = asset_df_percentage[asset_df_percentage[asset_df_percentage.columns[0]] > percent_filter]
        asset_df_forplot = asset_df_forplot.T
        print(asset_df_forplot)
        ap = asset_df_forplot.plot()

        # 选择负债部分超过一定百分比的项目，并作图
        debt_df_percentage = self.debt_df[:] / self.debt_df.loc['负债合计(万元)']
        debt_df_forplot = debt_df_percentage[debt_df_percentage[debt_df_percentage.columns[0]] > percent_filter]
        debt_df_forplot = debt_df_forplot.T
        print(debt_df_forplot)
        dp = debt_df_forplot.plot()

        ap_vals = ap.get_yticks()
        ap.set_yticklabels(['{:,.2%}'.format(x) for x in ap_vals])
        ap.set_xticks(range(len(asset_df_forplot.index)))
        ap.set_xticklabels(asset_df_forplot.index, rotation=30)

        dp_vals = dp.get_yticks()
        dp.set_yticklabels(['{:,.2%}'.format(x) for x in dp_vals])
        dp.set_xticks(range(len(asset_df_forplot.index)))
        dp.set_xticklabels(asset_df_forplot.index, rotation=30)
        plt.show()

    def asset_estimate(self):
        #print(self.asset_df.loc['流动资产合计(万元)'])
        df_asset_es = pd.DataFrame(self.asset_df.loc['资产总计(万元)'])
        df_asset_es['存货(万元)'] = self.asset_df.loc['存货(万元)']
        df_asset_es['流动资产合计(万元)'] = self.asset_df.loc['流动资产合计(万元)']
        df_asset_es['负债合计(万元)'] = self.debt_df.loc['负债合计(万元)']
        df_asset_es['流动负债合计(万元)'] = self.debt_df.loc['流动负债合计(万元)']
        df_asset_es['实收资本(或股本)(万元)'] = self.equity_df.loc['实收资本(或股本)(万元)']

        # 营运资金
        df_asset_es['营运资金'] = df_asset_es['流动资产合计(万元)'] - df_asset_es['流动负债合计(万元)']
        # 酸性测试
        df_asset_es['酸性测试'] = ['True' if x>0 else 'False' for x in df_asset_es['营运资金'] - df_asset_es['存货(万元)']]
        # 每股清算价值 ~ 流动资产价值
        df_asset_es['流动资产价值'] = df_asset_es['营运资金'] / df_asset_es['实收资本(或股本)(万元)']
        # 每股账面价值
        df_asset_es['账面价值'] = (df_asset_es['资产总计(万元)'] - df_asset_es['负债合计(万元)']) / df_asset_es['实收资本(或股本)(万元)']
        # 资产负债率
        df_asset_es['资产负债率'] = (df_asset_es['负债合计(万元)'] / df_asset_es['资产总计(万元)'])
        df_asset_es.T.to_csv("assert_estimate.csv", sep=',', encoding='gb2312')
        print(df_asset_es.T)

    def proc(self):
        self.choose_items()
        self.plot(0.1)
        self.asset_estimate()
