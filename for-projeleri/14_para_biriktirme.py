biriktirilecek_gun=int(input("Kaç gün para biriktireceksiniz: "))
hedef_tutari=int(input("Hedef tutarı: "))
birikim=0
toplam=0
ilk_ulasma_gunu=0
for i in range (1,biriktirilecek_gun+1):
    biriktirilen_para=int(input(f"{i}. gün ne kadar biriktirdiniz: "))
    toplam+=biriktirilen_para
    if toplam >=hedef_tutari:
        if ilk_ulasma_gunu == 0:
            ilk_ulasma_gunu=i
            print(f"{ilk_ulasma_gunu}. gün hedefe ulaşıldı.")
    elif toplam <hedef_tutari:
        eksik=hedef_tutari-toplam
        
        print("Hedefe ulaşılamadı,eksik tutar: ",eksik)
print("Toplam birikim: ",toplam)
