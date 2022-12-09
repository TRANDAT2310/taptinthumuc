import os
def cau_6():
    try:
        a = open('E:/hello.txt',encoding="utf-8")
        print(a.read())
    finally:
        a.close()
z=cau_6()