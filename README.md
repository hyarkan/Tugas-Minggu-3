# PMB App — Minggu 3

Implementasi awal modul Penerimaan Mahasiswa Baru (PMB):
- SQLAlchemy 2.0 models untuk `program_studi`, `jalur_masuk`, `calon_mahasiswa`
- Alembic migration dengan upgrade/downgrade
- FastAPI `POST /api/pmb/register`
- Validasi Pydantic, email unik, foreign key, status awal `pending`
- SQLite untuk pengembangan

## Menjalankan

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Buka Swagger UI: http://127.0.0.1:8000/docs

## Data referensi awal

Tambahkan program studi dan jalur masuk ke database sebelum mencoba register. Contoh melalui Python:

```bash
python -c "from app.database import SessionLocal; from app.models import ProgramStudi, JalurMasuk; db=SessionLocal(); db.add_all([ProgramStudi(kode='001', nama='Sistem Informasi', fakultas='FSTI'), JalurMasuk(nama='SNBP'), JalurMasuk(nama='SNBT'), JalurMasuk(nama='Mandiri')]); db.commit(); db.close()"
```

## Contoh request

`POST /api/pmb/register`

```json
{
  "nama_lengkap": "Siti Aminah",
  "email": "siti.aminah@example.com",
  "phone": "081234567890",
  "tanggal_lahir": "2007-04-12",
  "alamat": "Depok",
  "program_studi_id": 1,
  "jalur_masuk_id": 1
}
```

Sukses: HTTP 201, response berisi `id`, `nama_lengkap`, `email`, `phone`, `program_studi_id`, `jalur_masuk_id`, `status`, `created_at`, `nim`.

Uji email duplikat dengan mengirim request yang sama lagi: HTTP 409.

## Uji migrasi rollback

```bash
alembic downgrade -1
alembic upgrade head
```

Pastikan rollback dilakukan pada database pengembangan yang aman. `downgrade -1` menghapus tabel yang dibuat oleh revisi awal.

## Catatan validasi

- Format HP diperiksa pada lapisan Pydantic. SQLite tidak menyediakan constraint regex bawaan.
- SQLite foreign key diaktifkan melalui `PRAGMA foreign_keys=ON`.
- Format HP yang diterima: `+628...`, `628...`, atau `08...`, dengan nomor seluler Indonesia (bukan nomor rumah).
- Untuk mengikuti pilihan dosen, error validasi request yang default-nya 422 dipertahankan sebagai 422. Aturan bisnis/referensi tidak valid menjadi 400, email duplikat menjadi 409.
