# Bike-Sharing Rental Analysis and Dashboard

## How to Run the Dashboard

1. **Setup environmeent**
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

2. **Run streamlit app**
streamlit run bike.py


## Getting Started
### 1. Running the Analysis Notebook (notebook.ipynb)
1. Download the project from the repository or another source.
2. Open your preferred IDE, such as Jupyter Notebook or Google Colaboratory.
3. Create a new notebook in your chosen IDE.
4. Upload the notebook.ipynb file to your new notebook. Select the file with the .ipynb extension.
5. Connect to Hosted Runtime: If using Google Colaboratory, connect to a hosted runtime.
6. Run all code cells in the notebook to visualize and analyze the results.


### 2. Running the Streamlit Dashboard (dashboard/dashboard.py)
1. Download the project from the repository or another source.
2. Install Dependencies:
- Open the terminal or command prompt.
- Install Streamlit and other libraries
3. Check CSV File Location: Ensure the CSV file remains in the same folder as dashboard.py.
4. Run the Dashboard:
- Open Visual Studio Code (VSCode).
- Run the dashboard by typing the following command in the terminal: streamlit run bike.py
5. Access the Dashboard: Open a web browser and access the dashboard through the URL displayed in the terminal.

## Analysis

### Defining Question

- Bagaimana tren penggunaan sepeda dalam dalam beberapa tahun terakhir?
- Apakah cuaca mempengaruhi jumlah penyewa sepeda?
- Bagaimana pola penggunaan sepeda berdasarkan waktu (workingday, holiday, dan weekday)?
- Apakah musim mempengaruhi penyewa sepeda berdasarkan pelanggan Casual dan Registered?
- Bagaimana pola penggunaan sepeda berdasarkan jam dalam sehari? 

### Insight and Findings

- Jumlah penyewa sepeda pada tahun 2012 lebih tinggi dibandingkan pada tahun 2011. Pada awal tahun, baik pada tahun 2011 maupun tahun 2012, jumlah penyewa sepeda menunjukkan angka terendah.Pada tahun 2012, puncak jumlah penyewaan sepeda terjadi pada bulan September, sementara pada tahun 2011 puncaknya terjadi pada bulan Juni.
- kondisi cuaca memengaruhi jumlah penyewa sepeda. Khususnya, kondisi cuaca cerah atau sedikit berawan lebih disukai oleh penyewa sepeda, seiring dengan peningkatan jumlah penyewaan pada kondisi tersebut. Hal ini mungkin dikaitkan dengan kenyamanan dan keamanan berkendara di kondisi cuaca yang cerah.
- Pelanggan cenderung lebih memilih menyewa sepeda pada hari kerja dan bukan hari libur. Hal ini dapat disebabkan oleh kebutuhan transportasi harian ke tempat kerja atau aktivitas rutin lainnya yang dilakukan pada hari kerja. Jumat merupakan hari dengan jumlah rata-rata penyewa sepeda terbanyak dibandingkan dengan hari-hari lainnya.
- Baik pelanggan casual maupun pelanggan terdaftar (registered) menunjukkan kecenderungan yang tinggi untuk menyewa sepeda pada musim gugur. Sebaliknya, musim semi menunjukkan jumlah penyewaan sepeda paling rendah. Namun, tidak terlihat perbedaan yang signifikan dalam pola preferensi bersepeda antara pengguna casual dan pengguna terdaftar.
- Terdapat perbedaan pola penyewaan sepeda antara hari kerja dan akhir pekan. Pada hari kerja, puncak aktivitas terjadi pada pukul 08.00 dan 17.00, mencerminkan kebutuhan transportasi untuk pergi dan pulang dari tempat kerja. Di akhir pekan, frekuensi penyewaan lebih tinggi pada siang hari.

## Dashboard with Streamlit
View the dashboard on streamlit could directly on this link: https://bike-sharing-verent.streamlit.app/

![Bikesharing Rental Dashboard](screenshots/Screenshot%201.png)

![Bikesharing Rental Dashboard](screenshots/Screenshot%202.png)

![Bikesharing Rental Dashboard](screenshots/Screenshot%203.png)

![Bikesharing Rental Dashboard](screenshots/Screenshot%204.png)

![Bikesharing Rental Dashboard](screenshots/Screenshot%205.png)

![Bikesharing Rental Dashboard](screenshots/Screenshot%206.png)
