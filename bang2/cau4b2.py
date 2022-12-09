import os
def  open_file():
    a = open('D:/hello.txt', encoding="utf-8")
    print(a.read())
    a.close()
open_file()