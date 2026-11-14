birinci_uzunluk=int(input("Üçgenin birinci uzunluğunu giriniz: "))
ikinci_uzunluk=int(input("Üçgenin ikinci uzunluğunu giriniz: "))
ucuncu_uzunluk=int(input("Üçgenin üçüncü uzunluğunu giriniz: "))

if  (birinci_uzunluk <=0 or ikinci_uzunluk <=0 or ucuncu_uzunluk <=0):
    print("Geçersiz uzunluk.")
elif not ((birinci_uzunluk+ikinci_uzunluk>ucuncu_uzunluk) and (ikinci_uzunluk+ucuncu_uzunluk>birinci_uzunluk) and (birinci_uzunluk+ucuncu_uzunluk>ikinci_uzunluk)):
    print("Üçgen oluşturulamaz.")
else:
    if birinci_uzunluk==ikinci_uzunluk==ucuncu_uzunluk:
        print("Eşkenar üçgen.")
    elif (birinci_uzunluk==ikinci_uzunluk) or (birinci_uzunluk==ucuncu_uzunluk) or (ikinci_uzunluk==ucuncu_uzunluk):
        print("İkizkenar üçgen.")
    else:
        print("Çeşitkenar üçgen.")