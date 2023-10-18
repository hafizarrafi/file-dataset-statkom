import matplotlib.pyplot as plt

# Data yang diberikan
interval = ['0-19', '20-39', '40-59', '60-79', '80-99']
frekuensi = [619, 637, 459, 229, 56]
frek_kumulatif_lebih_kecil = [619, 1256, 1715, 1944, 2000]
frek_kumulatif_lebih_besar = [2000, 1944, 1715, 1256, 619]
frek_relatif = [30.95, 31.85, 22.94, 11.45, 2.8]
frek_relatif_kurang_dari = [30.95, 62.8, 85.75, 97.2, 100]
frek_relatif_lebih_dari = [100, 97.2, 85.75, 62.8, 30.95]

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