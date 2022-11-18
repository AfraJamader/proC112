import os
import shutil

from_dir = "C:/Users/Dell/Downloads"
to_dir = "C:/Users/Dell/OneDrive/Pictures"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files :
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)

    if extension == ' ':
        continue

    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file
        path2 = to_dir + "/" + "image files"
        path3 = to_dir + "/" + "image files" + '/' + file

        print('path1 : ' , path1)
        print('path3 : ' , path3)      

        if os.path.exists(path2):
            print("moving " + file +".....")
            shutil.move(path1 , path3)

        else:
            os.makedirs(path2)
            print("moving " + file + ".....")
            shutil.move(path1 , path3)
