import matplotlib.pyplot as plt

# Data yang diberikan
interval = ['2- 5 bulan', '6-9 bulan ', '10-13 bulan', '14-17 bulan', '18-21 bulan']
frekuensi = [391, 440, 409, 376, 384]
frek_kumulatif_lebih_kecil = [391, 831, 1340, 1616, 2000]
frek_kumulatif_lebih_besar = [2000, 1616, 1340, 831, 391]
frek_relatif = [19.55, 22, 20.45, 18.8, 19.2]
frek_relatif_kurang_dari = [19.55, 41.55, 62, 80.8, 100]
frek_relatif_lebih_dari = [100, 80.8, 62, 41.55, 19.55]

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