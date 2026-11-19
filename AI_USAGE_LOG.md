# Catatan Penggunaan AI

## Tujuan

AI digunakan sebagai alat bantu untuk mendukung implementasi dan debugging aplikasi PMB berbasis FastAPI.

## Bantuan AI

AI membantu dalam penyusunan model SQLAlchemy, konfigurasi Alembic dan migrasi database, pembuatan endpoint registrasi PMB, validasi input dan penanganan error, serta penyusunan dokumentasi.

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
