import argparse

def number_words(file):
    try:
        with open(file, 'r') as f:
            text = f.read()
            number_of_words = len(text.split())
            print(number_of_words)
    except FileNotFoundError:
        print(f'File "{file}" is not found...')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='filename', action='store', type=str)
    args = parser.parse_args()
    print(len(args.filename.split()))

if __name__ == "__task2__":
    main()

