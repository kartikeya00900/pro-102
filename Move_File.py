import os
import shutil


from_dir="C:/Users/karti/Downloads"

to_dir="C:/Users/karti/OneDrive/Documents"
list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == "":
        continue
    if extension in ['.txt','.doc1','.docx','.pdf']:
        path1=from_dir + "/"+file_name
        path2=to_dir + "/"+"Document_Files"
        path3=to_dir + "/"+"Document_Files"+"/"+file_name

        #print("Path1 ",path1)
        #print("Path3 ",path3)

        if os.path.exists(path2):
            print("Moving"+file_name+"...")

            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("Moving"+file_name+"...")
            shutil.move(path1,path3)    

     