import os
import shutil

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('FilesToSort')
folders = ['doc', 'docx', 'png', 'gif', 'txt', 'xlsx', 'xls', 'jpg', 'other']
for folder in folders:
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except FileExistsError:
        print("File {:<5} already exists".format(folder))


for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        extension = filename.split('.')
        file_extension = extension[1]
        if 'docx' in file_extension:
            shutil.move(filename, 'docx')
        elif 'doc' in file_extension:
            shutil.move(filename, 'doc')
        elif 'png' in file_extension:
            shutil.move(filename, 'png')
        elif 'gif' in file_extension:
            shutil.move(filename, 'gif')
        elif 'txt' in file_extension:
            shutil.move(filename, 'txt')
        elif 'xlsx' in file_extension:
            shutil.move(filename, 'xlsx')
        elif 'xls' in file_extension:
            shutil.move(filename, 'xls')
        elif 'jpg' in file_extension:
            shutil.move(filename, 'jpg')
        else:
            shutil.move(filename, 'other')
print("All files moved to correct folders")

