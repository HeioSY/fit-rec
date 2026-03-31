import glob
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

def load_and_clean_data(path_pattern):
    files = glob.glob(path_pattern)
    if not files:
        raise FileNotFoundError(f"Dosya bulunamadı: {path_pattern}")
    df_list = [pd.read_csv(f) for f in files]
    df = pd.concat(df_list, ignore_index=True)
    df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], errors='ignore', inplace=True)
    cols = ['food', 'Caloric Value', 'Protein', 'Fat', 'Carbohydrates', 'Vitamin A', 'Vitamin C',
                 'Vitamin B1', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin B12']
    df = df[cols].dropna()
    return df

if __name__ == "__main__":
    print("Veri yükleniyor ve temizleniyor...")
    df = load_and_clean_data('C:/Users/tugru/OneDrive/Masaüstü/Diyet Karar Destek Sistemi/Data/FOOD-DATA-GROUP*.csv')
    print(f"Temizlenmiş veri satır sayısı: {len(df)}")

def add_macro_labels(df):
    def label_row(row):
        protein = row['Protein']
        fat = row['Fat']
        carb = row['Carbohydrates']
        protein_label = 1 if protein >= 15 else 0
        fat_label = 1 if fat >= 10 else 0
        carb_label = 1 if carb >= 20 else 0
        return fat_label * 4 + carb_label * 2 + protein_label
    df['class_label'] = df.apply(label_row, axis=1)
    return df

def train_decision_tree(df, model_path='models/decision_tree.pkl'):
    features = ['Protein', 'Fat', 'Carbohydrates']
    X = df[features]
    y = df['class_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)
    print(f"Model Test Doğruluğu: %{accuracy * 100:.2f}")

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    print(f"Model kaydedildi: {model_path}")
    return clf

    print("Etiketler ekleniyor...")
    df = add_macro_labels(df)
    print("Etiketler eklendi. Örnek:")
    print(df[['food', 'Protein', 'Fat', 'Carbohydrates', 'class_label']].head())

    print("Model eğitiliyor...")
    clf = train_decision_tree(df)
    print("Model eğitimi tamamlandı.")
