# PDF Stuff

## Description
A program that will be used to collate pdfs, mainly for the purpose of mashing together lecture pdfs and making searches easier.


## Installation
```shell
cd pdf-stuff
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Program
If you want to merge pdf files, this program merges all the files in a folder, sorted by name.

If you are searching, it gives back pages containing the string.

### Using Command Line Interface

```shell
python cli.py [-h] [-m MERGE] [-f FIND] path
```
*-h* : is for help and shows what each option does.   

*path* : required, path to the folder or file.

*-m* : add the name of the file you want it to be named if you are merging, using this alone requires path to be pointing to a folder.

*-f* : search string for the pdf, using it alone requires path to be pointing to a file.

You can have both -m and -f options, but path must point to a folder.

### Using GUI
```shell
python kivyGui.py
```
*Path* : required, path to the folder or file.  

*Output File Name* : add the name of the file you want it to be named if you are merging, using this alone requires path to be pointing to a folder.

*Search* : search string for the pdf, using it alone requires path to be pointing to a file.

You can have both Output File Name and Search, but path must point to a folder.