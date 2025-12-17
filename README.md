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
- **MLflow** – tracking eksperimen

---

## 🧠 Machine Learning Canvas

| Elemen ML Canvas | Deskripsi |
|-----------------|-----------|
| **Background** | Pengguna perpustakaan ITERA sering mengalami kesulitan mendapatkan informasi dasar seperti jam operasional, layanan, dan aturan peminjaman, terutama bagi mahasiswa baru dan pengunjung jarak jauh. |
| **Problem** | Informasi perpustakaan masih sering ditanyakan berulang secara manual dan tidak selalu mudah diakses kapan saja. |
| **Objective** | Membangun chatbot berbasis web yang mampu menjawab pertanyaan umum perpustakaan secara cepat, relevan, dan konsisten. |
| **Value Proposition** | Menyediakan akses informasi perpustakaan 24/7, mudah digunakan, dan mengurangi beban pertanyaan rutin ke petugas. |
| **Data** | Dataset berupa file CSV yang berisi kumpulan pertanyaan, intent, dan jawaban seputar layanan perpustakaan ITERA. |
| **Feature Engineering** | Teks pertanyaan diubah menjadi representasi numerik menggunakan TF-IDF untuk menangkap kata-kata penting dalam pertanyaan. |
| **Modeling** | Menggunakan TF-IDF Vectorizer dan Cosine Similarity untuk mencocokkan pertanyaan pengguna dengan pertanyaan pada dataset. |
| **Evaluation** | Evaluasi dilakukan secara manual berdasarkan relevansi jawaban terhadap maksud pertanyaan pengguna. |
| **Inference** | Inference dilakukan secara online melalui aplikasi Streamlit, di mana sistem langsung memberikan jawaban saat pengguna mengajukan pertanyaan. |
| **Deployment** | Aplikasi dideploy sebagai web app menggunakan Streamlit Cloud sehingga dapat diakses secara publik. |
| **Monitoring & Improvement** | Performa sistem ditingkatkan dengan menambah dan memperbarui dataset CSV berdasarkan pertanyaan yang belum terjawab. |

---

## ⚙️ Cara Kerja Sistem

1. Pengguna memasukkan pertanyaan melalui antarmuka Streamlit
2. Teks pertanyaan dinormalisasi (lowercase, pembersihan karakter)
3. Pertanyaan diubah menjadi vektor TF-IDF
4. Sistem menghitung kemiripan dengan dataset CSV
5. Jawaban dengan skor kemiripan tertinggi ditampilkan
6. Jika skor rendah, sistem memberikan jawaban alternatif

---

## 👥 Kelompok 9 — MLOps RA

| No | Nama | NIM |
|----|------|-----|
| 1 | Asa Do'a Uyi | 122450005 |
| 2 | Renisha Putri Giani | 122450079 |
| 3 | Mirzan Yusuf Rabbani | 122450118 |
| 4 | Nasywa Nur Afifah | 122450125 |

---

📌 *PerpusBot ITERA dikembangkan sebagai bagian dari tugas Mata Kuliah MLOps.*

