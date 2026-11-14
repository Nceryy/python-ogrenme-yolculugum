yas=int(input("Yaşınızı giriniz: "))
ogr=input("Öğrenci misiniz(evet/hayır): ")
dolap_kira=input("Dolap kiralanacak mı(evet/hayır): ")
budget=float(input("Bütçenizi giriniz: "))
ogr_bilet=80
temel_bilet=120
dolap_fiyat=20

if yas <0 or budget <0:
    print("Geçersiz bilgi.")
elif yas<16:
    print("Yaş nedeniyle giriş yapılamaz.")
else:
    if ogr == "evet" and budget <ogr_bilet:
        if dolap_kira == "evet":
            budget=(budget-(ogr_bilet+dolap_fiyat))*-1
            print("Bütçe yetersiz.","Eksik:",budget)
        else:
             budget=((budget-ogr_bilet)*-1)
             print("Bütçe yetersiz.","Eksik:",budget)

    elif ogr == "evet" and dolap_kira =="evet" and budget>=ogr_bilet+dolap_fiyat:
        ogr_bilet+=dolap_fiyat
        budget-=ogr_bilet
        print("Giriş yapabilir,","Toplam ücret:",ogr_bilet,"Kalan bütçeniz:",budget)
    elif ogr == "evet" and budget>=ogr_bilet:
        budget-=ogr_bilet
        print("Giriş yapabilir,","Toplam ücret:",ogr_bilet,"Kalan bütçeniz:",budget)
    
    else:
        if budget<temel_bilet:
            if dolap_kira == "evet":
                budget=((budget-(temel_bilet+dolap_fiyat))*-1)
                print("Bütçe yetersiz,","Eksik:",budget)
            else:
                budget=((budget-temel_bilet)*-1)
                print("Bütçe yetersiz,","Eksik:",budget)
        elif dolap_kira =="evet" and budget>=temel_bilet+dolap_fiyat:
            temel_bilet+=dolap_fiyat
            budget-=temel_bilet
            print("Giriş yapabilir,","Toplam ücret:",temel_bilet,"Kalan bütçeniz:",budget)
        elif budget>=temel_bilet:
            budget-=temel_bilet
            print("Giriş yapabilir,","Toplam ücret:",temel_bilet,"Kalan bütçeniz:",budget)
        
            
    