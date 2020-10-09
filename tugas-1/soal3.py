#####program untuk menentukan apakah seorang siswa lulus atau tidak######
t = 69 #teori
p = 69 #praktek
kkm = 70 

if t >= kkm and p >= kkm :
    print ("selamat!,Anda lulus ujian")
elif t < kkm and p >= kkm :
    print ("anda harus mengulang ujian teori")
elif t >= kkm and p < kkm :
    print ("anda harus mengulan ujian  praktik")
elif t < kkm and p < kkm :
    print ("anda harus mengulang ujian teori dan praktek")

