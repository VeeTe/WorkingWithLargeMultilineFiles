import os, argparse, sys
def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_file(file_path, content):
    """Writes the contents of a string to a file."""
    with open(file_path, 'w') as file:
        file.write(content)


def preprocess_text(text):
    """Converts the text to lowercase and removes duplicates."""
    text = text.lower()
    text = sanitize(text)
    unique_words = set(text.split())
    processed_text = '\n'.join(sorted(unique_words))
    return processed_text

strBadCharacters = '!@#$%^&*()+{}|:"<>?~`=[]\\;\',/'
def sanitize(strPassed):
    for strBadCharacter in strBadCharacters.split():
        if strBadCharacter in strPassed: strPassed = strPassed.replace(strBadCharacter,"")
    return strPassed

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compare two text files and output a single file without duplicates")
    parser.add_argument("input_file", help="Path to the second input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    # Create the input and output files using system calls
    if sys.platform == "win32":
        os.system(f"type nul > {args.input_file}")
        os.system(f"type nul > {args.output_file}")
    else:
        os.system(f"touch {args.input_file}")
        os.system(f"touch {args.output_file}")

    # Print a message indicating that the output file was created
    print(f"Output written to {args.output_file}")
    input_text = args.input_file
    output_text = args.output_file
    # Read the input file.
    input_text = read_file(input_text)

    # Preprocess the text.
    preprocessed_text = preprocess_text(input_text)

    # Write the preprocessed text to the output file.
    write_file(output_text, preprocessed_text)

if __name__ == "__main__":
    main()
