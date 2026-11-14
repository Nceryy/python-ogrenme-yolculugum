sensor1 = int(input("1. sensörün ölçümü: "))
sensor2 = int(input("2. sensörün ölçümü: "))
sensor3 = int(input("3. sensörün ölçümü: "))

if (sensor1 < 0 or sensor1 > 100
    or sensor2 < 0 or sensor2 > 100
    or sensor3 < 0 or sensor3 > 100):
    print("Geçersiz ölçüm.")

else:
    fark12 = abs(sensor1 - sensor2)
    fark13 = abs(sensor1 - sensor3)
    fark23 = abs(sensor2 - sensor3)

    if fark12 <= 5 and fark13 <= 5 and fark23 <= 5:
        sonuc = (sensor1 + sensor2 + sensor3) / 3
        print("Üç sensör kullanıldı. Sonuç:", sonuc)

    elif fark12 > 5 and fark13 > 5 and fark23 > 5:
        print("Yeniden ölçüm gerekli.")

    elif fark12 <= fark13 and fark12 <= fark23:
        sonuc = (sensor1 + sensor2) / 2
        print("1 ve 2 kullanıldı. Sonuç:", sonuc)

    elif fark13 <= fark23:
        sonuc = (sensor1 + sensor3) / 2
        print("1 ve 3 kullanıldı. Sonuç:", sonuc)

    else:
        sonuc = (sensor2 + sensor3) / 2
        print("2 ve 3 kullanıldı. Sonuç:", sonuc)