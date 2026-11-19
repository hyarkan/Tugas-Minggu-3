from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models import CalonMahasiswa, JalurMasuk, ProgramStudi, StatusPMB
from app.schemas.register import RegisterRequest

class EmailAlreadyRegistered(Exception):
    pass

class InvalidReference(Exception):
    pass

def register_candidate(db: Session, payload: RegisterRequest) -> CalonMahasiswa:
    if db.scalar(select(CalonMahasiswa.id).where(CalonMahasiswa.email == str(payload.email))):
        raise EmailAlreadyRegistered

    if db.get(ProgramStudi, payload.program_studi_id) is None:
        raise InvalidReference("Program studi tidak ditemukan.")
    if db.get(JalurMasuk, payload.jalur_masuk_id) is None:
        raise InvalidReference("Jalur masuk tidak ditemukan.")

    candidate = CalonMahasiswa(
        nama_lengkap=payload.nama_lengkap,
        email=str(payload.email),
        phone=payload.phone,
        tanggal_lahir=payload.tanggal_lahir,
        alamat=payload.alamat,
        program_studi_id=payload.program_studi_id,
        jalur_masuk_id=payload.jalur_masuk_id,
        status=StatusPMB.pending,
    )
    db.add(candidate)
    try:
        db.commit()
        db.refresh(candidate)
    except IntegrityError as exc:
        db.rollback()
        # Covers concurrent requests that both passed the pre-check.
        if "email" in str(exc).lower() or "unique" in str(exc).lower():
            raise EmailAlreadyRegistered from exc
        raise InvalidReference("Referensi data tidak valid.") from exc
    return candidate
