import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Festival Desa", page_icon="🎉")

# Header halaman
t1, t2 = st.columns((0.25, 1))
t1.image('margahayu.png', width=100)
t2.title("Desa Margahayu")
t2.markdown("##### Halaman Festival Tahunan Desa Margahayu")
st.markdown("---")

# Daftar festival
festival_list = [
    {
        "nama": "Peringatan Hari Raya Besar Islam",
        "folder": "PHBI",
        "deskripsi": "Perayaan 1 Muharram, Maulid Nabi dengan berbagai kegiatan keagamaan.",
    },
    {
        "nama": "Napak Tilas Budaya",
        "folder": "Napak",
        "deskripsi": "Kegiatan napak tilas budaya lokal dengan pertunjukan seni tradisional.",
    },
    {
        "nama": "Ruatan Bumi",
        "folder": "Ruatan",
        "deskripsi": "Upacara adat untuk menjaga kesuburan tanah dan panen raya.",
    },
    {
        "nama": "17 Agustus",
        "folder": "17",
        "deskripsi": "Perayaan HUT RI dengan berbagai lomba dan upacara bendera.",
    }
]

# Loop setiap festival
for fest in festival_list:
    st.subheader(f"🎪 {fest['nama']}")
    st.markdown(f"_{fest['deskripsi']}_")

    # Path ke gambar
    image_paths = [f"foto_festival/{fest['folder']}_{i}.jpg" for i in range(1, 4)]
    cols = st.columns(3)

    for i in range(3):
        with cols[i]:
            try:
                img = Image.open(image_paths[i])
                img = img.resize((250, 180))  # Ukuran seragam
                st.image(img)
            except FileNotFoundError:
                st.warning(f"Gambar tidak ditemukan: {image_paths[i]}")

    st.markdown("---")

# Sidebar
with st.sidebar:
    st.image('desa_lestari.png', width=180)
    st.header("Festival Tahunan Desa Margahayu")
    st.caption("Empat festival utama Desa Margahayu yang menjadi agenda tahunan dan daya tarik masyarakat.")
