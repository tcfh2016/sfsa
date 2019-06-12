import argparse
import report.report_analyzer as report_analyzer
import trade.trade_analyzer as trade_analyzer

def main():
    args = parse_args()

    if args.option == 'balance' or args.option == 'income':
        report_analyzer.ReportAnalyzer(args).start()
    elif args.option == 'trade':
        trade_analyzer.TradeAnalyzer(args).start()
    else:
        print ("Invalid Option!")

def parse_args():
    arg_parser = argparse.ArgumentParser()

    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", #required=True,
                             help="file needed to be parsed.")
    group.add_argument("-s", "--stock", #required=True,
                             help="stock No.")
    arg_parser.add_argument("-o", "--option", required=True,
                             choices=['balance', 'income', 'trade'],
                             help="options.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()
