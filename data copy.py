import pandas as pd

# Baca file Excel
dfs = pd.read_excel('datasetfix.xlsx', skiprows=range(2002, 2007))

# Cetak daftar nama kolom
print(dfs.columns)

