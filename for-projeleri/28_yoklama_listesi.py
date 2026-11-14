# Gerçek Hayat Problemi 1 - Sınıf Yoklama Listesi
# Sınıf mevcudunu alıp her öğrenci için "Öğrenci No: X" yazdırın,
# sonda toplam öğrenci sayısını gösterin.

sinif_mevcudu=int(input("Sınıf mevcudunu giriniz: "))
no=1
for i in range(1,sinif_mevcudu+1):
    print("Öğrenci No:",no)
    no+=1

print("Yoklama listesi hazır.","Toplam öğrenci:",sinif_mevcudu)
