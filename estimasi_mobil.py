import pickle
import streamlit as st
from PIL import Image

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Toyota Bekas')
st.image('toyota.png')
st.text('Silahkan diisi dengan benar.')

st.sidebar.header('Kritik dan Saran')
st.sidebar.text_input('Nama')
st.sidebar.text_input('Email')
st.sidebar.text_area('Kritik & Saran')
st.sidebar.button('KIRIM')

year = st.number_input('Masukkan Tahun Pembuatan')
mileage = st.number_input('Masukkan Kilometer Mobil')
tax = st.number_input('Masukkan Pajak Mobil')
mpg = st.number_input('Masukkan Konsumsi BBM')
engineSize = st.number_input('Masukkan Size Engine')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi Harga Mobil dalam Rupiah(Juta) : ', predict*18500)