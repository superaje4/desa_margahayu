import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Pertanian dan Perkebunan",
    page_icon="🌴",
)

datadesa = pd.read_csv("./data/datadesa.csv")                #convert ke panda df

#this is the header
t1, t2 = st.columns((0.25, 1))
t1.image('margahayu.png', width=100)
t2.title("Desa Margahayu")
t2.markdown("##### Halaman Data Pertanian dan Perkebunan Desa Margahayu")
st.markdown("---")


pt23 = pd.read_csv("./data/pt23.csv")                      #convert ke panda df
lahan23 = pt23.iloc[70:73,0:2]
lahan23.index = list(lahan23.iloc[0:3,0])
lahan23 = lahan23.iloc[0:3,1:2]
pt23 = pt23.iloc[0:68,0:4]
pt23.index = list(pt23.iloc[0:68,0])
pt23 = pt23.iloc[0:68,1:4]


import altair as alt
st.write('# Luas Lahan Pertanian dan Perkebunan Berdasarkan Jenis Produksi')
data = pd.melt(lahan23.reset_index(), id_vars=["index"])
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title=""),
    )
)
text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
chart = (chart + text)
st.altair_chart(chart, use_container_width=True)
datapie = data
datapie['value'] = datapie['value'].div(float(data['value'].sum().sum()/100)).round(2)
piechart = alt.Chart(datapie,title=alt.TitleParams('Persentase (%) Luas Lahan Pertanian Berdasarkan Jenis Produksi', anchor='middle')).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="index", type="nominal"),
)
piechart = piechart.mark_arc(outerRadius=120)
textpie = piechart.mark_text(radius=140, size=20).encode(text="value")

piechart = piechart + textpie
tampil = st.checkbox("Tampilkan Grafik dalam Persentase")
if tampil:
    st.altair_chart(piechart, use_container_width=True)

st.write('## Tanaman Pangan Berdasarkan Komoditas')
pilih1 = st.radio("Menampilkan:",['Luas Lahan (Ha)','Hasil Panen (Ton/Ha)'],key="pangan")
if pilih1 =='Luas Lahan (Ha)':
    datatp1 = pt23.iloc[0:18,0]
elif pilih1 == 'Hasil Panen (Ton/Ha)':
    datatp1 = pt23.iloc[0:18,1]
datatp1 = pd.melt(datatp1.reset_index(), id_vars=["index"])
pangan0 = st.checkbox("jangan tampilkan data yang bernilai 0 (nol)",value=True,key="pangan0")
if pangan0:
    datatp1 = datatp1[datatp1['value'] != 0]        #Filter untuk menghapus baris di mana value = 0
charttp1 = (
    alt.Chart(datatp1,title=alt.TitleParams(pilih1, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text1 = charttp1.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp1 = (charttp1 + text1)
st.altair_chart(charttp1,use_container_width=True)

st.write('## Tanaman Buah-buahan Berdasarkan Komoditas')
pilih2 = st.radio("Menampilkan:",['Luas Lahan (Ha)','Hasil Panen (Ton/Ha)'],key="buah")
if pilih2 =='Luas Lahan (Ha)':
    datatp2 = pt23.iloc[18:48,0]
elif pilih2 == 'Hasil Panen (Ton/Ha)':
    datatp2 = pt23.iloc[18:48,1]
datatp2 = pd.melt(datatp2.reset_index(), id_vars=["index"])
buah0 = st.checkbox("jangan tampilkan data yang bernilai 0 (nol)",value=True,key="buah0")
if buah0:
    datatp2 = datatp2[datatp2['value'] != 0]        #Filter untuk menghapus baris di mana value = 0
charttp2 = (
    alt.Chart(datatp2,title=alt.TitleParams(pilih2, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text2 = charttp2.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp2 = (charttp2 + text2)
st.altair_chart(charttp2,use_container_width=True)

st.write('## Perkebunan Berdasarkan Komoditas')
pilih3 = st.radio("Menampilkan:",['Luas Lahan (Ha)','Hasil Panen (Ton/Ha)'],key="kebun")
if pilih3 =='Luas Lahan (Ha)':
    datatp3 = pt23.iloc[48:68,0]
elif pilih3 == 'Hasil Panen (Ton/Ha)':
    datatp3 = pt23.iloc[48:68,1]
datatp3 = pd.melt(datatp3.reset_index(), id_vars=["index"])
kebun0 = st.checkbox("jangan tampilkan data yang bernilai 0 (nol)",value=True,key="kebun0")
if kebun0:
    datatp3 = datatp3[datatp3['value'] != 0]        #Filter untuk menghapus baris di mana value = 0
charttp3 = (
    alt.Chart(datatp3,title=alt.TitleParams(pilih3, anchor='middle'))
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title="",sort="descending"),
        color=alt.Color("variable", type="nominal", title="",legend=None),
    )
)
text3 = charttp3.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='value'
)
charttp3 = (charttp3 + text3)
st.altair_chart(charttp3,use_container_width=True)

st.write('# Tabel Luas Lahan Hasil Pertanian dan Perkebunan')
st.dataframe(pt23,use_container_width=True)
st.write(" Keterangan: data di atas merupakan data tahun ",str(int(datadesa.iloc[22,1])))

with st.sidebar:
    st.image('desa_lestari.png',width=180)
    st.header("Dashboard Data Pertanian dan Perkebunan Desa Margahayu")
    st.caption("""Menu pertanian dan perkebunan menyediakan data luas lahan serta hasil panen dari berbagai komoditas tanaman pangan, buah-buahan, dan hasil perkebunan di Desa Margahayu, Kecamatan Cileunyi, Kabupaten Bandung, Jawa Barat.""")
