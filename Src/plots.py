import matplotlib.pyplot as plt

def plot_macro_progress(toplamlar, hedefler):
    """
    toplamlar: dict, örn: {'kalori': 1522, 'protein': 87, 'yag': 56, 'karb': 167}
    hedefler: dict, örn: {'kalori': 2000, 'protein': 120, 'yag': 70, 'karb': 250}
    """
    labels = ['Kalori', 'Protein', 'Yağ', 'Karbonhidrat']
    alinan = [toplamlar['kalori'], toplamlar['protein'], toplamlar['yag'], toplamlar['karb']]
    hedef = [hedefler['kalori'], hedefler['protein'], hedefler['yag'], hedefler['karb']]

    progress = [a/h if h>0 else 0 for a, h in zip(alinan, hedef)]

    fig, ax = plt.subplots(figsize=(8,4))
    bars = ax.barh(labels, progress, color=['#90ee90' if p>=1 else '#ffdb58' for p in progress])
    ax.set_xlim(0, 1.2)
    ax.set_xlabel("Hedefe Ulaşma Oranı (%)")
    ax.set_title("Günlük Makro ve Kalori Hedefi İlerlemesi")

    # Oranların üzerine değerleri yaz
    for i, (p, a, h) in enumerate(zip(progress, alinan, hedef)):
        ax.text(min(p,1) + 0.05, i, f"{a:.0f} / {h:.0f}", va='center', fontsize=11)

    # Kırmızı çizgi: 100% hedef
    ax.axvline(1, color='red', linestyle='--', label='Günlük Hedef')
    ax.legend()
    plt.tight_layout()
    return fig
