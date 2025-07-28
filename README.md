<b>Release 1</b> Alat bantu untuk generate graph mengenai utilisasi jaringan RX Mbps dan TX Mbps dalam 1 modem IPASOLINK 200, 400, 1000 / IPASO VR 2, 4, 10

  1. Generate diawali dengan penggantian extensi .rmon ke .csv secara manual karena pandas tidak dapat membaca .rmon (kemungkinan belum menemukan caranya)
  2. Melakukan read data, cleaning data kolom yang diperlukan (case: tidak semua kolom dipakai), penambahan kolom, konversi tipe data kolom object ke float64, penulisan rumus (konversi ke Mbps) <b>(x * 8) / (60 * 15) / 1000000</b>
  3. Pembuatan plot/graph menggunakan library Matplotlib
  4. Sampel graph ![image](https://github.com/user-attachments/assets/9fad0528-13c7-44a6-8133-a2b2c8874396)

<b>Release 2</b>
Beberapa improvement karena user tidak perlu menginstall python pada PC mereka

  1. Menjalana generate RMON graph via file .exe (lumayan besar sekitar 60Mb)
  2. Melakukan read data, cleaning data kolom yang diperlukan (case: tidak semua kolom dipakai), penambahan kolom, konversi tipe data kolom object ke float64, penulisan rumus (konversi ke Mbps) <b>(x * 8) / (60 * 15) / 1000000</b>
  3. Pembuatan plot/graph menggunakan library Matplotlib
  4. Sampel graph ![image](https://github.com/user-attachments/assets/08c7b73c-ef76-4400-8b3b-6d8dc72c4d71)


Sekian, terima kasih
