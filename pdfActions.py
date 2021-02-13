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

    result = ""

    if output_file_name != None and os.path.isdir(path) and search_string == None:
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        result = merge(path, output_file_name)
    elif output_file_name != None and os.path.isdir(path) == False and search_string == None:
        result = 'Path must point to an existing folder!'
        print(result)
    elif output_file_name == None and os.path.isfile(path) and search_string != None:
        result = search(path, search_string)
    elif output_file_name == None and os.path.isfile(path) == False and search_string != None:
        result = 'Path must point to an existing pdf file!'
        print(result)
    elif output_file_name != None and os.path.isdir(path) == False and search_string != None:
        result = 'Path must point to an existing folder if merging and searching!'
        print(result)
    elif output_file_name != None and os.path.isdir(path) and search_string != None:
        print(output)
        if output_file_name.endswith('.pdf') == False:
            output_file_name += ".pdf"
        result = merge(path, output_file_name)
        result += search(path + "/" + output_file_name, search_string)
        
    return result


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
    result = 'Done!\n' + 'The name of the merged file is ' + output_file_name + ".\nTime taken to merge: " + str(round(end - start, 2)) + " seconds.\n"
    print(result)

    return result


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

    result = ('The search word was: ' + search_string + '.\nThe number of pages containing the word: ' + str(len(pages)) + '\nThe pages containing the word: ' + 
    ', '.join(str(e) for e in pages) + '\nTime taken for search: ' + str(round(end - start, 2)) + ' seconds.')
    print(result)
    file.close()
    return result