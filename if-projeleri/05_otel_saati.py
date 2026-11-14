saat=int(input("Saati giriniz: "))
bakim=input("Bakım yapılıyor mu(evet/hayır): ")
personel=input("Gelen kişi personel mi(evet/hayır): ")
rezervasyon=input("Rezervasyonu var mı(evet/hayır): ")

if saat <0 or saat >23:
    print("Geçersiz saat.")
elif bakim == "evet":
    print("Bakım nedeniyle kapalı.")
elif (bakim == "hayır") and (personel=="evet"):
    print("Personel girişi.")
elif (personel == "hayır" and rezervasyon == "evet") and ((saat >=20 and saat <=23)  or (saat >=0 and saat <=5)):
    print("Ziyaretçi girişi.")
else:
    print("Giriş reddedildi.")