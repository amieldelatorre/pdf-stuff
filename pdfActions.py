import PyPDF2
import sys, os, time, threading

def process_input(path, output_file_name, search_string):
    if path == "" or path == None: 
        print("Path cannot be none or empty string!")
        return
    
    if output_file_name == "":
        output_file_name = None
    if search_string == "":
        search_string = None

    if output_file_name != None and os.path.isdir(path) and search_string == None:
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        merge(path, output_file_name)
    elif output_file_name != None and os.path.isdir(path) == False and search_string == None:
        print('Path must point to a folder if the -m option is being used!')
    elif output_file_name == None and os.path.isfile(path) and search_string != None:
        search(path, search_string)
    elif output_file_name == None and os.path.isfile(path) == False and search_string != None:
        print(os.path.isfile(path))
        print('Path must point to a pdf file if the -f option is being used!')
    elif output_file_name != None and os.path.isdir(path) == False and search_string != None:
        print('Path must point to a folder if the -f and -m options are being used!')
    elif output_file_name != None and os.path.isdir(path) and search_string != None:
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        merge(path, output_file_name)
        search(path + "/" + output_file_name, search_string)
        
    return


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
    print('The name of the merged file is', output_file_name)
    print('Time elapsed ==', end - start)

    return


def search(path, search_string):
    start = time.time()
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
    
    end = time.time()

    print('The search word was:', search_string)
    print('The pages containing the word:', pages)
    print('The number of pages containing the word:', len(pages))
    print('Time elapsed ==', end - start)
    file.close()
    return