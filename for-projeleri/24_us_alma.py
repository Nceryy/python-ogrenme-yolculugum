# Uygulama Sorusu 12 (Orta-zor)
# Kullanıcıdan taban ve üs alın. ** operatörünü kullanmadan, for döngüsü ve
# çarpma ile üssü hesaplayın. Her adımda ara sonucu yazdırın.

taban=int(input("Tabanı giriniz: "))
us=int(input("Üsü giriniz: "))
carpim=1
if us == 0:
    carpim=1

for i in range(1,us+1):
        carpim*=taban
        print(f"{i}. adim:",carpim)

print("Sonuç:",carpim)
