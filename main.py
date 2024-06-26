import argparse


def checkbytes(filename: str) -> int:
    with open(filename, 'rb') as file:
        # Read the entire file content
        content = file.read()
        # Get the length of the content in bytes
        num_bytes = len(content)
    return num_bytes


def checklines(filename: str) -> int:
    num_lines = 0
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for _ in file:
            num_lines += 1
    return num_lines


def checkwords(filename: str) -> int:
    num_words = 0
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into words and count them
            words = line.split()
            num_words += len(words)
    return num_words


def checkcharacters(filename: str) -> int:
    num_characters = 0
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Add the length of the line to the character count
            num_characters += len(line)
    return num_characters


def checkdefault(filename: str) -> list:
    n_bytes = checkbytes(filename=filename)
    n_lines = checklines(filename=filename)
    n_words = checkwords(filename=filename)
    return [n_lines, n_words, n_bytes]


def main() -> None:
    parser = argparse.ArgumentParser(
                                    description="Count lines, words, "
                                                "or characters in a file.")
    parser.add_argument('filename',
                        type=str,
                        help='The file to process.'
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

    if args.lines:
        print(f"{checklines(args.filename)} {args.filename}")
    if args.words:
        print(f"{checkwords(args.filename)} {args.filename}")
    if args.characters:
        print(f"{checkcharacters(args.filename)} {args.filename}")

    # If no option is provided, count lines, words, and characters by default
    if not (args.lines or args.words or args.characters):
        print(f"{checklines(args.filename)} "
              f"{checkwords(args.filename)} {checkcharacters(args.filename)} "
              f"{args.filename}")


if '__main__' == __name__:
    main()
