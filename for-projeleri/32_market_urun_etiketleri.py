# Gerçek Hayat Problemi 5 - Market Ürün Etiketleri
# İlk ürün kodu ve ürün adedini alın. Her ürün kodunu yazdırın; kodu 5'e
# bölünenlere "- İndirimli" ekleyin. Sonda indirimli ürün sayısını gösterin.

ilk_urun_kodu=int(input("İlk ürün kodu: "))
urun_adedi=int(input("Ürün adedi: "))
indirimli_urun=0
for i in range(1,urun_adedi+1):
    if ilk_urun_kodu % 5 == 0:
        print("Ürün kodu: ",ilk_urun_kodu,"- İndirimli")
        indirimli_urun+=1
    else:
        print("Ürün kodu: ",ilk_urun_kodu)
    ilk_urun_kodu+=1

print("İndirimli ürün sayısı: ",indirimli_urun)
