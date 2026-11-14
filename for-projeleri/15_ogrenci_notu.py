ogrenci_notu_sayisi=int(input("Kaç öğrencinin notunu gireceksiniz: "))
en_yuksek_not=-1
ilk_ogrenci_sirasi=0
en_yuksek_not_adedi=0

for i in range(1,ogrenci_notu_sayisi+1):
    ogrenci_notu=int(input(f"{i}. öğrencinin notunu giriniz: "))
    if ogrenci_notu > en_yuksek_not:
        en_yuksek_not=ogrenci_notu
        ilk_ogrenci_sirasi=i
        en_yuksek_not_adedi=1
    elif ogrenci_notu == en_yuksek_not:
        en_yuksek_not_adedi+=1

print("En yükseknot: ",en_yuksek_not)
print("İlk öğrencinin sırası: ",ilk_ogrenci_sirasi)
print("Bu notu alan öğrenci sayısı: ",en_yuksek_not_adedi)