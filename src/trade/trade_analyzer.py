import os
import pandas as pd
import matplotlib.pyplot as plt

class TradeAnalyzer(object):
    def __init__(self, args, data_path):
        filename = args.stock[0] + ".csv"
        self.datafile = os.path.join(data_path, filename)

        if (not os.access(self.datafile, os.R_OK)):
            print("Can't find {}...".format(self.datafile))
            os._exit(0)

        self.min_value_in_month_file = args.stock[0] + "_month_min.csv"
        self.max_value_in_month_file = args.stock[0] + "_month_max.csv"
        self.min_max_in_month_file =  args.stock[0] + "_month_min_max.csv"
        self.min_max_df = None

        self.start_date = args.startdate
        self.end_date = args.enddate

    def read_from_file(self):
        self.df = pd.read_csv(self.datafile,
                         encoding="utf-8-sig",
                         dayfirst=True,
                         usecols = ["日期", "收盘价"])
        self.df = self.df[self.df["收盘价"] > 0]
        print(self.df.dtypes)

    def output_to_file(self):
        df = self.df
        df["日期"] = pd.to_datetime(df["日期"])
        df["年"] = df["日期"].dt.year
        df["月"] = df["日期"].dt.month

        month_groups = df.groupby(["年", "月"])
        month_groups.min().reset_index().to_csv(self.min_value_in_month_file, sep=',', encoding='utf-8-sig')
        month_groups.max().reset_index().to_csv(self.max_value_in_month_file, sep=',', encoding='utf-8-sig')

        min_max_df = month_groups.min()
        min_max_df.rename(columns={'收盘价':'最低价'}, inplace=True)
        min_max_df['最高价'] = month_groups.max()['收盘价']
        min_max_df['日期'] = min_max_df['日期'].dt.to_period('M')
        min_max_df.to_csv(self.min_max_in_month_file, sep=',', encoding="utf-8-sig")
        min_max_df = min_max_df.set_index('日期', drop=True)
        self.min_max_df = min_max_df

        print(min_max_df)
        print(min_max_df.dtypes)

    def plot(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plot_df = self.min_max_df
        if self.start_date != None and self.end_date != None:
            plot_df = self.min_max_df[self.start_date:self.end_date]

        p = plot_df.plot()
        plt.show()

    def start(self):
        self.read_from_file()
        self.output_to_file()
        self.plot()
