import os

#Dont execute this, was just for DEMONSTRATION
print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)
print(os.getcwd())
print(os.chdir('c:\\'))
print(os.getcwd())

# os.path.abspath() will pass the directory
os.path.abspath('spam.png')

#os.path.isabs will return true or false if it is a absolute path



