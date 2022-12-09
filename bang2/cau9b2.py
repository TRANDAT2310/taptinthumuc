import os
def open_file():
    a = open("D:/hello.txt","r")
    print(a.read())
    a.close()
open_file()