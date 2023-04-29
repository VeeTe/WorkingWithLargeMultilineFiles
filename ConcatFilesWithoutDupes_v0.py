import os
import argparse
import codecs
import chardet
import sys
from tqdm import tqdm

def detect_encoding(filename):
    # Determine the encoding of a file
    with open(filename, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]

def create_empty_file(filename):
    # Create an empty file using a system call
    if sys.platform == "win32":
        os.system(f"type nul > {filename}")
    else:
        os.system(f"touch {filename}")

def read_input_file(file_path, encoding):
    # Read the contents of an input file and return them as a list of words
    with codecs.open(file_path, "r", encoding=encoding, errors="ignore") as f:
        try:
            words = f.read().split()
        except UnicodeDecodeError:
            print(f"Unable to decode contents of {file_path}")
            return None
    return words

def compare_files(file1, file2, output_file):
    # Determine the encoding of each input file
    encoding1 = detect_encoding(file1)
    encoding2 = detect_encoding(file2)

    # Read the contents of each input file
    words1 = read_input_file(file1, encoding1)
    words2 = read_input_file(file2, encoding2)

    if words1 is None or words2 is None:
        return

    # Combine the words from both files and remove duplicates
    unique_words = set(words1 + words2)

    # Determine the encoding to use when writing the output file
    encoding = detect_encoding(output_file)

    # Create the output file
    create_empty_file(output_file)

    # Write the unique words to the output file
    with codecs.open(output_file, "w", encoding=encoding) as f:
        f.write("\n".join(unique_words))

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compare two text files and output a single file without duplicates")
    parser.add_argument("file1", help="Path to the first input file")
    parser.add_argument("file2", help="Path to the second input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    # Create the input and output files using system calls
    if sys.platform == "win32":
        os.system(f"type nul > {args.file1}")
        os.system(f"type nul > {args.file2}")
        os.system(f"type nul > {args.output_file}")
    else:
        os.system(f"touch {args.file1}")
        os.system(f"touch {args.file2}")
        os.system(f"touch {args.output_file}")

    # Compare the two files and output the result to a new file
    compare_files(args.file1, args.file2, args.output_file)

    # Print a message indicating that the output file was created
    print(f"Output written to {args.output_file}")

if __name__ == "__main__":
    main()

