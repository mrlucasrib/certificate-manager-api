from fastapi import FastAPI, File, UploadFile
import csv
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.requests import Request

from starlette.responses import Response
from database import SessionLocal, engine
import crud, models

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db

@app.post("/uploadcertificates/")
async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        content = str((await file.read()).decode('utf-8'))
        lines = [str.split(line, ",") for line in content.split('\n')]
        crud.create_certificates(db, lines)
    except:
        pass
    return {"success": True}

def decrypt(encrypted, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))


@app.get("/certificate")
def get_certificate(issue_to: str, db: Session = Depends(get_db)):
    return crud.get_certificate_by_name(db, issue_to)