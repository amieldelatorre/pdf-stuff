import argparse
from pdfActions import process_input


def main():
    path = ""
    search_string = None
    output_file_name = None

    parser = argparse.ArgumentParser(description="Merge a folder's pdf files. Having both -m and -f arguments will find the string in the resulting merged file.")

    parser.add_argument('path', type=str, help='Path to folder or file.')
    parser.add_argument('-m', '--merge', type=str, help='Merge files in a folder. Please provide the file name to merge to.')
    parser.add_argument('-f', '--find', type=str, help='Find a specific string in a pdf. Please provide the string to search.')

    args = parser.parse_args()
    path = args.path
    search_string = args.find
    output_file_name = args.merge

    process_input(path, output_file_name, search_string)
    
    exit()

    
main()