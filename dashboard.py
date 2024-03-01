import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

with st.sidebar:
    st.subheader('Bike Sharing Dataset')
    st.image("https://th.bing.com/th/id/OIP.VyPZmXDDAUcMjpd7ZIsGCQHaEX?w=253&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")
    st.markdown('---')
    st.write("Menu")
    selected_menu = st.radio("", ["Dashboard", "Dashboard Musim", "Dashboard Persentase Musim"])

# Memuat data
day_df = pd.read_csv("clean_day.csv")

# Mengelompokkan data berdasarkan musim dan menghitung jumlah sewa sepeda
season_counts = day_df.groupby('season')['count_cr'].sum().reset_index()

# Fungsi untuk menghitung jumlah sewa sepeda berdasarkan musim
def hitung_jumlah_sewa_per_musim(data):
    sewa_per_musim = data.groupby('season')['count_cr'].sum().reset_index()
    return sewa_per_musim

# Fungsi untuk membuat plot
def tampilkan_plot(data):
    plt.figure(figsize=(10, 6))
    plt.bar(data['season'], data['count_cr'], color='skyblue')
    plt.title('Distribusi Jumlah Sewa Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Sewa Sepeda')
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Fungsi untuk membuat plot lingkaran
def create_pie_chart(data):
    plt.figure(figsize=(8, 8))
    plt.pie(data['count_cr'], labels=data['season'], autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
    plt.title('Persentase Jumlah Sewa Sepeda Berdasarkan Musim')
    plt.axis('equal')
    st.pyplot(plt)

def main():
    if selected_menu == "Dashboard":
        st.title('Dashboard Distribusi dan Persentase Jumlah Sewa Sepeda Berdasarkan Musim')
        st.markdown("Dashboard ini menampilkan distribusi jumlah sewa sepeda berdasarkan musim serta persentase jumlah sewa sepeda berdasarkan musim.")
        tampilkan_plot(season_counts)
        create_pie_chart(season_counts)
    elif selected_menu == "Dashboard Musim":
        st.title('Dashboard Distribusi Jumlah Sewa Sepeda Berdasarkan Musim')
        st.markdown("Dashboard ini menampilkan distribusi jumlah sewa sepeda berdasarkan musim.")
        tampilkan_plot(season_counts)
    elif selected_menu == "Dashboard Persentase Musim":
        st.title('Dashboard Persentase Jumlah Sewa Sepeda Berdasarkan Musim')
        st.markdown("Dashboard ini menampilkan persentase jumlah sewa sepeda berdasarkan musim.")
        create_pie_chart(season_counts)

if __name__ == '__main__':
    main()

st.caption('Copyright (c) Kahfi Zairan Maulana 2024')
