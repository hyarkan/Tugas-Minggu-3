# Catatan Penggunaan AI

## Tujuan

AI digunakan sebagai alat bantu untuk mendukung implementasi dan debugging aplikasi PMB berbasis FastAPI.

## Bantuan AI

AI membantu dalam penyusunan model SQLAlchemy, konfigurasi Alembic dan migrasi database, pembuatan endpoint registrasi PMB, validasi input dan penanganan error, serta penyusunan dokumentasi.

## Prompt Terbaik

Prompt yang dipilih dan dirangkum dari kebutuhan pengerjaan proyek:

"Bantu saya mengembangkan aplikasi PMB berbasis FastAPI menggunakan SQLAlchemy 2.0 dan Alembic. Implementasikan tiga model tabel beserta atribut dan constraint yang diperlukan, konfigurasi migrasi database dengan pengujian upgrade dan downgrade, serta buat endpoint POST /api/pmb/register. Pastikan endpoint memiliki validasi input, menolak email duplikat dengan HTTP 409, dan menangani kesalahan data seperti tanggal lahir, program studi, serta jalur masuk yang tidak valid. Berikan penjelasan implementasi dan langkah pengujian agar hasilnya dapat diperiksa."

Prompt tersebut digunakan sebagai acuan untuk memperoleh bantuan AI dalam implementasi dan pengujian aplikasi PMB.

## Pengujian

Pengujian mencakup skenario berikut:

- Registrasi berhasil: `201`
- Email duplikat: `409`
- Tanggal lahir tidak valid: `422`
- Program studi tidak ditemukan: `400`
- Jalur masuk tidak ditemukan: `400`

## Peran Mahasiswa

Mahasiswa meninjau saran AI, menjalankan dan menguji aplikasi, memeriksa hasil migrasi, serta memastikan hasil akhir sesuai dengan instruksi tugas.

## Pernyataan

AI digunakan sebagai alat bantu. Verifikasi dan tanggung jawab atas hasil akhir tetap berada pada mahasiswa.
