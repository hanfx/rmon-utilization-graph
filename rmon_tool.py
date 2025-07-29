import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import webbrowser

root = tk.Tk()
root.withdraw()  # Sembunyikan jendela utama Tkinter

print("Memulai script...")
file_path = filedialog.askopenfilename(
    title = "Pilih file CSV",
    filetypes=[("CSV/RMON files", "*.csv;*.rmon"), ("All files", "*.*")]
)

print("File path:", file_path)

# file_path = "15min-ETH-s0p66-20250727-KPA030_MT_STP_1K.csv"

data = pd.read_csv(file_path, header = 1)

data.insert(3, "RX Mbps", [0] * len(data))
data.insert(4, "TX Mbps", [0] * len(data))

# Mengubah ke string untuk melakukan pembersihan data
data['RX Octs'] = data['RX Octs'].astype(str)
data['TX Octs'] = data['TX Octs'].astype(str)

# Periksa apakah kolom 'RX Octs' atau 'TX Octs' mengandung karakter '*'
if data['RX Octs'].str.contains(r'\*').any() or data['TX Octs'].str.contains(r'\*').any():
    # Hapus karakter '*' jika ditemukan
    data['RX Octs'] = data['RX Octs'].str.replace('*', '', regex=False)
    data['TX Octs'] = data['TX Octs'].str.replace('*', '', regex=False)
    print("Karakter '*' telah dihapus dari kolom RX Octs dan TX Octs.")
else:
    print("Tidak ada karakter '*' pada kolom RX Octs dan TX Octs. Lanjutkan.")

data['RX Mbps'] = data['RX Mbps'].astype(float)
data['TX Mbps'] = data['TX Mbps'].astype(float)
data['RX Octs'] = data['RX Octs'].astype(float)
data['TX Octs'] = data['TX Octs'].astype(float)

data['RX Mbps'] = (data['RX Octs'] * 8)/(60*15)/1000000
data['TX Mbps'] = (data['TX Octs'] * 8)/(60*15)/1000000

# Membuat grafik garis untuk RX Mbps dan TX Mbps
plt.figure("RMON viewer tool v1.0 (experimental)", figsize=(10, 6))
ax = plt.axes()
ax.set_facecolor('#FDF6F6')

# Plot RX Mbps dan TX Mbps
plt.plot(data['Time Stamp'], data['RX Mbps'], label='RX Mbps', color='#002C54', linestyle='-', linewidth=2)
plt.plot(data['Time Stamp'], data['TX Mbps'], label='TX Mbps', color='#C5001A', linestyle='-', linewidth=2)

# Menambahkan judul grafik
file_base = os.path.splitext(os.path.basename(file_path))[0]
file_name_part = file_base.split('-')

if len(file_name_part)  >= 5:
    title_part = file_name_part[4]
else:
    title_part = file_base
plt.title(f"Utilisasi {title_part}", fontsize= 18)

time_part = file_base.split('-')[3]
plt.xlabel(f'Time {time_part}', fontsize=14)
plt.ylabel('Utils (Mbps)', fontsize=14)
# Menambahkan legenda
plt.legend()

#interval data
# data['Time Stamp'] = pd.to_datetime(data['Time Stamp'])
# data['Time Interval'] = data['Time Stamp'].apply(lambda x: pd.date_range(start=x, periods=2, freq='15min').max())

# Menandai sumbu x berdasarkan index data
# plt.xlim([data['Time Stamp'].min(),data['Time Stamp'].max()])

# Menemukan nilai tertinggi
max_rx = data['RX Mbps'].max()
min_rx = data['RX Mbps'].min()
max_tx = data['TX Mbps'].max()
min_tx = data['TX Mbps'].min()

# Menampilkan baris data tertinggi
highest_rx = data.loc[data['RX Mbps'] == max_rx]
lowest_rx = data.loc[data['RX Mbps'] == min_rx]
highest_tx = data.loc[data['TX Mbps'] == max_tx]
lowest_tx = data.loc[data['TX Mbps'] == min_tx]

# Menambahkan anotasi pada titik tertinggi
for idx, row in highest_rx.iterrows():
    plt.text(idx, row['RX Mbps'], f"Max: {row['RX Mbps']:.2f}", color='black', fontsize='small', va='bottom')

for idx, row in lowest_rx.iterrows():
    plt.text(idx, row['RX Mbps'], f"Min: {row['RX Mbps']:.2f}", color='black', fontsize='small', va='top')

for idx, row in highest_tx.iterrows():
    plt.text(idx, row['TX Mbps'], f"Max: {row['TX Mbps']:.2f}", color='black', fontsize='small', va='bottom')

for idx, row in lowest_tx.iterrows():
    plt.text(idx, row['TX Mbps'], f"Min: {row['TX Mbps']:.2f}", color='black', fontsize='small', va='top')

# Menambahkan margin +100 dari nilai maksimum data
# plt.ylim(0, max_rx * 1.2)
# plt.ylim(0, max_tx * 1.2)

# Tambahkan hyperlink
link_text = ax.text(
    1.0, -0.15,
    "About this minitool (Github) →",
    fontsize=10,
    color='blue',
    ha='right',
    va='center',
    transform=ax.transAxes
)
# Github link
def on_click(event):
    if link_text.contains(event)[0]:
        webbrowser.open("https://github.com/hanfx/rmon-utilization-graph")

# click event
plt.gcf().canvas.mpl_connect('button_press_event', on_click)
plt.tight_layout(rect=[0, 0.15, 1, 1])


# Menampilkan grafik

plt.grid(axis='y')
plt.xticks(data['Time Stamp'][::4], rotation=45)
plt.tight_layout()
plt.show()