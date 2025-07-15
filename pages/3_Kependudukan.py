import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Kependudukan",
    page_icon=":family:",
)

datadesa = pd.read_csv("./data/datadesa.csv")              #convert ke panda df

#this is the header
t1, t2 = st.columns((0.25, 1))
t1.image('margahayu.png', width=100)
t2.title("Desa Margahayu")
t2.markdown("##### Halaman Kependudukan Desa Margahayu")
st.markdown("---")

# Pilih Tahun Global - Akan memengaruhi semua data
st.write("### Pilih Tahun")
tahun_pilihan = st.radio("Tahun Data:", options=["2023", "2022"], index=0, horizontal=True)

#data umur
 # Save to CSV for local use
data_umur_2023=pd.read_csv('./data/data_umur_2023.csv')
data_umur_2022=pd.read_csv('./data/data_umur_2022.csv')

#data etnis  # Save to CSV for local use
data_etnis_2023=pd.read_csv('./data/data_etnis_2023.csv')
data_etnis_2022 = pd.read_csv('./data/data_etnis_2022.csv')

#data agama
data_agama_2023= pd.read_csv('./data/data_agama_2023.csv')
data_agama_2022 = pd.read_csv('./data/data_agama_2022.csv')

#data pekerjaan
data_pekerjaan_2023= pd.read_csv('./data/data_pekerjaan_2023.csv')
data_pekerjaan_2022 = pd.read_csv('./data/data_pekerjaan_2022.csv')

#data pendidikan  # Save to CSV for local use
data_pendidikan_2023=pd.read_csv('./data/data_pendidikan_2023.csv')
data_pendidikan_2022 = pd.read_csv('./data/data_pendidikan_2022.csv')

if tahun_pilihan == "2023":
    data_umur = data_umur_2023
    jp= data_umur.iloc[0:16,1:3].sum().sum()
    datapiramida = data_umur.iloc[0:16,1:3]
    datapiramida.iloc[0:16,0] = -datapiramida.iloc[0:16,0]  
    datapiramida.index = list(data_umur.iloc[0:16,0])
    tabel_umur= data_umur.iloc[0:16,0:3]
    
    
    data_etnis = data_etnis_2023
    data_agama = data_agama_2023
    data_pekerjaan = data_pekerjaan_2023
    data_pendidikan = data_pendidikan_2023
else:
    data_umur = data_umur_2022
    jp=data_umur.iloc[0:13,1:3].sum().sum()
    datapiramida = data_umur.iloc[0:13,1:3]
    datapiramida.iloc[0:13,0] = -datapiramida.iloc[0:13,0]
    datapiramida.index = list(data_umur.iloc[0:13,0])
    tabel_umur = data_umur.iloc[0:13,0:3]
    
    data_etnis = data_etnis_2022
    data_agama = data_agama_2022
    data_pekerjaan = data_pekerjaan_2022
    data_pendidikan = data_pendidikan_2022




#data umur
st.write("# Jumlah Penduduk Berdasarkan Jenis Kelamin dan Kelompok Usia")
jk = list(["Laki-laki","Perempuan"])
datapiramida.columns = jk


import altair as alt
# Convert wide-form data to long-form
# See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
data = pd.melt(datapiramida.reset_index(), id_vars=["index"])
# Horizontal stacked bar chart
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title="",axis=alt.Axis(labels=False)),
        y=alt.Y("index", type="nominal", title="usia",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)

st.altair_chart(chart, use_container_width=True)   #bikin piramida chart
st.write("Total Penduduk:",int(jp)," | Penduduk Laki-laki:",int(data_umur.iloc[20,1])," | Penduduk Perempuan:",int(data_umur.iloc[21,1]))
with st.expander("lihat tabel"):
    st.dataframe(tabel_umur, use_container_width=True, hide_index=True)   #menampilkan data

#data pekerjaan
st.write("# Jumlah Penduduk Berdasarkan Jenis Pekerjaan")
df_pekerjaan = data_pekerjaan
chart = (
    alt.Chart(df_pekerjaan)
    .mark_bar()
    .encode(
        x=alt.X("Jumlah:Q", title=""),
        y=alt.Y("Status Pekerjaan:N", sort='-x', title=""),
        color=alt.value("#1f77b4")
    )
)
# Tambahkan label jumlah di ujung bar
text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3
).encode(
    text='Jumlah:Q'
)
final_chart = chart + text
st.altair_chart(final_chart, use_container_width=True)

with st.expander("Lihat Tabel Data"):
    st.dataframe(df_pekerjaan, use_container_width=True, hide_index=True)

#data pendidikan
df_pendidikan = data_pendidikan
st.write("# Jumlah Penduduk Berdasarkan Tingkat Pendidikan")
# --- Chart horizontal bar ---
chart = (
    alt.Chart(df_pendidikan)
    .mark_bar()
    .encode(
        x=alt.X("Jumlah:Q", title=""),
        y=alt.Y("Tingkat Pendidikan:N", sort='-x', title=""),
        color=alt.value("#1f77b4")
    )
)

# --- Tambahkan label angka di ujung bar ---
text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3
).encode(
    text='Jumlah:Q'
)

final_chart = chart + text
st.altair_chart(final_chart, use_container_width=True)

with st.expander("Lihat Tabel"):
    st.dataframe(df_pendidikan, use_container_width=True, hide_index=True)

#data etnis
st.write('# Jumlah Penduduk Menurut Etnis')

et = data_etnis
et.index = list(et.iloc[0:21,0])
et = et.iloc[0:20,1:4]
pilih5 = st.radio("Pilih Jenis Kelamin: ",['Laki & Perempuan','Laki-laki','Perempuan'],key="etnis")
if pilih5 =='Laki & Perempuan':
    datatp4 = et.iloc[0:20,2]
elif pilih5 == 'Laki-laki':
    datatp4 = et.iloc[0:20,0]
elif pilih5 == 'Perempuan':
    datatp4 = et.iloc[0:20,1]
datatp4 = pd.melt(datatp4.reset_index(), id_vars=["index"])
et0 = st.checkbox("jangan tampilkan data bernilai 0 (nol)",value=True,key="et0")
if et0:
    datatp4 = datatp4[datatp4['value'] != 0]        #Filter untuk menghapus baris di mana value = 0
charttp4 = (
    alt.Chart(datatp4,title=alt.TitleParams(pilih5, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title=""),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text4 = charttp4.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp4 = (charttp4 + text4)
st.altair_chart(charttp4,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(et,use_container_width=True)


#data agama
st.write('# Jumlah Penduduk Menurut Agama')
agam = data_agama
agam.index = list(agam.iloc[0:9,0])
agam = agam.iloc[0:8,1:4]
pilih6 = st.radio("Pilih Jenis Kelamin: ",['Laki & Perempuan','Laki-laki','Perempuan'],key="agama")
if pilih6 =='Laki & Perempuan':
    datatp5 = agam.iloc[0:8,2]
elif pilih6 == 'Laki-laki':
    datatp5 = agam.iloc[0:8,0]
elif pilih6 == 'Perempuan':
    datatp5 = agam.iloc[0:8,1]
datatp5 = pd.melt(datatp5.reset_index(), id_vars=["index"])
agam0 = st.checkbox("jangan tampilkan data bernilai 0 (nol)",value=True,key="agam0")
if agam0:
    datatp5 = datatp5[datatp5['value'] != 0]        #Filter untuk menghapus baris di mana value = 0
charttp5 = (
    alt.Chart(datatp5,title=alt.TitleParams(pilih6, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index",type="nominal", title=""),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text5 = charttp5.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp5 = (charttp5 + text5)
st.altair_chart(charttp5,use_container_width=True)
with st.expander("lihat tabel"):
    st.dataframe(agam,use_container_width=True)

with st.sidebar:
    st.image('desa_Lestari.png',width=180)
    st.header("Dashboard Data Kependudukan Desa Margahayu")
    st.caption("""Menu kependudukan ini menyediakan data jumlah penduduk berdasarkan usia, jenis kelamin, serta data tingkat pendidikan dan status pendidikan angkatan kerja di Desa Margahayu, Kecamatan Pegaden Barat, Kabupaten Subang, Jawa Barat.""")
