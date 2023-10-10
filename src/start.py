import os
import logging
import chardet
import argparse
import report.report_analyzer as report_analyzer
import trade.trade_analyzer as trade_analyzer
import finance.irr as irr

logging.basicConfig(
    handlers=[
                logging.FileHandler(filename="runtime.log", encoding='utf-8', mode='a+')
             ],
    format="%(asctime)s %(name)s:%(levelname)s:%(filename)s:%(lineno)d：%(message)s",
    datefmt="%F %A %T",
    level=logging.INFO)

def detect_encoding(file):
    with open(file, 'rb') as f:
        content_bytes = f.read()
    detected = chardet.detect(content_bytes)
    encoding_format = detected['encoding']
    filename = os.path.basename(file)
    print(f"{filename} detected as {encoding_format}.")
    return encoding_format


def convert_to_utf8(filename):
    encoding_format = detect_encoding(filename)
    # strip blanks at the end of each line.

    with open(filename, 'r', encoding=encoding_format) as f:
        lines = f.readlines()
    with open(filename, 'w', encoding=encoding_format) as f:
        lines = map(lambda x: x.replace(' ', ''), lines)
        f.writelines(lines)

    # convert to utf-8
    if encoding_format == 'utf-8-sig' or encoding_format == 'UTF-8-SIG':
        return
    print(f"Converting {os.path.basename(filename)} to UTF-8...")
    with open(filename, 'r', encoding='gb2312') as f:
        content_text = f.read()
    with open(filename, 'w', encoding='utf-8-sig') as f:
        f.write(content_text)


def convert_file_format(file, keyword_list):
    if os.path.isfile(file):
        for keyword in keyword_list:
            if (keyword in file):
                convert_to_utf8(file)
    elif os.path.isdir(file):
        for filename in os.listdir(file):
            f = os.path.join(file, filename)
            convert_file_format(f, keyword_list)


def main():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    config_path = os.path.join(current_path, "data", "config")

    # 参数解析
    args = parse_args()

    if args.option == 'balance' or args.option == 'income' or args.option == 'cashflow':
        report_data_path = os.path.join(current_path, "data", "report")
        convert_file_format(report_data_path, args.stock)
        report_analyzer.ReportAnalyzer(args, report_data_path, config_path).start()
    elif args.option == 'trade':
        trade_data_path = os.path.join(current_path, "data", "trade")
        convert_file_format(trade_data_path, args.stock)
        trade_analyzer.TradeAnalyzer(args, trade_data_path).start()
    elif args.option == 'irr':
        irr.Irr(300000.0, 5*12, 0.003, 900).run()
    else:
        print("Invalid Option!")


def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-o", "--option", required=True,
                            choices=['balance', 'income', 'cashflow', 'trade', 'irr'],
                            help="options.")
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file",  # required=True,
                       help="file needed to be parsed.")
    group.add_argument("-s", "--stock", nargs='+',
                       help="support one or more stocks.")
    arg_parser.add_argument("-p", "--plot",
                            help="plot option.")
    arg_parser.add_argument("-sd", "--startdate",
                            help="specify the start date.")
    arg_parser.add_argument("-ed", "--enddate",
                            help="specify the end date.")

    return arg_parser.parse_args()


if __name__ == '__main__':
    main()
