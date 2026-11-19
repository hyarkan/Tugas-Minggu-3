
from app.database import SessionLocal
from app.models.program_studi import ProgramStudi
from app.models.jalur_masuk import JalurMasuk


def seed_data():
    db = SessionLocal()

    try:
        # Data awal program studi
        program = db.query(ProgramStudi).filter_by(kode="SIF").first()

        if not program:
            program = ProgramStudi(
                kode="SIF",
                nama="Sistem Informasi",
                fakultas="FSTI",
            )
            db.add(program)

        # Data awal jalur masuk
        jalur = db.query(JalurMasuk).filter_by(
            nama="Reguler"
        ).first()

        if not jalur:
            jalur = JalurMasuk(nama="Reguler")
            db.add(jalur)

        db.commit()

        print("Data referensi berhasil disiapkan.")

        print("\nProgram Studi:")
        for p in db.query(ProgramStudi).all():
            print(f"ID: {p.id} | Kode: {p.kode} | Nama: {p.nama}")

        print("\nJalur Masuk:")
        for j in db.query(JalurMasuk).all():
            print(f"ID: {j.id} | Nama: {j.nama}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
