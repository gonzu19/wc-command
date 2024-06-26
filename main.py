import argparse
import sys


def checklines(file):
    num_lines = 0
    for _ in file:
        num_lines += 1
    return num_lines


def checkwords(file):
    num_words = 0
    for line in file:
        words = line.split()
        num_words += len(words)
    return num_words


def checkcharacters(file):
    num_characters = 0
    for line in file:
        num_characters += len(line)
    return num_characters


def main() -> None:
    parser = argparse.ArgumentParser(
                                    description="Count lines, words, "
                                                "or characters in a file.")
    parser.add_argument('filename',
                        type=str,
                        help='The file to process.',
                        nargs="?"
                        )
    parser.add_argument('-l',
                        '--lines',
                        action='store_true',
                        help='Count the number of lines.'
                        )
    parser.add_argument('-w',
                        '--words',
                        action='store_true',
                        help='Count the number of words.'
                        )
    parser.add_argument('-c',
                        '--characters',
                        action='store_true',
                        help='Count the number of characters.'
                        )

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r') as file:
            file_content = file.readlines()
    else:
        # Read from standard input
        file_content = sys.stdin.readlines()
        args.filename = ""

    if args.lines:
        print(f"{checklines(file_content)} {args.filename}")
    if args.words:
        print(f"{checkwords(file_content)} {args.filename}")
    if args.characters:
        print(f"{checkcharacters(file_content)} {args.filename}")

    # If no option is provided, count lines, words, and characters by default
    if not (args.lines or args.words or args.characters):
        print(f"{checklines(file_content)} "
              f"{checkwords(file_content)} {checkcharacters(file_content)} "
              f"{args.filename}")


if '__main__' == __name__:
    main()
