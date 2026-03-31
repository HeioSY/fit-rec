from data_processing import load_and_clean_data, add_macro_labels, train_decision_tree
from user_input import get_user_info
from calculations import calculate_bmr, calculate_daily_calories, calculate_macros
from menu_recommender import recommend_menu
from vitamin_tracker import calculate_vitamin_intake, plot_vitamin_intake

def main():
    df = load_and_clean_data('data/FOOD-DATA-GROUP*.csv')
    df = add_macro_labels(df)
    
    clf = train_decision_tree(df)
    
    boy, kilo, yas, cinsiyet, hedef = get_user_info()
    
    bmr = calculate_bmr(boy, kilo, yas, cinsiyet)
    kalori = calculate_daily_calories(bmr, hedef)
    protein, yag, karb = calculate_macros(kalori)
    
    print(f"\nBMR: {bmr:.2f} kcal")
    print(f"Günlük Kalori İhtiyacı: {kalori:.2f} kcal")
    print(f"Protein: {protein:.2f} g, Yağ: {yag:.2f} g, Karbonhidrat: {karb:.2f} g")
    
    menu = recommend_menu(df, protein, yag, karb)
    
    for ogun, besinler in menu.items():
        print(f"\n{ogun}:")
        for besin, gramaj in besinler:
            print(f" - {besin}: {gramaj} gram")
    
    # Örnek vitamin RDA değerleri (mg veya µg cinsinden)
    vitamin_rda = {
        'Vitamin A': 900,
        'Vitamin C': 90,
        'Vitamin B1': 1.2,
        'Vitamin B2': 1.3,
        'Vitamin B3': 16,
        'Vitamin B5': 5,
        'Vitamin B6': 1.3,
        'Vitamin B12': 2.4,
    }
    
    vitamin_totals = calculate_vitamin_intake(menu, df)
    plot_vitamin_intake(vitamin_totals, vitamin_rda)

if __name__ == "__main__":
    main()
