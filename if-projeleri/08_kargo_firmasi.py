agirlik = float(input("Ağırlığı kilogram cinsinden giriniz: "))
mesafe = int(input("Mesafeyi kilometre olarak giriniz: "))
paket = input("Paket kırılabilir mi? (evet/hayır): ")

if agirlik <= 0 or mesafe <= 0:
    print("Geçersiz bilgi.")
else:
    a_uygun = agirlik <= 15 and mesafe <= 500

    b_uygun = (
        agirlik <= 20
        and mesafe <= 300
        and (agirlik <= 5 or paket == "hayır")
    )

    ucret1 = 40 + agirlik * 5
    ucret2 = 70 + agirlik * 2

    if a_uygun and b_uygun:
        if ucret1 <= ucret2:
            print("A firması seçildi. Ücret:", ucret1, "TL")
        else:
            print("B firması seçildi. Ücret:", ucret2, "TL")

    elif a_uygun:
        print("A firması seçildi. Ücret:", ucret1, "TL")

    elif b_uygun:
        print("B firması seçildi. Ücret:", ucret2, "TL")

    else:
        print("Gönderim yapılamaz.")