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
        print(self.income_df)

    def plot(self, percent_filter):
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
        print(value_items)

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
        print(percent_items)

        fig, axes = plt.subplots(nrows=2, ncols=1)
        value_items.plot(ax=axes[0])
        percent_items.plot(ax=axes[1])
        plt.show()

        '''
        income_plot = df_forplot.plot(figsize=(8,6))
        income_plot.set_xlabel("日期")
        income_plot.set_ylabel("百分比")
        vals = income_plot.get_yticks()
        income_plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
        income_plot.set_xticks(range(len(df_forplot.index)))
        income_plot.set_xticklabels(df_forplot.index, rotation=30)
        plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
        plt.show()
        '''

    def analyze(self):
        self.prepare()
        self.plot(0.05)
