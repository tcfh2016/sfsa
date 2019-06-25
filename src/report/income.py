import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer

class IncomeStatementAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)
        self.pre()

        self.income_df = np.NaN

    def prepare(self):
        # 滤除利润相关项目
        self.income_df = self.numberic_df['营业总收入(万元)':'净利润(万元)']

    def plot_profit(self, percent_filter):
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 选择资产部分超过一定百分比的项目，并作图
        df_percentage = self.income_df[:] / self.income_df.loc['营业总收入(万元)']
        df_forplot = df_percentage[df_percentage[df_percentage.columns[0]] > percent_filter]
        df_forplot = df_forplot.T
        print(df_forplot)

        income_plot = df_forplot.plot(figsize=(8,6))
        income_plot.set_xlabel("日期")
        income_plot.set_ylabel("百分比")
        vals = income_plot.get_yticks()
        income_plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
        income_plot.set_xticks(range(len(df_forplot.index)))
        income_plot.set_xticklabels(df_forplot.index, rotation=30)
        plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
        plt.show()

    def ratio_analyze(self):
        self.prepare()
        self.plot_profit(0.05)
