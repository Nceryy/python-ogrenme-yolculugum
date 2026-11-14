# Uygulama Sorusu 15 (Zorlayıcı - Final)
# Hedef tutar ve ay sayısını alın. Her ay biriktirilen parayı (küsuratlı olabilir)
# isteyip ay sonu toplamını yazdırın. Sonda en çok biriktirilen ayı ve miktarını,
# hedefe ilk ulaşılan ayı (ya da "Hedefe ulaşılamadı") yazdırın.

hedef_tutari=float(input("Hedef tutarını giriniz: "))
kac_ay=int(input("Kaç ay biriktiriceksiniz: "))

toplam=0
en_cok_biriktirilen_para=0
en_cok_biriktirilen_ay=0
hedefe_ulasilan_ay=0

for i in range(1,kac_ay+1):
    para=float(input(f"{i}. ay ne kadar biriktirdiniz: "))
    toplam+=para

    if i == 1:
        en_cok_biriktirilen_para = para
        en_cok_biriktirilen_ay = i

    if para > en_cok_biriktirilen_para:
        en_cok_biriktirilen_para = para
        en_cok_biriktirilen_ay = i


    if toplam >= hedef_tutari and hedefe_ulasilan_ay == 0:
        hedefe_ulasilan_ay = i

    print(f"{i}. ay sonu toplam:",toplam)

if toplam >= hedef_tutari:
    print("En çok biriktirilen ay:",en_cok_biriktirilen_ay,"(",en_cok_biriktirilen_para,")")
    print("Hedefe ilk ulaşılan ay:",hedefe_ulasilan_ay)
else:
    print("En çok biriktirilen ay:",en_cok_biriktirilen_ay,"(",en_cok_biriktirilen_para,")")
    print("Hedefe ulaşılamadı")
