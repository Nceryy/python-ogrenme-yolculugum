urun=int(input("Ürün saysını giriniz: "))
toplam=0
if urun <=0:
    print("Geçersiz ürün sayısı.")
else:
    for i in [24,6,1]:
        adet=urun//i
        urun-=i*adet
        print(i,"Kutu=",adet)
        toplam=toplam+adet
    print("Toplam:",toplam)

