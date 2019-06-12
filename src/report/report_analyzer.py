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

    def estimate_profitability(self):
        income_es = pd.DataFrame(self.income_df.loc['营业利润(万元)'])
        income_es['资产总计(万元)'] = self.balance_df.loc['资产总计(万元)']
        income_es['净利润(万元)'] = self.income_df.loc['净利润(万元)']
        income_es['负债合计(万元)'] = self.balance_df.loc['负债合计(万元)']
        income_es['净资产(万元)'] = self.balance_df.loc['所有者权益(或股东权益)合计(万元)']

        income_es['总资产报酬率'] = income_es['营业利润(万元)'] / income_es['资产总计(万元)']
        income_es['净资产报酬率'] = income_es['净利润(万元)'] / income_es['净资产(万元)']
        income_es.T.to_csv("income_estimate.csv", sep=',', encoding='gb2312')
        print(income_es.T)

    def estimate_asset(self):
        #print(self.asset_df.loc['流动资产合计(万元)'])
        df_asset_es = pd.DataFrame(self.balance_df.loc['资产总计(万元)'])
        df_asset_es['存货(万元)'] = self.balance_df.loc['存货(万元)']
        df_asset_es['流动资产合计(万元)'] = self.balance_df.loc['流动资产合计(万元)']
        df_asset_es['负债合计(万元)'] = self.balance_df.loc['负债合计(万元)']
        df_asset_es['流动负债合计(万元)'] = self.balance_df.loc['流动负债合计(万元)']
        df_asset_es['实收资本(或股本)(万元)'] = self.balance_df.loc['实收资本(或股本)(万元)']

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

    def start(self):
        self.balance_df = self.balance_analyzer.numberic_df
        self.income_df = self.income_analyzer.numberic_df

        if (self.args.option == 'balance'):
            self.balance_analyzer.analize()
            self.estimate_asset()
        elif (self.args.option == 'income'):
            self.income_analyzer.analize()
            self.estimate_profitability()
        else:
            print("Invalid option !")
