import argparse


def parse_arg():
    parser = argparse.ArgumentParser(description="abc")
    parser.add_argument('--num', type=int, default=1)
    parser.add_argument('--gpu', type=str, default='0')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arg()
    print(args.num, args.gpu)