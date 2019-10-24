import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer


class IncomeStatementAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)
        self.read_data()

        self.income_df = np.NaN

    def prepare(self):
        # Prepared items to be displayed
        # 1. 营业总收入
        # 2. 营业收入
        # 3. 营业成本
        # 4. 营业费用 （销售费用、管理费用、财务费用）
        # 5. 核心利润 （营业总收入 - 营业总成本）
        # 6. 营业利润 （营业总收入 - 营业总成本 + 其他收益）
        # 7. 净利润 （营业利润 + 营业外收支 - 税收）
        self.income_df = self.numberic_df.loc[['营业总收入(万元)',
                                               '营业收入(万元)',
                                               '营业总成本(万元)',
                                               '营业成本(万元)',
                                               '销售费用(万元)',
                                               '管理费用(万元)',
                                               '财务费用(万元)',
                                               '营业利润(万元)',
                                               '净利润(万元)']]
        # print(self.income_df)

    def plot(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        df = self.income_df.T
        df['营业费用(万元)'] = df['销售费用(万元)'] + \
                              df['管理费用(万元)'] + \
                              df['财务费用(万元)']
        df['核心利润(万元)'] = df['营业总收入(万元)'] - df['营业总成本(万元)']
        df['毛利润(万元)'] = df['营业收入(万元)'] - df['营业成本(万元)']

        # Two sub-diagrames are needed: value and percentage
        # 1. 数值
        #   - 营业总收入
        #   - 营业收入
        #   - 营业成本
        #   - 营业费用
        #   - 核心利润
        #   - 营业利润
        value_items = df[['营业总收入(万元)',
                          '营业收入(万元)',
                          '营业成本(万元)',
                          '营业费用(万元)',
                          '核心利润(万元)',
                          '营业利润(万元)',
                          '净利润(万元)']]
        # print(value_items)

        # 2. 百分比
        #   - 毛利率
        #   - 费用率 （营业费用 / 营业收入）
        #   - 核心利润率 （核心利润 / 营业收入）
        #   - 营业利润率 （营业利润 / 营业收入）
        percent_items = df[['营业收入(万元)',
                            '毛利润(万元)',
                            '营业费用(万元)',
                            '核心利润(万元)',
                            '营业利润(万元)',
                            ]]
        percent_items = percent_items[:].div(percent_items['营业收入(万元)'], axis=0)
        percent_items = percent_items.ix[:, 1:]
        # print(percent_items)

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
        self.prepare()
        self.plot()
