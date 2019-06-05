import argparse
import local.balance as balance
import local.income as income
import local.csv as csv

def main():
    opt = parse_args()

    if opt.option == 'balance':
        par = balance.BalanceSheetAnalysis(opt)
        par.proc()
    elif opt.option == 'income':
        par = income.IncomeStatementAnalysis(opt)
        par.proc()
    elif opt.option == 'yieldcurve':
        p = csv.Csv(opt)
        p.proc()
    else:
        print ("Invalid Option!")

def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--file", required=True,
                        help="bin file which needed to be parsed.")
    arg_parser.add_argument("--option", required=True,
                        help="balance/yieldcurve/income.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()
