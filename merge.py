import os;
from PyPDF2 import PdfMerger;


cwd = os.getcwd()

print("Th Current working directory is: {0}".format(cwd))

dirList = []
fList = []


def getList(list):
    for filename in os.scandir(cwd):
        f = os.path.join(cwd, filename)
        # checking if it is a dir
        if filename.is_dir():
            list.append(f)


getList(dirList)

for i in dirList:
    print(i)

for dir in dirList:
    merger = PdfMerger()
    cwd = os.chdir(dir)
    cwd = os.getcwd()

    for filename in os.listdir(cwd):
        merger.append(filename)
       
        print (filename)
    
    merger.write(f"{os.path.basename(dir)}.pdf")
    merger.close()
    print("--------------------------")
   




