import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# masukkan data interval, frekuensi, frek kumulatif < dan >, 
# frek relatif, dan frek relatif kumulatif < dan>
interval = ['0-19', '20-39', '40-59', '60-79', '80-99']
frekuensi = [619, 637, 459, 229, 56]
frek_kumulatif_lebih_kecil = [619, 1256, 1715, 1944, 2000]
frek_kumulatif_lebih_besar = [2000, 1944, 1715, 1256, 619]
frek_relatif = [30.95, 31.85, 22.94, 11.45, 2.8]
frek_relatif_kurang_dari = [30.95, 62.8, 85.75, 97.2, 100]
frek_relatif_lebih_dari = [100, 97.2, 85.75, 62.8, 30.95]

# Membuat dataframe dari data untuk tabel
data = {
    'Interval': interval,
    'Frekuensi': frekuensi,
    'Frek. Kumulatif (<)': frek_kumulatif_lebih_kecil,
    'Frek. Kumulatif (>)': frek_kumulatif_lebih_besar,
    'Frek. Relatif (%)':frek_relatif,
    'Frek. Relatif Kurang Dari (%)': frek_relatif_kurang_dari,
    'Frek. Relatif Lebih Dari (%)': frek_relatif_lebih_dari,
}
#dataframe disimpan
df = pd.DataFrame(data)

# Menampilkan tabel data dengan pembatas kolom dan baris menggunakan tabulate
table = tabulate(df, headers='keys', tablefmt='pretty', showindex=False)

# Menampilkan diagram garis
plt.figure(figsize=(12, 6))

#dikarenakan ada 2 bentuk satuan data, maka dipisahkan sesuai satuannya
#menjadi 2 kelompok

# Kelompok 1: Frekuensi, Frek. Kumulatif (<), dan Frek. Kumulatif (>)
plt.subplot(121)  # Subplot 1
plt.plot(interval, frekuensi, marker='o', color='b', label='Frekuensi')
plt.plot(interval, frek_kumulatif_lebih_kecil, marker='o', color='g', label='Frek. Kumulatif (<)')
plt.plot(interval, frek_kumulatif_lebih_besar, marker='o', color='r', label='Frek. Kumulatif (>)')
plt.xlabel('Interval')
plt.ylabel('Frekuensi / Frek. Kumulatif')
plt.title('Kelompok 1')
plt.legend()
plt.grid(True, linestyle='--')

# Kelompok 2: Frek. Relatif Kurang Dari (%) dan Frek. Relatif Lebih Dari (%)
plt.subplot(122)  # Subplot 2
plt.plot(interval, frek_relatif, marker='o', linestyle='dashed', color='c', label='Frek. Relatif(%)')
plt.plot(interval, frek_relatif_kurang_dari, marker='o', linestyle='dashed', color='c', label='Frek. Relatif Kurang Dari (%)')
plt.plot(interval, frek_relatif_lebih_dari, marker='o', linestyle='dashed', color='m', label='Frek. Relatif Lebih Dari (%)')
plt.xlabel('Interval')
plt.ylabel('Frek. Relatif (%)')
plt.title('Kelompok 2')
plt.legend()
plt.grid(True, linestyle='--')

# Menampilkan tabel dan diagram
print(table)
plt.tight_layout()
plt.show()
