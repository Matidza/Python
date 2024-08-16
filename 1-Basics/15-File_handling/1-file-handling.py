# File Handing
'''
in python we see data in different datatypes
usually in different file format. in addition to 
to handling files, we can also save data in other file types like 
['.txt', '.csv', '.json', '.xml', '.excel']

File handling is useful since we can Create, Read, Update
and Delete files
'''
# To HANDLE data in python, we use open(), a built-in function

'''
Syntax: open('filename', mode)

mode(r,a,w,x,t,b)
r = Read
a = Append
w = write
x =create
t = text- text mode
b = binary eg. images
'''

# Open files for reading

f = open('ok.txt')
print(f)

f = open('./15-File_handling/ok.txt', 'r')
txt = f.read()
print(txt)
f.close()