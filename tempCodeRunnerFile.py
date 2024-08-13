f = open('ok.txt')
print(f)

f = open('./15-File_handling/ok.txt', 'r')
txt = f.read()
print(txt)
f.close()