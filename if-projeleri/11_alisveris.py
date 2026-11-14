purchase_amount = float(input("Alışveriş tutarı: "))
is_member = input("Üye misiniz? (evet/hayır): ")
has_coupon = input("Kuponunuz var mı? (evet/hayır): ")

if purchase_amount <= 0:
    print("Geçersiz tutar.")

else:
    member_discount = 0
    coupon_discount = 0

    if is_member == "evet":
        member_discount = purchase_amount * 20 / 100

    if has_coupon == "evet" and purchase_amount >= 400:
        coupon_discount = 100

    if member_discount >= coupon_discount:
        discount = member_discount
    else:
        discount = coupon_discount

    discounted_amount = purchase_amount - discount

    if discounted_amount >= 500:
        shipping_fee = 0
    else:
        shipping_fee = 40

    total_payment = discounted_amount + shipping_fee

    print("İndirim tutarı:", discount, "TL")
    print("Kargo ücreti:", shipping_fee, "TL")
    print("Ödenecek toplam:", total_payment, "TL")