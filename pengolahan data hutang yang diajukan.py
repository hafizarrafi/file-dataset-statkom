import matplotlib.pyplot as plt

# Data yang diberikan
interval = ['3-52 * 100.000', '53-102 * 100.000 ', '103-152 * 100.000', '153-202 * 100.000', '203-252 * 100.000']
frekuensi = [491, 527, 545, 304, 133]
frek_kumulatif_lebih_kecil = [491, 1018, 1563, 1867, 2000]
frek_kumulatif_lebih_besar = [2000, 1867, 1563, 1018, 491]
frek_relatif = [24.55, 26.35, 27.25, 15.2, 6.65]
frek_relatif_kurang_dari = [24.55, 50.9, 78.15, 93.5, 100]
frek_relatif_lebih_dari = [100, 93.5, 78.15, 50.9, 24.55]

# Membuat diagram garis
plt.figure(figsize=(10, 6))
plt.plot(interval, frekuensi, marker='o', color='b', label='Frekuensi')
plt.plot(interval, frek_kumulatif_lebih_kecil, marker='o', color='g', label='Frek. Kumulatif (<)')
plt.plot(interval, frek_kumulatif_lebih_besar, marker='o', color='r', label='Frek. Kumulatif (>)')
plt.plot(interval, frek_relatif_kurang_dari, marker='o', linestyle='dashed', color='c', label='Frek. Relatif Kurang Dari (%)')
plt.plot(interval, frek_relatif_lebih_dari, marker='o', linestyle='dashed', color='m', label='Frek. Relatif Lebih Dari (%)')

# Menyertakan label sumbu x dan y, serta judul diagram
plt.xlabel('Interval')
plt.ylabel('Frekuensi / Frek. Kumulatif / Frek. Relatif (%)')
plt.title('Diagram Garis berdasarkan Interval')
plt.legend()
plt.grid(True, linestyle='--')

# Menampilkan diagram
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()