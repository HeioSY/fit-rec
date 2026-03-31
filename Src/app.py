import streamlit as st
from data_processing import load_and_clean_data, add_macro_labels
from calculations import calculate_bmr, calculate_daily_calories, calculate_macros
from menu_recommender import recommend_menu, calculate_gramaj, calculate_menu_totals, calculate_food_macros 
from vitamin_tracker import calculate_vitamin_intake, plot_vitamin_intake
from plots import plot_macro_progress
import matplotlib.pyplot as plt

def main():
    st.title("Fit-Reç")

    df = load_and_clean_data('C:/Users/tugru/OneDrive/Masaüstü/Diyet Karar Destek Sistemi/Data/FOOD-DATA-GROUP*.csv')
    df = add_macro_labels(df)

    boy = st.number_input("Boyunuz (cm)", 100, 250, 175)
    kilo = st.number_input("Kilonuz (kg)", 30, 200, 78)
    yas = st.number_input("Yaşınız", 10, 100, 25)
    cinsiyet = st.selectbox("Cinsiyetiniz", ["Erkek", "Kız"])
    hedef = st.selectbox("Hedefiniz", ["Kilo Vermek", "Kilo Korumak", "Kilo Almak"])


    if st.button("Menü Öner"):
        bmr = calculate_bmr(boy, kilo, yas, cinsiyet)
        kalori = calculate_daily_calories(bmr, hedef)
        protein, yag, karb = calculate_macros(kalori)

        st.write(f"BMR değeriniz: {bmr:.2f} kcal")
        st.write(f"Günlük kalori ihtiyacınız: {kalori:.2f} kcal")
        st.write(f"Protein: {protein:.2f} g, Yağ: {yag:.2f} g, Karbonhidrat: {karb:.2f} g")


        menu = recommend_menu(df, protein, yag, karb)

            

         # --- Yeni: Her besin için detaylar ---
        detaylar = calculate_food_macros(menu, df)
        st.markdown("### Seçilen Her Besinin Makro ve Kalorileri")
        st.dataframe(detaylar)  
        # ---------------------------
       
        toplamlar = calculate_menu_totals(menu, df)
        hedefler = {
            'kalori': kalori,
            'protein': protein,
            'yag': yag,
            'karb': karb
        }
        st.markdown("### Menüden Günlük Alacağınız Toplam Besin Değerleri")
        st.write(f"**Toplam Kalori:** {toplamlar['kalori']} kcal")
        st.write(f"**Toplam Protein:** {toplamlar['protein']} g")
        st.write(f"**Toplam Yağ:** {toplamlar['yag']} g")
        st.write(f"**Toplam Karbonhidrat:** {toplamlar['karb']} g")

        # --- Makro ve kalori ilerleme grafiği ---
        fig2 = plot_macro_progress(toplamlar, hedefler)
        st.pyplot(fig2)


        vitamin_rda = {
            'Vitamin A': 90,
            'Vitamin C': 90,
            'Vitamin B1': 1.2,
            'Vitamin B2': 1.3,
            'Vitamin B3': 16,
            'Vitamin B5': 5,
            'Vitamin B6': 1.3,
            'Vitamin B12': 2.4,
        }

        vitamin_totals = calculate_vitamin_intake(menu, df)

        fig, ax = plt.subplots(figsize=(10, 5))
        labels = list(vitamin_totals.keys())
        alinan = list(vitamin_totals.values())
        hedef = [vitamin_rda[vit] for vit in labels]

        ax.bar(labels, alinan, alpha=0.7, label='Alınan')
        ax.plot(labels, hedef, color='red', marker='o', linestyle='--', label='Günlük İhtiyaç')
        ax.set_ylabel('Vitamin Miktarı (mg veya µg)')
        ax.set_xticks(range(len(labels)))         
        ax.set_xticklabels(labels, rotation=45)
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
