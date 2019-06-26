import os
import chardet
import argparse
import report.report_analyzer as report_analyzer
import trade.trade_analyzer as trade_analyzer

def detect_encoding(file):
    with open(file, 'rb') as f:
        content_bytes = f.read()

    detected = chardet.detect(content_bytes)
    encoding_format = detected['encoding']
    print(f"{file}: detected as {encoding_format}.")
    return encoding_format

def convert_to_utf8(filename):
    encoding_format = detect_encoding(filename)
    if encoding_format == 'utf-8-sig' or encoding_format == 'UTF-8-SIG':
        return

    with open(filename, 'r', encoding='gb2312') as f:
        content_text = f.read()

    with open(filename, 'w', encoding='utf-8-sig') as f:
        f.write(content_text)

def convert_file_format(file):
    if os.path.isfile(file):
        convert_to_utf8(file)
    elif os.path.isdir(file):
        for filename in os.listdir(file):
            f = os.path.join(file, filename)
            convert_file_format(f)

def main():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    config_path = os.path.join(current_path, "data", "config")

    # 参数解析
    args = parse_args()

    if args.option == 'balance' or args.option == 'income':
        report_data_path = os.path.join(current_path, "data", "report")
        convert_file_format(report_data_path)
        report_analyzer.ReportAnalyzer(args, report_data_path, config_path).start()
    elif args.option == 'trade':
        trade_data_path = os.path.join(current_path, "data", "trade")
        convert_file_format(trade_data_path)
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
