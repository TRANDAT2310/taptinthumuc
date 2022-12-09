import os
def open_file():
    a = open("D:/hello.txt","w",encoding="utf-8")
    a.write("hello\n")
    a.write("hello\n")
    a.write("bingchiling \n")
    a.close()
open_file()