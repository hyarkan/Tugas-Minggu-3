from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.register import RegisterRequest, RegisterResponse
from app.services.pmb_service import EmailAlreadyRegistered, InvalidReference, register_candidate

router = APIRouter(prefix="/api/pmb", tags=["PMB"])

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    try:
        return register_candidate(db, payload)
    except EmailAlreadyRegistered:
        raise HTTPException(status_code=409, detail="Email sudah terdaftar.")
    except InvalidReference as exc:
        raise HTTPException(status_code=400, detail=str(exc))
