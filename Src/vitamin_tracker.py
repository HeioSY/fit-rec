import matplotlib.pyplot as plt

def calculate_vitamin_intake(menu, df):
    vitamin_cols = ['Vitamin A', 'Vitamin C', 'Vitamin B1', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin B12']
    vitamin_totals = {vit: 0 for vit in vitamin_cols}

    for ogun, besinler in menu.items():
        for besin_adi, gramaj in besinler:
            besin = df[df['food'] == besin_adi].iloc[0]
            for vit in vitamin_cols:
                vitamin_miktar = besin[vit] * gramaj / 100
                vitamin_totals[vit] += vitamin_miktar

    return vitamin_totals

def plot_vitamin_intake(vitamin_totals, vitamin_rda):
    labels = list(vitamin_totals.keys())
    alinan = list(vitamin_totals.values())
    hedef = [vitamin_rda[vit] for vit in labels]

    plt.clf()
    plt.figure(figsize=(12,6))
    plt.bar(labels, alinan, alpha=0.7, label='Alınan')
    plt.plot(labels, hedef, color='red', marker='o', linestyle='--', label='Günlük İhtiyaç')
    plt.xticks(ticks=range(len(labels)), labels=labels, rotation=45)
    plt.ylabel('Vitamin Miktarı (mg veya µg)')
    plt.title('Günlük Vitamin Alım Takibi')
    plt.legend()
    plt.tight_layout()
    plt.show()

