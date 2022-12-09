import os
def xoa_file():
    os.remove('D:/filedelete.txt')
    print("delete file success")
def xoa_thu_muc():
    os.rmdir('D:/filedelete')
    print("delete file success ")
z1=xoa_thu_muc()
z2=xoa_file()