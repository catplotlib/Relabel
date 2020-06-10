def change_name():
    import os
    from os import listdir
    variable=input("Enter new file names:\n")
    path = os.getcwd()
    i = 1
    for filename in listdir(path):
        m=filename.index('.')
        l=len(filename) 
        n=l-m
        if(variable==""):
            os.rename(filename,str(i).zfill(1)+filename[-n:])
        else:
            os.rename(filename,variable+ str(i).zfill(1)+filename[-n:])
        i+=1
