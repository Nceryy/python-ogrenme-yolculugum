para=int(input("Çekeceğiniz tutarı giriniz: "))

if para <100:
    print("Minimum para çekme tutarı 100 TL'dir.")
else:
    for deger in [200,100,50,20,10,5,1]:
        adet = para//deger
        para-=deger*adet
        print(deger,"TL'LİK",adet)