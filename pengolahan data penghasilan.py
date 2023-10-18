import matplotlib.pyplot as plt

# Data yang diberikan
interval = ['2-14 * 100.000', '5-27 * 100.000 ', '28-40 * 100.000', '41-53 * 100.000', '54-66 * 100.000']
frekuensi = [378, 390, 405, 435, 392]
frek_kumulatif_lebih_kecil = [378, 768, 1173, 1608, 2000]
frek_kumulatif_lebih_besar = [2000, 1608, 1173, 768, 378]
frek_relatif = [18.9, 19.5, 20.25, 21.75, 19.6]
frek_relatif_kurang_dari = [18.9, 38.4, 58.65, 80.4, 100]
frek_relatif_lebih_dari = [100, 80.4, 58.65, 38.4, 18.9]

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