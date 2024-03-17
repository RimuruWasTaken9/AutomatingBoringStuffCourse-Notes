Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\rimuru\MyPythonScripts\abswp10-3.py
c:\spam\eggs.png
c:\spam\eggs.png
folder1\folder2\folder3\folder4\file.png
folder1\folder2\folder3\folder4\file.png
C:\Users\rimuru\MyPythonScripts
None
c:\
C:\Users\rimuru\MyPythonScripts\spam.png
C:\Users\spam.png
True
rimuru\MyPythonScripts\spam.png
c:\folder1\folder2\folder3\folder4
file.png
folder4
False
True
4096
['abswp10-1.py', 'abswp10-2.py', 'abswp10-3.py', 'abswp9-24.py', 'abswp9-26.py', 'abswp9-28.py', 'abswp9-29.py', 'abswp9-30.py', 'cavegame.bat', 'cavegame.py', 'dreamcode9-25.bat', 'dreamcode9-25.py', 'hello.bat', 'hello.py', 'relearning9-25.py', 'relearning9-26.py']
39688

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========
Traceback (most recent call last):
  File "C:/Users/rimuru/MyPythonScripts/abswp10-4.py", line 5, in <module>
    open('c:\\users\\rimuru\\dreamcode.py')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\rimuru\\dreamcode.py'

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========
Traceback (most recent call last):
  File "C:/Users/rimuru/MyPythonScripts/abswp10-4.py", line 5, in <module>
    open('c:\\users\\rimuru\\MyPythonScripts\\dreamcode.py')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\rimuru\\MyPythonScripts\\dreamcode.py'

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========
helloFile = open('c:\\users\\rimuru\\hello.txt')

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========
helloFile.read()
''

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========
Traceback (most recent call last):
  File "C:/Users/rimuru/MyPythonScripts/abswp10-4.py", line 5, in <module>
    helloFile = open('c:\\users\\rimuru\\hello')
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\rimuru\\hello'

========= RESTART: C:/Users/rimuru/MyPythonScripts/abswp10-4.py =========

helloFile = open('c:\\users\\rimuru\\hello.txt')
helloFile.read()
SyntaxError: multiple statements found while compiling a single statement
helloFile = open('c:\\users\\rimuru\\hello.txt')
helloFile.read()
'Hello world!\nHow are you?'
helloFile.close()
content = helloFile.read()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    content = helloFile.read()
ValueError: I/O operation on closed file.
helloFile = open('c:\\users\\rimuru\\hello.txt')
content = helloFile.read()
print(content)
Hello world!
How are you?
helloFile.close()
helloFile = open('c:\\users\\rimuru\\hello.txt')
helloFile.readlines()
['Hello world!\n', 'How are you?']
helloFile.close()
helloFile = open('c:\\users\\rimuru\\hello.txt', 'w')
#write mode is 'w'
helloFile.close
<built-in method close of _io.TextIOWrapper object at 0x00000209B22EF100>
helloFile.close()
helloFile = open('c:\\users\\rimuru\\hello2.txt','w')
helloFile.write('Hello!!!!!!')
11
helloFile.write('Hello!!!!!!')
11
helloFile.write('Hello!!!!!!!')
12
#it will give you how many characters you wrote to it, ignore this tho
helloFile.close()
import shelve
#I didn't write about half of the stuff he showed, cuz it would've
#messed with my computer even more, go back to it if we need that shit
