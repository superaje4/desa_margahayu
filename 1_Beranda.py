# -- coding: utf-8 --
"""
Created on Wed Oct  4 11:54:31 2023

@author: Asus
"""

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import base64

st.set_page_config(page_title="Dashboard Data Desa Margahayu", page_icon="🏠")

# this is the header
t1, t2 = st.columns((0.25, 1))
t1.image('margahayu.png', width=100)
t2.title("Desa Margahayu")
t2.markdown("##### Halaman Utama Dashboard Data Desa Margahayu")
st.markdown("---")

#this is content
 #st.image('https://www.desawisata-cibiruwetan.com/wp-content/uploads/2023/01/branding-cibiru-wetan-WISATA-1-800x197.png')
### Import Data Lengkap

datadesa = pd.read_csv('./data/datadesa.csv')  # Load data from CSV file
#convert ke panda df
st.write("# Rekap Data Desa Margahayu")


datap2024 = pd.read_csv("./data/datap2024.csv")            
jp2024=datap2024.iloc[0:16,1:3].sum().sum()

datapiramida = datap2024.iloc[0:16,1:3]
jk = list(["Laki-laki","Perempuan"])
datapiramida.iloc[0:16,0]=-datapiramida.iloc[0:16,0]
datapiramida.index = list(datap2024.iloc[0:16,0])
datapiramida.columns = jk

pd2024laki = int(datap2024.iloc[0:16,1:2].sum().sum())
pd2024pere = int(datap2024.iloc[0:16,2:3].sum().sum())
lakipere2024 = pd.DataFrame({"laki":[pd2024laki],"perempuan":[pd2024pere]})
lakipere2024.columns = list(["Laki-laki","Perempuan"])

m1, m2, m3 = st.columns((1,1,1))
m1.write("")
m2.metric(label = 'Total KK',value = "📋"+str(int(datap2024.iloc[18,1])))
m3.write("")

m1, m2, m3 = st.columns((1,1,1))
m1.write("")
m2.metric(label ='Total Penduduk (jiwa)',value = "🚻"+str(int(jp2024)))
m3.write("")

m1, m2, m3, m4 = st.columns((1,1,1,1))
m1.write("")
m2.metric(label ='Penduduk Laki-laki',value = "🚹"+str(int(pd2024laki)))
m3.metric(label = 'Penduduk Perempuan',value = "🚺"+str(int(pd2024pere)))
m4.write("")
st.write("Berdasarkan data Kementerian Dalam Negeri (Kemendagri), jumlah kartu keluarga (KK) yang terdaftar di Desa Margahayu pada tahun ",str(int(datadesa.iloc[20,1]))," sebanyak ",str(int(datap2024.iloc[18,1])),". Jumlah penduduk pada periode tersebut sebanyak ",str(int(jp2024))," jiwa dengan penduduk laki-laki sebanyak ",str(int(pd2024laki))," jiwa dan penduduk perempuan sebanyak",str(pd2024pere)," jiwa.")


fas23 = pd.read_csv("./data/fas23.csv")                     #convert ke panda df
fas23 = fas23.iloc[1:98,0:3]
sd=int(fas23.iloc[2,1]);mi=int(fas23.iloc[14,1]);sdt=int(fas23.iloc[2,1]+fas23.iloc[14,1])
smp=int(fas23.iloc[3,1]);mts=int(fas23.iloc[15,1]);smpt=int(fas23.iloc[3,1]+fas23.iloc[15,1])
sma=int(fas23.iloc[4,1]);ma=int(fas23.iloc[16,1]);smat=int(fas23.iloc[4,1]+fas23.iloc[16,1])

pd1,pd2,pd3,pd4,pd5 = st.columns((1,1,1,1,1))
pd1.write("")
pd2.metric(label='SD',value="🎒"+str(sdt))
pd3.metric(label='SMP',value="🏫"+str(smpt))
pd4.metric(label='SMA/K',value="📘"+str(smat))
pd5.write("")
st.write("Berdasarkan data Kementerian Pendidikan dan Budaya (Kemendikbud) dan Kementerian Agama, jumlah sekolah yang terdaftar di Desa Margahayu pada tahun ",str(int(datadesa.iloc[21,1])),", antara lain SD/sederajat sebanyak ",str(sdt)," (termasuk ",str(mi)," Madrasah Ibtidaiyah/MI), SMP/sederajat sebanyak ",str(smpt)," (termasuk ",str(mts)," Madrasah Tsanawiyah/MTs), dan SMA/SMK/sederajat sebanyak ",str(smat)," (termasuk ",str(ma)," Madrasah Aliyah/MA).")


pt23 = pd.read_csv("./data/pt23.csv") #
pt23 = pt23.iloc[0:65,0:4]
pt23.index = list(pt23.iloc[0:65,0])
pt23 = pt23.iloc[0:72,1:4]
p1,p2 = st.columns((1,1))
p1.metric(label='Hasil panen Padi (Ton/Ha)',value="🌾"+str(int(pt23.iloc[0,1])))
p2.metric(label='Hasil Panen Kacang Tanah (Ton/Ha)',value=" 🥜"+str(int(pt23.iloc[3,1])))
st.write("Pada tahun ",str(int(datadesa.iloc[22,1])),", sawah di Desa Margahayu yang memiliki luas ",str(int(pt23.iloc[0,0]))," hektar (Ha) menghasilkan panen sebanyak ",str(int(pt23.iloc[0,1]))," Ton untuk setiap hektarnya. Selain itu, lahan kacang tanah di Margahayu yang memiliki luas ",str(int(pt23.iloc[3,0]))," hektar (Ha) memiliki hasil panen sebanyak ",str(int(pt23.iloc[3,1]))," Ton untuk setiap hektarnya.")

import pydeck as pdk
st.write("# Profil Desa Margahayu")
with st.sidebar:
    st.image('desa_lestari.png',width=180)
    st.header("Dashboard Desa Margahayu")
    st.caption("""Dashboard ini menyediakan data kewilayahan dan karakteristik penduduk di Desa Margahayu, Kecamatan Pegaden Barat, Kabupaten Subang, Jawa Barat.""")



datadesa1 = pd.DataFrame(datadesa.iloc[0:12,0:2])                       #convert ke panda df
desa = datadesa1.style.hide(axis=0).hide(axis=1)                     #menyembunyikan nomor tabel dan header                                   #menyembunyikan header
st.image('desa.jpg')
st.write(desa.to_html(),unsafe_allow_html=True,use_container_width=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

st.write("# Peta Lokasi Desa Margahayu")
# Gambar lokal
mapimage = 'maps.png'  # Pastikan file ini ada di folder yang sama
urlmaps = 'https://www.google.com/maps/place/Margahayu,+Pagaden+Barat,+Subang+Regency,+West+Java,+Indonesia/@-6.4759309,107.7748455,15z/data=!3m1!4b1!4m6!3m5!1s0x2e69392f52cc8d7f:0x394bb6a8c964cd71!8m2!3d-6.4785615!4d107.772504!16s%2Fg%2F11b_2k9jyc?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D'
# Baca dan encode file PNG
with open(mapimage, "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()
# Tampilkan gambar yang bisa diklik
st.markdown(
    f'<a href="{urlmaps}" target="_blank">'
    f'<img src="data:image/png;base64,{encoded}" alt="Clickable Map" style="width: 100%;" title="Klik untuk membukanya di Maps">'
    f'</a>',
    unsafe_allow_html=True
)
st.write("Desa Margahayu, Kecamatan Pagaden Barat, Kabupaten Subang, Jawa Barat")

datadesa2 = pd.DataFrame(datadesa.iloc[12:18,0:2])                       #convert ke panda df
desa2 = datadesa2.style.hide(axis=0).hide(axis=1)                        #menyembunyikan header dan nomor tabel
st.write(desa2.to_html(),unsafe_allow_html=True,use_container_width=True)         #menyembunyikan nomor tabel dari .to_html sampe True)

# st.write("# Kunjungi Kami")
# ig = "https://cdn-icons-png.flaticon.com/512/174/174855.png"
# fb = "https://cdn-icons-png.flaticon.com/512/124/124010.png"
# twitter = 'https://cdn-icons-png.flaticon.com/512/124/124021.png'
# url_ig = 'https://www.instagram.com/margahayuremaja?igsh=MTZuZm9ibmIwYnpsYg%3D%3D&utm_source=qr'
# url_fb = 'https://www.facebook.com/profile.php?id=100077962515459'
# url_twitter = 'https://x.com/margahayuremaja?s=21'
# #st.write("[instagram](%s)" % url_ig," | [youtube](%s)" % url_yt," | [website](%s)" % url_web)
# pd1,pd2,pd3,pd4, pd5= st.columns((1,1,1,1,1))

# # Menggunakan HTML untuk membuat gambar yang dapat diklik
# pd1.write('')
# pd2.markdown(f'<a href="{url_ig}" target="_blank"><img src="{ig}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
# pd3.markdown(f'<a href="{url_fb}" target="_blank"><img src="{fb}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
# pd4.markdown(f'<a href="{url_twitter}" target="_blank"><img src="{twitter}" alt="Clickable Image" style="width:80px;"></a>', unsafe_allow_html=True)
# pd5.write('')
# st.write("**📧: margahayuremajaremaja@gmail.com**")
# urlkantor = 'https://www.google.com/maps/place/Kantor+Desa+Margahayu/@-6.4667772,107.7668442,839m/data=!3m2!1e3!4b1!4m6!3m5!1s0x2e6938d41db89247:0xff667ed1d2d61eda!8m2!3d-6.4667772!4d107.7694191!16s%2Fg%2F11bw2ghj9j?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D'
# st.write("🏢: **[Jl.Cibangkonol No.28, Margahayu, Kec.Pagaden Barat, Kab.Subang, Jawa Barat 40625](%s)**"%urlkantor)


st.markdown("## 📲 Kunjungi Kami")

# Ikon media sosial
ig = "https://cdn-icons-png.flaticon.com/512/174/174855.png"
fb = "https://cdn-icons-png.flaticon.com/512/124/124010.png"
twitter = 'https://cdn-icons-png.flaticon.com/512/124/124021.png'

# Link akun media sosial
url_ig = 'https://www.instagram.com/margahayuremaja'
url_fb = 'https://www.facebook.com/profile.php?id=100077962515459'
url_twitter = 'https://x.com/margahayuremaja?s=21'

# Baris ikon media sosial
c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])

with c2:
    st.markdown(f'<a href="{url_ig}" target="_blank"><img src="{ig}" style="width:48px;"></a>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<a href="{url_fb}" target="_blank"><img src="{fb}" style="width:48px;"></a>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<a href="{url_twitter}" target="_blank"><img src="{twitter}" style="width:48px;"></a>', unsafe_allow_html=True)

st.markdown("---")

# Kontak dan lokasi
email = "margahayuremajaremaja@gmail.com"
url_kantor = 'https://www.google.com/maps/place/Kantor+Desa+Margahayu/@-6.4667772,107.7668442,839m/data=!3m2!1e3!4b1!4m6!3m5!1s0x2e6938d41db89247:0xff667ed1d2d61eda!8m2!3d-6.4667772!4d107.7694191!16s%2Fg%2F11bw2ghj9j?entry=ttu'

col1, col2 = st.columns([0.05, 4])
with col1:
    st.markdown("📧")
with col2:
    st.markdown(f"**{email}**")

col3, col4 = st.columns([0.05, 4])
with col3:
    st.markdown("🏢")
with col4:
    st.markdown(f"""[**Jl. Cibangkonol No.28, Margahayu, Kec. Pagaden Barat, Kab. Subang, Jawa Barat 40625**]({url_kantor})""")
