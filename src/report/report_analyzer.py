import os
import pandas as pd
import report.balance as balance
import report.income as income

class ReportAnalyzer():
    def __init__(self, args):
        self.args = args
        self.balance_filename = "zcfzb" + args.stock + ".csv"
        self.income_filename = "lrb" + args.stock + ".csv"
        self.balance_df = None
        self.income_df = None

        if os.access(self.balance_filename, os.R_OK) and os.access(self.income_filename, os.R_OK):
            self.balance_analyzer = balance.BalanceSheetAnalyzer(self.balance_filename)
            self.income_analyzer = income.IncomeStatementAnalyzer(self.income_filename)
        else:
            print("Can't find {} and {}".format(self.balance_filename, self.income_filename))
            os._exit(0)

    def analize_profitability(self):
        income_es = pd.DataFrame(self.income_df.loc['营业利润(万元)'])
        income_es['资产总计(万元)'] = self.balance_df.loc['资产总计(万元)']
        income_es['净利润(万元)'] = self.income_df.loc['净利润(万元)']
        income_es['负债合计(万元)'] = self.balance_df.loc['负债合计(万元)']
        income_es['净资产(万元)'] = self.balance_df.loc['所有者权益(或股东权益)合计(万元)']

        income_es['总资产报酬率'] = income_es['营业利润(万元)'] / income_es['资产总计(万元)']
        income_es['净资产报酬率'] = income_es['净利润(万元)'] / income_es['净资产(万元)']
        income_es.T.to_csv("income_estimate.csv", sep=',', encoding='gb2312')
        print(income_es.T)

    def start(self):
        self.balance_df = self.balance_analyzer.numberic_df
        self.income_df = self.income_analyzer.numberic_df

        if (self.args.option == 'balance'):
            self.balance_analyzer.analize()
        elif (self.args.option == 'income'):
            self.income_analyzer.analize()
            self.analize_profitability()
        else:
            print("Invalid option !")
