import os
import argparse
import report.report_analyzer as report_analyzer
import trade.trade_analyzer as trade_analyzer

def main():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    args = parse_args()

    if args.option == 'balance' or args.option == 'income':
        report_data_path = os.path.join(current_path, "data", "report")
        report_analyzer.ReportAnalyzer(args, report_data_path).start()
    elif args.option == 'trade':
        trade_data_path = os.path.join(current_path, "data", "trade")
        trade_analyzer.TradeAnalyzer(args, trade_data_path).start()
    else:
        print ("Invalid Option!")

def parse_args():
    arg_parser = argparse.ArgumentParser()

    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", #required=True,
                             help="file needed to be parsed.")
    group.add_argument("-s", "--stock", nargs='+',
                             help="support one or more stocks.")

    arg_parser.add_argument("-o", "--option", required=True,
                             choices=['balance', 'income', 'trade'],
                             help="options.")
    arg_parser.add_argument("-p", "--plot",
                             help="plot option.")
    arg_parser.add_argument("-sd", "--startdate",
                             help="specify the start date.")
    arg_parser.add_argument("-ed", "--enddate",
                             help="specify the end date.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()
