# 📚 PerpusBot ITERA

PerpusBot ITERA adalah chatbot informasi perpustakaan berbasis *Machine Learning ringan* yang dikembangkan untuk membantu mahasiswa dan sivitas akademika ITERA memperoleh informasi perpustakaan secara cepat, akurat, dan mudah diakses.  
Chatbot ini menggunakan pendekatan *Information Retrieval* dengan **TF-IDF** dan **Cosine Similarity** untuk mencocokkan pertanyaan pengguna dengan basis pengetahuan yang tersedia.

🔗 **Demo Aplikasi:**  
https://perpusbotitera.streamlit.app/

---

## 🎯 Tujuan Pengembangan

- Menyediakan layanan informasi perpustakaan ITERA secara otomatis
- Mengurangi beban pertanyaan berulang kepada pustakawan
- Mengimplementasikan konsep *Machine Learning* sederhana dalam konteks nyata
- Menerapkan alur dasar **MLOps** (data → model → deployment)

---

## ✨ Fitur Utama

- 💬 Chatbot interaktif berbasis teks
- 🧠 Pencocokan pertanyaan menggunakan TF-IDF & cosine similarity
- 📖 Informasi lengkap perpustakaan ITERA:
  - Lokasi dan jam operasional
  - Peminjaman dan pengembalian buku
  - Perpanjangan dan denda keterlambatan
  - Layanan Tugas Akhir (TA)
  - Tata tertib dan aturan ruang baca
- 📂 Basis pengetahuan berbentuk dataset CSV (mudah dikembangkan)
- 🛡️ Fallback response jika pertanyaan tidak ditemukan
- 🌐 Akses online melalui Streamlit Community Cloud

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.10+**
- **Streamlit** – antarmuka web
- **scikit-learn** – TF-IDF & cosine similarity
- **pandas** – pengolahan dataset
- **re (regex)** – normalisasi teks
- **MLflow** *(opsional)* – tracking eksperimen

---

## ⚙️ Cara Kerja Sistem

1. Pengguna memasukkan pertanyaan melalui antarmuka Streamlit
2. Teks pertanyaan dinormalisasi (lowercase, pembersihan karakter)
3. Pertanyaan diubah menjadi vektor TF-IDF
4. Sistem menghitung kemiripan dengan dataset CSV
5. Jawaban dengan skor kemiripan tertinggi ditampilkan
6. Jika skor rendah, sistem memberikan jawaban alternatif

---

## 📂 Struktur Proyek

