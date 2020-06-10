def change_name():
    import os,sys
    from os import listdir
    variable=input("Enter new file names:\n")
    path = os.getcwd()
    i = 1
    for filename in listdir(path):
        if(variable==""):
            os.rename(filename,str(i).zfill(1)+filename[-4:])
            i+=1
        else:
            os.rename(filename,variable+ str(i).zfill(1)+filename[-4:])
            i+=1


