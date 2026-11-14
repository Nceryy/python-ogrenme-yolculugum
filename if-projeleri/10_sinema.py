age=int(input("Enter your age: "))
is_student=input("Are you a studen(evet/hayır): ")
is_3d=input("İs it 3D(evet/hayır): ")
budget=float(input("Enter your budget: "))
three_d=30
cocuk_bilet=80
ogr_bilet=100
temel_bilet=150

if age <0 or budget<0:
    print("Geçersiz bilgi.")

elif age<12 or age >=65:
    if is_3d == "evet" and budget<cocuk_bilet+three_d:
        budget=((budget)-(cocuk_bilet+three_d))*-1
        print("Bütçe yetersiz.","Eksik",budget)

    elif budget<cocuk_bilet:
        budget=((budget)-(cocuk_bilet))*-1
        print("Bütçe yetersiz.","Eksik:",budget)

    elif is_3d == "evet" and budget>=cocuk_bilet+three_d:
        cocuk_bilet+=three_d
        budget-=cocuk_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",cocuk_bilet,"Kalan bütçeniz:",budget)

    else:
        budget-=cocuk_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",cocuk_bilet,"Kalan bütçeniz:",budget)

elif is_student == "evet":
    if is_3d == "evet" and budget<ogr_bilet+three_d:
            budget=((budget)-(ogr_bilet+three_d))*-1
            print("Bütçe yetersiz.","Eksik:",budget)
    
    elif budget<ogr_bilet:
            budget=((budget)-(ogr_bilet))*-1
            print("Bütçe yetersiz.","Eksik:",budget,)

    elif is_3d == "evet" and budget >=ogr_bilet+three_d:
        ogr_bilet+=three_d
        budget-=ogr_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",ogr_bilet,"Kalan bütçeniz:",budget)

    else:
        budget-=ogr_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",ogr_bilet,"Kalan bütçeniz:",budget)

else:
    if is_3d == "evet" and budget<temel_bilet+three_d:
            budget=((budget)-(temel_bilet+three_d))*-1
            print("Bütçe yetersiz.","Eksik:",budget)
    
    elif budget<temel_bilet:
            budget=((budget)-(temel_bilet))*-1
            print("Bütçe yetersiz.","Eksik",budget)

    elif is_3d == "evet" and budget>= temel_bilet+three_d:
        temel_bilet+=three_d
        budget-=temel_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",temel_bilet,"Kalan bütçeniz:",budget)

    else:
        budget-=temel_bilet
        print("Bilet alınabilir.,","Bilet fiyatı:",temel_bilet,"Kalan bütçeniz:",budget)