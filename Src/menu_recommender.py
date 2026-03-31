import random
from googletrans import Translator


#translator = Translator()
#ceviri_cache = {}

#ef cevir_besin_adi(ingilizce_ad):
    #if ingilizce_ad in ceviri_cache:
        #return ceviri_cache[ingilizce_ad]
    #try:
        #turkce = translator.translate(ingilizce_ad, src='en', dest='tr').text
        #ceviri_cache[ingilizce_ad] = turkce
        #return turkce
    #except Exception:
        #return ingilizce_ad 

def calculate_gramaj(hedef_miktar, besin_100g_miktar):
    if besin_100g_miktar > 0:
        return round((hedef_miktar / besin_100g_miktar) * 100, 1)
    else:
        return 0

def recommend_menu(df, protein_hedef, yag_hedef, karb_hedef ):

    df_filtreli = df.copy()
    
    
    macro_groups = df_filtreli.groupby('class_label')

    menu = {'Kahvaltı': [], 'Öğle': [], 'Akşam': [], 'Ara Öğün': []}

    dagilim = {
        'Kahvaltı': {'protein': 0.3, 'fat': 0.25, 'carb': 0.3},
        'Öğle': {'protein': 0.3, 'fat': 0.35, 'carb': 0.35},
        'Akşam': {'protein': 0.3, 'fat': 0.3, 'carb': 0.3},
        'Ara Öğün': {'protein': 0.1, 'fat': 0.1, 'carb': 0.05},
    }

    for ogun, oranlar in dagilim.items():
        secilen_besinler = []
        for _ in range(2):
            if len(macro_groups) == 0:
                continue
            class_key = random.choice(list(macro_groups.groups.keys()))
            grup = macro_groups.get_group(class_key)
            besin = grup.sample(1).iloc[0]

            protein_gramaj = calculate_gramaj(protein_hedef * oranlar['protein'], besin['Protein'])
            fat_gramaj = calculate_gramaj(yag_hedef * oranlar['fat'], besin['Fat'])
            carb_gramaj = calculate_gramaj(karb_hedef * oranlar['carb'], besin['Carbohydrates'])

            gramajlar = [x for x in [protein_gramaj, fat_gramaj, carb_gramaj] if x > 0]
            gramaj = min(gramajlar) if gramajlar else 0

            secilen_besinler.append((besin['food'], gramaj))

        menu[ogun] = secilen_besinler

    return menu
def calculate_menu_totals(menu, df):
    toplam_kalori = 0
    toplam_protein = 0
    toplam_yag = 0
    toplam_karb = 0

    for ogun, besinler in menu.items():
        for besin_adi, gramaj in besinler:
            besin = df[df['food'] == besin_adi].iloc[0]
            toplam_kalori += besin['Caloric Value'] * gramaj / 100
            toplam_protein += besin['Protein'] * gramaj / 100
            toplam_yag += besin['Fat'] * gramaj / 100
            toplam_karb += besin['Carbohydrates'] * gramaj / 100

    return {
        'kalori': round(toplam_kalori, 2),
        'protein': round(toplam_protein, 2),
        'yag': round(toplam_yag, 2),
        'karb': round(toplam_karb, 2),
    }
def calculate_food_macros(menu, df):
    detaylar = []
    for ogun, besinler in menu.items():
        for besin_adi, gramaj in besinler:
            besin = df[df['food'] == besin_adi].iloc[0]
            detaylar.append({
                "Öğün": ogun,
                "Besin": besin_adi,
                "Gramaj": gramaj,
                "Kalori": round(besin['Caloric Value'] * gramaj / 100, 2),
                "Protein": round(besin['Protein'] * gramaj / 100, 2),
                "Yağ": round(besin['Fat'] * gramaj / 100, 2),
                "Karbonhidrat": round(besin['Carbohydrates'] * gramaj / 100, 2)
            })
    return detaylar

