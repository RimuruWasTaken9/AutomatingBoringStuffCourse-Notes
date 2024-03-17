import shutil
'''
#everything in this will actually effect my computer, so its commented out
shutil.copy('c:\\spam.txt','c:\\delicious')#make a copy of a file/folder
#and put it in a specified spot
shutil.copy('c:\\spam.txt','c:\\delicious\\spamspamspam.txt')#this makes it
#so the copied file is also renamed to whatever is last
shutil.copytree('c:\\delicious','c:\\delicious_backup')#this makes a copy
#of a folder and everything in it and puts the copy in a specified spot
shutil.move('c:\\spam.txt','c:\\delicious\\walnut')#this moves the file
#to the specified spot
shutil.move('c:\\delicious\\walnut\\spam.txt','c:\\delicious\\walnut\\eggs.txt')
#to rename a file, you use the shutil.move but just change the last file name
'''
#New video
'''
import os
os.unlink('bacon.txt')#this is will delete a single file
os.rmdir('c:\\delicious')#this will remove a completely empty folder
shutil.rmtree('c:\\delicious')#this will remove a folder even if it has
#stuff inside it
for filename in os.listdir():
    if filename.endswith('.rxt'):#this is purposely misspelled for a dry test
        #os.unlink(filename)
        print(filename)
#this for loop looks for all the files in a folder and deletes any that
#end in '.rtx'
#all of these delete functions permanently delete files/folders, they don't
#just send them to the recycling bin

#there is an import that instead sends it to the recycling bin
import send2trash
send2trash.send2trash('c:\\users\rimuru\desktop\\IMPORTANTFILE.rxt')
#this would send the IMPORTANTFILE.rxt to the recycling bin
'''
#New video
import os
for folderName,subFolders,filenames in os.walk('c:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
    
