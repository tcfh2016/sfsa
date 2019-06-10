import os
import report.balance as balance
import report.income as income

class ReportAnalyzer():
    def __init__(self, args):
        self.args = args
        self.balance_filename = "zcfzb" + args.stock + ".csv"
        self.income_filename = "lrb" + args.stock + ".csv"
        self.balance_df = None
        self.income_df = None

    def analize(self):
        if (self.args.option == 'balance'):
            self.balance_analyzer.analize()
        elif (self.args.option == 'income'):
            self.income_analyzer.analize()
        else:
            print("Invalid option !")

    def start(self):
        if os.access(self.balance_filename, os.R_OK) and os.access(self.income_filename, os.R_OK):
            self.balance_analyzer = balance.BalanceSheetAnalyzer(self.balance_filename)
            self.income_analyzer = income.IncomeStatementAnalyzer(self.income_filename)

            self.analize()
        else:
            print("Can't find {} and {}".format(self.balance_filename, self.income_filename))
            os._exit(0)
