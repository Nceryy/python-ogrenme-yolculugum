kullanim_suresi=int(input("Kullanım süresini giriniz: "))
kulaklik_kiralanacak=input("Kulaklık kiralanacak mı(evet/hayır): ")
butce=float(input("Bütçenizi giriniz: "))

if kullanim_suresi <1 or kullanim_suresi >8 or butce <0:
    print("Geçersiz bilgi.")
else:
    saatlik_ucret=50 #max 200
    kulaklik_kira=30
    if kulaklik_kiralanacak == "evet":
        toplam_odeme=(saatlik_ucret*kullanim_suresi)

        if toplam_odeme >=200:
            toplam_odeme=200+kulaklik_kira  
            if butce<toplam_odeme:
                eksik=toplam_odeme-butce
                print("Bütçe yetersiz.","Eksik:",eksik)
            else:
                butce-=toplam_odeme
                print("Toplam ödeme:",toplam_odeme,"Kalan bütçeniz",butce)
       
        else:
            if butce < toplam_odeme+kulaklik_kira:
                toplam_odeme+=kulaklik_kira
                eksik=toplam_odeme-butce
                print("Bütçe yetersiz.","Eksik:",eksik)
            else:
                toplam_odeme+=kulaklik_kira
                butce-=toplam_odeme
                print("Toplam ödeme:",toplam_odeme,"Kalan bütçeniz",butce)

    else:
        toplam_odeme=(saatlik_ucret*kullanim_suresi)

        if toplam_odeme >=200:
            toplam_odeme=200
            if butce < toplam_odeme:
                eksik=toplam_odeme-butce
                print("Bütçe yetersiz.","Eksik:",eksik)

            else:
                butce-=toplam_odeme
                print("Toplam ödeme:",toplam_odeme,"Kalan bütçeniz",butce)
                
        else:
            if butce < toplam_odeme:
                eksik=toplam_odeme-butce
                print("Bütçe yetersiz.","Eksik:",eksik)
            else:
                butce-=toplam_odeme
                print("Toplam ödeme:",toplam_odeme,"Kalan bütçeniz",butce)

