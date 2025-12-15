# 📚 PerpusBot ITERA

PerpusBot ITERA adalah chatbot informasi perpustakaan berbasis Machine Learning ringan yang dirancang untuk mahasiswa dan staf ITERA. Chatbot ini memberikan jawaban cepat terkait lokasi, jam operasional, peminjaman, koleksi buku, dan layanan perpustakaan.

---

## 🔹 Fitur Utama
- Menjawab pertanyaan terkait **informasi perpustakaan ITERA**.
- Memberikan informasi **koleksi buku dan ketersediaannya**.
- Menyediakan jawaban **FAQ** dan layanan TA.
- Mudah diakses melalui **Streamlit**.

---

## 🔹 Data
PerpusBot menggunakan dataset dummy akademik sebagai baseline:
1. **Knowledge Base Chatbot**
   - Kolom: `intent`, `question_keywords`, `answer`
   - Contoh pertanyaan: lokasi perpustakaan, jam operasional, cara meminjam, dsb.

2. **Koleksi Buku**
   - Kolom: `book_id`, `judul`, `kategori`, `tahun_terbit`, `stok`
   - Informasi koleksi buku yang bisa dicek melalui OPAC.

3. **Statistik Perpustakaan**
   - Kolom: `koleksi`, `kunjungan_harian`, `pembaca_aktif`, `jumlah_exemplar`, `tahun_data`
   - Ringkasan statistik perpustakaan.

---

## 🔹 Teknologi
- **Python** (3.10+)
- **Streamlit** untuk antarmuka online
- **scikit-learn** (TF-IDF + cosine similarity)
- **pandas** untuk pengolahan data
- **re** untuk normalisasi teks
- **MLflow** (opsional) untuk tracking eksperimen

---

## Kelompok 9 MLOps RA
- Asa Do'a Uyi 122450005
- Renisha Putri Giani 122450079
- Mirzan Yusuf Rabbani 122450118
- Nasywa Nur Afifah 122450125
