import argparse
import local.balance_sheet as balance_sheet
import local.csv as csv

def main():
    opt = parse_args()

    if opt.option == 'balancesheet':
        par = balance_sheet.BalanceSheetAnalysis(opt)
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
                        help="balancesheet/yieldcurve.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()
