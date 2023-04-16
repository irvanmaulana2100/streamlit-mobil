import pickle
import streamlit as st

model = pickle.load(open('Estimasi_mobil.sav', 'rb'))

st.title('Selamat Datang di Website Estimasi Harga Mobil Toyota')

year = st.number_input('Input Tahun Pembuatan')
mileage = st.number_input('Masukkan Kilometer Mobil')
tax = st.number_input('Masukkan Pajak Mobil')
mpg = st.number_input('Masukkan Konsumsi BBM')
engineSize = st.number_input('Masukkan Size Engine')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi Harga Mobil dalam Pounds : ', predict)
    st.write('Estimasi Harga Mobil dalam IDR(Juta) : ', predict*18500)