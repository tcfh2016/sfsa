import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer


class CashflowStatementAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)
        self.read_data()

        self.cashflow_df = np.NaN

    def prepare(self):
        self.cashflow_df = self.numberic_df.loc[['销售商品、提供劳务收到的现金(万元)',
                                                 '经营活动产生的现金流量净额(万元)',
                                                 '投资活动产生的现金流量净额(万元)',
                                                 '筹资活动产生的现金流量净额(万元)',
                                                 '现金及现金等价物净增加额(万元)',
                                                 '净利润(万元)']]

    def plot(self):
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        df = self.cashflow_df.T

        net_items = df[['经营活动产生的现金流量净额(万元)',
                        '投资活动产生的现金流量净额(万元)',
                        '筹资活动产生的现金流量净额(万元)',
                        '现金及现金等价物净增加额(万元)']]

        net_income_items = df[['经营活动产生的现金流量净额(万元)',
                               '净利润(万元)']]

        fig, axes = plt.subplots(nrows=2, ncols=1)
        net_plot = net_items.plot(ax=axes[0], figsize=(8, 6))
        net_plot.set_ylabel("数值")

        netincome_plot = net_income_items.plot(ax=axes[1], figsize=(8, 6))
        netincome_plot.set_ylabel("数值")
        netincome_plot.set_xlabel("日期")

        # plt.show()

    def analyze(self):
        self.prepare()
        self.plot()
