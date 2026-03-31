def calculate_bmr(boy, kilo, yas, cinsiyet):
    if cinsiyet == 'Erkek':
        return 10 * kilo + 6.25 * boy - 5 * yas + 5
    elif cinsiyet == 'Kız':
        return 10 * kilo + 6.25 * boy - 5 * yas - 161
    else:
        raise ValueError("Cinsiyet bilgisi geçersiz")

def calculate_daily_calories(bmr, hedef):
    aktivite_carpani = 1.2
    kalori = bmr * aktivite_carpani
    if hedef == 'Kilo Vermek':
        kalori -= 500
    elif hedef == 'Kilo Almak':
        kalori += 500
    elif hedef == 'Kilo Korumak':
        pass
    else:
        raise ValueError("Hedef bilgisi geçersiz")
    return kalori

def calculate_macros(kalori):
    protein_pct = 0.25
    fat_pct = 0.25
    carb_pct = 0.50
    protein_gram = (kalori * protein_pct) / 4
    fat_gram = (kalori * fat_pct) / 9
    carb_gram = (kalori * carb_pct) / 4
    return protein_gram, fat_gram, carb_gram

def calculate_gramaj(hedef_miktar, besin_100g_miktar):
    if besin_100g_miktar > 0:
        return round((hedef_miktar / besin_100g_miktar) * 100, 1)
    else:
        return 0
    
def calculate_daily_calories(bmr, hedef, aktivite_seviyesi='düşük'):
    aktivite_dict = {
        'düşük': 1.2,
        'orta': 1.55,
        'yüksek': 1.9
    }
    if aktivite_seviyesi not in aktivite_dict:
        raise ValueError("Aktivite seviyesi geçersiz. Seçenekler: düşük, orta, yüksek")
    
    kalori = bmr * aktivite_dict[aktivite_seviyesi]
    if hedef == 'Kilo Vermek':
        kalori -= 500
    elif hedef == 'Kilo Almak':
        kalori += 500
    elif hedef == 'Kilo Korumak':
        pass
    else:
        raise ValueError("Hedef bilgisi geçersiz")
    return kalori
