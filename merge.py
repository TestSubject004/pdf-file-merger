import os;
from PyPDF2 import PdfMerger,PdfFileReader, PdfReader;
from PyPDF2.errors import PdfReadError;
import pathlib



cwd = os.getcwd()

print("Th Current working directory is: {0}".format(cwd))



def procDir():
    
    flist=[]
    for filename in os.scandir(cwd):
        f = os.path.join(cwd, filename)
      
        if filename.is_file() and filename.name.endswith('.pdf'):
            
            
            flist.append(filename.name)
            print(filename.name)
                
            
    if flist:
        merger = PdfMerger()
        for lis in flist:
            merger.append(lis)        
        merger.write(f"{os.path.basename(cwd)}.pdf")
        merger.close()
    print("--------------------------")
    return getList()


def getList():
    dirList=[]
    for filename in os.scandir(cwd):
        
        f = os.path.join(cwd, filename)
        # checking if it is a dir
        if filename.is_dir():
            dirList.append(f)
    if dirList:
        return dirList
    else:
        return None




def exec():
    global cwd
    abc = procDir()
    
    if abc:
        for dir in abc:
            os.chdir(dir)
            cwd = os.getcwd()
            exec()
    else:
        return
        
            
    
    
exec ()






