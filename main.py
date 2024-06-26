def checkbytes(filename: str) -> int:
    with open(filename, 'rb') as file:
        # Read the entire file content
        content = file.read()
        # Get the length of the content in bytes
        num_bytes = len(content)
    return num_bytes

def main() -> None:
    pass

if '__main__' == __name__:
    main()  
