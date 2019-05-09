import argparse
import src.local as local

def main():
    opt = parse_args()
    p = local.Csv(opt)
    p.proc()

def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--file", required=True,
                        help="bin file which needed to be parsed.")

    return arg_parser.parse_args()

if __name__ == '__main__':
    main()
