import argparse

def main():
    parser = argparse.ArgumentParser('Process some integers.')
    parser.add_argument('integer_1', help="an integer for the accumulator", type=int, )
    parser.add_argument('integer_2', help="an integer for the accumulator", type=int)

    args = parser.parse_args()
    answer = args.integer_1 + args.integer_2
    print(f'The sum of {args.integer_1} and {args.integer_2} is {answer}')


if __name__ == "__main__":
    main()

