def get_user_info():
    while True:
        try:
            boy = float(input("Boyunuzu cm cinsinden giriniz: "))
            if boy <= 0:
                print("Boy pozitif bir sayı olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    while True:
        try:
            kilo = float(input("Kilonuzu kg cinsinden giriniz: "))
            if kilo <= 0:
                print("Kilo pozitif bir sayı olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    while True:
        try:
            yas = int(input("Yaşınızı giriniz: "))
            if yas <= 0:
                print("Yaş pozitif bir tam sayı olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir tam sayı giriniz.")

    cinsiyet = ""
    while cinsiyet not in ("E", "K"):
        cinsiyet = input("Cinsiyetiniz (E/K): ").strip().upper()
        if cinsiyet not in ("E", "K"):
            print("Lütfen 'E' veya 'K' giriniz.")

    hedef = ""
    while hedef not in ("vermek", "korumak", "almak"):
        hedef = input("Hedefiniz nedir? (vermek/korumak/almak): ").strip().lower()
        if hedef not in ("vermek", "korumak", "almak"):
            print("Lütfen geçerli bir hedef giriniz: vermek, korumak, almak")

    return boy, kilo, yas, cinsiyet, hedef
