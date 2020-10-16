#program Management kontak
import function

daftar_kontak = []
daftar_kontak.append ({
    "nama" : "erique",
    "telepon" : "08999461176"
})
 
# Menu Program
while True :
    print("-----------selamat datang------------")
    print("1. Daftar Kontak")
    print("2. Tammbah Kontak")
    print("0. Keluar program")

    menu = input("pilih menu :")

    if menu == "0":
        break
    elif menu == "1" :
        function.display_kontak(daftar_kontak)
    elif menu =="2" :
        kontak =  function.new_kontak()
        daftar_kontak.append(kontak)
    else :
        print("MENU NOT FOUND !!!! tekan 1 atau 2")

print("program selesai,Sanpai Jumpa")
