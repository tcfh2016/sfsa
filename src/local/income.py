import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import local.common as common

class IncomeStatementAnalysis(object):
    def __init__(self, opt):
        self.filename = opt.file
        self.numberic_df = np.NaN
        self.income_df = np.NaN

    def get_numberic_sheet(self):
        # 读取原始数据，并获取索引信息，用于之后的数据计算
        df = pd.read_csv(self.filename, encoding="gb2312", index_col = 0, header = 0,
                         dtype=np.object)
        #print(df)
        self.numberic_df = common.convert_to_numeric(df)
        print(self.numberic_df)

    def calc_percentage(self):
        self.get_numberic_sheet()

        df = self.numberic_df['营业总收入(万元)':'净利润(万元)']
        #df = df[df['2018-12-31'] > 0]，这种方式与下面这种方式等价
        df = df[df[df.columns[0]] > 0]
        print(df)
        self.income_df = df

    def plot(self, percent_filter):
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 选择资产部分超过一定百分比的项目，并作图
        df_percentage = self.income_df[:] / self.income_df.loc['营业总收入(万元)']
        df_forplot = df_percentage[df_percentage[df_percentage.columns[0]] > percent_filter]
        df_forplot = df_forplot.T
        print(df_forplot)

        income_plot = df_forplot.plot()

        # 设置纵坐标显示百分比，横坐标标签倾斜以便展示完全。
        vals = income_plot.get_yticks()
        income_plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
        income_plot.set_xticks(range(len(df_forplot.index)))
        income_plot.set_xticklabels(df_forplot.index, rotation=30)
        plt.show()

    def income_estimate(self):
        income_es = pd.DataFrame(self.numberic_df.loc['营业利润(万元)'])

    def proc(self):
        self.calc_percentage()
        self.plot(0.05)
        self.income_estimate()
