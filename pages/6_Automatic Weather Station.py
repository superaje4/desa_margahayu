import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Automatic Weather Station",
    page_icon="⛅"
)

# Header halaman
col1, col2 = st.columns((0.25, 1))
col1.image("margahayu.png", width=100)  # ganti dengan logo desa
col2.title("Automatic Weather Station")
col2.markdown("**Pantauan Cuaca Otomatis Desa Margahayu**")

st.markdown("---")

# Foto AWS
st.subheader("📸 Foto Automatic Weather Station")
st.image("aws.jpg", caption="Lokasi AWS di Desa Margahayu", use_container_width=True)

# Penjelasan AWS
st.subheader("🌤️ Apa itu Automatic Weather Station?")
st.markdown("""
**Automatic Weather Station (AWS)** adalah perangkat otomatis yang digunakan untuk mengukur dan merekam berbagai parameter cuaca seperti:
- Suhu udara
- Kelembaban
- Curah hujan
- Kecepatan dan arah angin
- Tekanan udara

AWS yang terpasang di Desa Cibiru Wetan menyediakan **data cuaca real-time** yang dapat dimanfaatkan untuk pertanian, peringatan dini bencana, dan perencanaan kegiatan masyarakat.

🌦️ **Fitur unggulan:**  
Selain pengamatan cuaca langsung, AWS juga menyediakan **prakiraan cuaca hingga 10 hari ke depan**, termasuk kemungkinan hujan, suhu harian, dan arah angin — sangat membantu untuk petani, nelayan, dan pelaku kegiatan luar ruang di desa.
""")

# Tautan ke dashboard AWS online
st.subheader("🔗 Pantau Data Cuaca Langsung")
dashboard_url = "https://jbr.cwssibu.org/dashboard/aws-jbr18"  # ganti dengan link sebenarnya
st.markdown(f"""
📡 Lihat data cuaca terkini di dashboard AWS melalui link berikut:

👉 [**Buka Dashboard AWS Desa Margahayu**]({dashboard_url})
""")

# Sidebar
with st.sidebar:
    st.image("desa_lestari.png", width=180)
    st.header("Pantauan Cuaca Desa")
    st.caption("Halaman ini menampilkan sistem pemantauan cuaca otomatis (AWS) yang dipasang di Desa Margahayu.")
