urun=int(input("Ürün saysını giriniz: "))

if urun <=0:
    print("Geçersiz ürün sayısı")
else:
    yirmidort=urun//24
    urun-=yirmidort*24

    alti=urun//6
    urun-=alti*6

    bir=urun//1

    print("Yirmi dört kutu:",yirmidort)
    print("Altı kutu:",alti)
    print("Bir kutu: ",bir)
    toplam=yirmidort+alti+bir
    print("Toplam kutu sayısı: ",toplam)