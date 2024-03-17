print('c:\\spam\\eggs.png')
print(r'c:\spam\eggs.png')

x ='\\'.join(['folder1','folder2','folder3','folder4','file.png'])
print(x)

import os
os.path.join('folder1','folder2','folder3','folder4','file.png')
print(os.path.join('folder1','folder2','folder3','folder4','file.png'))

#directory is just an old name for folder

print(os.getcwd())
print(os.chdir('c:\\'))
print(os.getcwd())
"""
'spam.png' is a relative file path
absolute file paths always begins with the root folder (c drive), giving the
full path to the file
relative file paths can also begin with other folders

to call for a regular path, put .\ in front of the relative path if you
are in the directory right above the folder/file
this .\ is also optional and you can just begin with the file name if you
are in the right cd.
if you want to reference a file/folder in a directory above your cd,
you need to put ..\ instead.
EASIER WAY TO THINK OF IT: the . represents "this folder" and
the .. represents "the parent folder"
"""
os.chdir('C:\\Users\\rimuru\\MyPythonScripts')

print(os.path.abspath('spam.png'))#will return a string of the absolute path
#that you give it
print(os.path.abspath('..\\..\\spam.png'))
print(os.path.isabs('C:\\Users\\rimuru\\MyPythonScripts'))


print(os.path.relpath('C:\\Users\\rimuru\\MyPythonScripts\\spam.png','\
C:\\Users'))

print(os.path.dirname('c:\\folder1\\folder2\\folder3\\folder4\\file.png'))
print(os.path.basename('c:\\folder1\\folder2\\folder3\\folder4\\file.png'))
print(os.path.basename('c:\\folder1\\folder2\\folder3\\folder4'))
#dirname pulls off everything upto the file in the filepath
#basename pulls off the last file/folder in the filepath

print(os.path.exists('c:\\folder1\\folder2\\folder3\\folder4\\file.png'))
print(os.path.exists('C:\\Users\\rimuru\\MyPythonScripts'))
#this one looks if its a real path name on our computer

#there is also os.path.isfile and os.path.isdir that act as true or false
#if the last thing in the path is a file or folder respectively

print(os.path.getsize('C:\\Users\\rimuru\\MyPythonScripts'))
#returns how big the file is in bytes

print(os.listdir('C:\\Users\\rimuru\\MyPythonScripts'))

totalSize = 0 #this for loop will find out the total size of all files in MyPythonScripts
for filename in os.listdir('C:\\Users\\rimuru\\MyPythonScripts'):
    if not os.path.isfile(os.path.join('C:\\Users\\rimuru\\MyPythonScripts', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\rimuru\\MyPythonScripts', filename))
 

print(totalSize)

#os.makedirs('c:\\onedream\\onewish\\randomjapanese\\overthetop')
#^^^DON'T uncomment, will create 4 different folders on my actual computer

#don't worry about memorizing all of these, just know they exist and look up
#what each of them do again when we need it

