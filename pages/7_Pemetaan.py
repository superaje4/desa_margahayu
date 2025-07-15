import streamlit as st
import base64
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemetaan Desa Margahayu",
    page_icon="🗺️",
    layout="wide"
)

# Header
col1, col2 = st.columns((0.25, 1))
col1.image("margahayu.png", width=100)
col2.title("Pemetaan Desa Margahayu")
col2.markdown("**Visualisasi Lokasi Strategis & Infrastruktur Desa Margahayu**")

st.markdown("---")

# Subheader Peta
st.subheader("📍 Peta Interaktif Desa Margahayu")

embed_url = "https://www.google.com/maps/d/embed?mid=1sFK24sv2lI1ZROolqYAvxl_uWwoMN74&ehbc=2E312F"

st.markdown("""
Berikut adalah peta interaktif yang menampilkan berbagai lokasi penting di Desa Margahayu, seperti fasilitas umum, lahan pertanian, dan infrastruktur lainnya.
""")

# Tampilkan peta di iframe
st.markdown(f"""
<iframe src="{embed_url}" width="100%" height="600" style="border:0;"></iframe>
""", unsafe_allow_html=True)

# Tombol untuk membuka di tab baru
st.markdown(f"""
🔗 [**Buka Peta di Google Maps (Tab Baru)**](https://www.google.com/maps/d/u/0/viewer?mid=1sFK24sv2lI1ZROolqYAvxl_uWwoMN74)
""")

st.markdown("---")

# KMZ Download
st.subheader("📂 Unduh Data Lokasi (KMZ)")

st.markdown("""
Untuk keperluan pemetaan lanjutan atau analisis di Google Earth, Anda dapat mengunduh file KMZ berikut:
""")

kmz_path = "C:/Users/ASUS/Desktop/Daming/VSC/desa_margahayu/Desa Margahayu.kmz"  # Ganti dengan path file KMZ yang sebenarnya

if os.path.exists(kmz_path):
    with open(kmz_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/vnd.google-earth.kmz;base64,{b64}" download="Peta_Desa_Margahayu.kmz">📥 Klik di sini untuk mengunduh file KMZ</a>'
        st.markdown(href, unsafe_allow_html=True)
else:
    st.warning("📎 File KMZ belum tersedia. Silakan unggah terlebih dahulu.")

st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("desa_lestari.png", width=180)
    st.header("Pemetaan Desa")
    st.caption("Halaman ini menyajikan visualisasi geografis berbagai elemen strategis Desa Margahayu melalui peta interaktif dan data spasial.")
