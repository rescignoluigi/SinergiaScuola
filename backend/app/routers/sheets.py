from fastapi import APIRouter
from app.google_sheets_manager import create_sheet, write_data

router = APIRouter(prefix="/sheets")

@router.post("/create")
def create():
    sheet_id = create_sheet("SinergiaScuola - Prova")
    write_data(sheet_id, "A1", [["Classe", "Docente", "Materia"]])
    return {"sheet_id": sheet_id}
