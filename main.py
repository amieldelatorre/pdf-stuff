import PyPDF2
import sys
import os
import time
import argparse

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

    if args.merge != None and os.path.isdir(path) and search_string == None:
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        merge(path, output_file_name)
    elif args.merge != None and os.path.isdir(path) == False and search_string == None:
        print('Path must point to a folder if the -m option is being used!')
    elif args.merge == None and os.path.isfile(path) and search_string != None:
        search(path, search_string)
    elif args.merge == None and os.path.isfile(path) == False and search_string != None:
        print(os.path.isfile(path))
        print('Path must point to a pdf file if the -f option is being used!')
    elif args.merge != None and os.path.isdir(path) == False and search_string != None:
        print('Path must point to a folder if the -f and -m options are being used!')
    elif args.merge != None and os.path.isdir(path) and search_string != None:
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        merge(path, output_file_name)
        search(path + "/" + output_file_name, search_string)
    
    exit()

def merge(path, output_file_name):
    start = time.time()
    pdf_files = []

    for file_name in os.listdir(path):
        if file_name.endswith('.pdf'):
            pdf_files.append(file_name)
    
    pdf_files.sort(key = str.lower)

    writer = PyPDF2.PdfFileWriter()

    for file_name in pdf_files:
        file = open(path + '/' + file_name, 'rb')
        reader = PyPDF2.PdfFileReader(file)

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            writer.addPage(page)

    output_file = open(path + "/" + output_file_name, 'wb')
    writer.write(output_file)

    output_file.close()
    end = time.time()
    print('Done!')
    print('Time elapsed ==', end - start)
    print('The name of the merged file is', output_file_name)

    return


def search(path, search_string):
    search_string = search_string.lower()
    if path.endswith('.pdf') == False:
        print("The file referenced is not a pdf file.")
        exit()
    
    pages = []

    file = open(path, 'rb')
    reader = PyPDF2.PdfFileReader(file)

    for pageNum in range(reader.numPages):
        page = reader.getPage(pageNum)
        text = page.extractText().lower()
        if search_string.lower() in text:
            pages.append(pageNum + 1)
    
    print('The search word was:', search_string)
    print('The pages containing the word:', pages)
    print('The amount of pages containing th word:', len(pages))
    return

    
main()