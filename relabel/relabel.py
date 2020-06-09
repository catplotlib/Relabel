def change_name():
    import os,sys
    from os import listdir
    class HiddenPrints:
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
            
    variable=input("Enter new file names:\n")
    with HiddenPrints():
        path = os.getcwd()
        i = 1
        for filename in listdir(path):
            if(variable==""):
                os.rename(filename,str(i).zfill(1)+filename[-4:])
                i+=1
            else:
                os.rename(filename,variable+ str(i).zfill(1)+filename[-4:])
                i+=1





"""import os
from os import listdir

def change_name():
    path = os.getcwd()
    i = 1
    for filename in listdir(path):
        if(variable==""):
            os.rename(filename,str(i).zfill(1)+filename[-4:])
            i+=1
        else:
            os.rename(filename,variable+ str(i).zfill(1)+filename[-4:])
            i+=1

variable=input("Enter new file names:\n")"""