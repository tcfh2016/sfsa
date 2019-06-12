import os
import pandas as pd

class TradeAnalyzer(object):
    def __init__(self, args):
        self.filename = args.stock + ".csv"
        if (not os.access(self.filename, os.R_OK)):
            print("Can't find {}...".format(self.filename))
            os._exit(0)

        self.min_value_in_month_file = args.stock + "_month_min.csv"
        self.max_value_in_month_file = args.stock + "_month_max.csv"
        self.min_max_in_month_file =  args.stock + "_month_min_max.csv"

        #self.start_date = None
        #self.end_date = None

    def read_from_file(self):
        self.df = pd.read_csv(self.filename,
                         encoding="gb2312",
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
        month_groups.min().reset_index().to_csv(self.min_value_in_month_file, sep=',', encoding='gb2312')
        month_groups.max().reset_index().to_csv(self.max_value_in_month_file, sep=',', encoding='gb2312')

        min_max_df = month_groups.min()
        min_max_df['最高价'] = month_groups.max()['收盘价']
        min_max_df.to_csv(self.min_max_in_month_file, sep=',', encoding='gb2312')

        #print(month_groups.min())
        #print(month_groups.max())
        print(min_max_df)
        print(month_groups)

    def plot(self):
        pass

    def start(self):
        self.read_from_file()
        self.output_to_file()
