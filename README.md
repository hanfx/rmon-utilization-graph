<h2>RMON Utilization Graph Viewer Minitool</h2>
  Mini tool untuk bantu visualisasikan graph trafik Tx/Rx(Mbps) dari file .rmon/.csv yang diimport dari <b>IPASOLINK 200, 400, 1000 / IPASOLINK VR 2, 4, 10</b>

  <h4>📌 Features:</h4>
    <ul>
      <li>Generate visualisasi utilisasi trafik Rx/Tx(Mbps)</li> 
      <li>Melakukan read data, cleaning data kolom yang diperlukan (case: tidak semua kolom dipakai), penambahan kolom, konversi tipe data kolom object ke float64, penulisan rumus (konversi ke Mbps) <b>(x * 8) / (60 * 15) / 1000000</b></li>
      <li>Mark penggunaan max dan min Rx/Tx</li>
      <li>Support run.bat dan .exe (run.bat lebih mudah, .exe masih sering terjadi bug)</li>
    </ul>
  
  <h4>📂 Format file yang dipakai:</h4>
    <ul>
      <li>15min-ETH-s0p66-20250727-ABC123_site_name.rmon</li>
      <li>15min-ETH-s0p66-20250727-ABC123_site_name.csv</li>
      <li>15min-ETH-s0p66-20250727.csv</li>
      <li>Menampilkan waktu (`20250727`) pada label sumbu X</li>
      <li>Menampilkan nama site (`ABC123_site_name`) pada judul grafik</li>
    </ul>
     <br>jika format tidak sesuai maka ditampilkan nama file penuh sebagai fallback pada judul grafik.</br>

  <h4>🔧 Depedencies:</h4>
    <ul>
      <li><a href="https://www.python.org/downloads/" target="_blank">python</a></li>
      <li><a href="https://pip.pypa.io/en/stable/installation" target="_blank">pip</a></li>
      <li><a href="https://pypi.org/project/matplotlib/](https://matplotlib.org/stable/install/index.html" target="blank">matplotlib</a></li>
      <li><a href="https://pandas.pydata.org/docs/getting_started/install.html" target="_blank">pandas</a></li>
      <li><a href="https://docs.python.org/3/library/tkinter.html" target="_blank">tkinter (for .exe build)</a></li>
    </ul>

  <br></br>
  <h4>📈📉 Example:</h4>
  <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/0a2bf8a0-c1aa-4a51-8702-1796ba7efd9e" />
  <br></br>

  <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/d3a40911-17a6-46a9-ac70-98593f70ed87" />
  <br></br>
Sekian, semoga bermanfaat, terimakasih
