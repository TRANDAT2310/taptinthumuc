import os
def tap_tin_nhi_phan():
    a = open("C:\Users\FPTSHOP\OneDrive\Pictures\Saved Pictures\z3532680284218_c268c117a473c5fc776e815824e84e2e.jpg","wb")
    data=bytearray(" ghi nhị phân ".encode("ascii"))
    a.write(data)
    a.close()
    a = open("C:\Users\FPTSHOP\OneDrive\Pictures\Saved Pictures\z3532680284218_c268c117a473c5fc776e815824e84e2e.jpg","rb")
    print(a.read())
    a.close()
tap_tin_nhi_phan()