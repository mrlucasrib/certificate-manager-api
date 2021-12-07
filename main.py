from fastapi import FastAPI, File, UploadFile
import csv
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.requests import Request
import os
from starlette.responses import Response
from database import SessionLocal, engine
import base64
import hashlib
import os

# from Crypto import Random
# from Crypto.Cipher import AES

# from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
import crud, models
import random

# BLOCK_SIZE = 64
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
#     BLOCK_SIZE - len(s) % BLOCK_SIZE
# )
# unpad = lambda s: s[: -ord(s[len(s) - 1 :])]

# KEY = "ABCDEFGHIJKLMNOP".encode()
# iv = os.urandom(16)

#''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

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
 

    # content = await file.read()

    # print(decrypt(content, KEY))

    # print(str(decd.decode("utf-8")))
    # lines = [str.split(line, ",") for line in content.split('\n')]
    # print(crud.create_certificates(db, lines))

    return {"success": True, 
    "input": file.filename}


def decrypt(encrypted, passphrase):
    IV = Random.new().read(16)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))

# def decrypt(enc: str, password: str) -> str:
#     # private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     enc_b64decoded = enc#base64.b64decode(enc)
#     iv = enc_b64decoded[:16]
#     cipher = Cipher(algorithms.AES(password), modes.CBC(iv))
#     decryptor = cipher.decryptor()
#     decrypt_message = decryptor.update(enc_b64decoded[16:]) + decryptor.finalize()
#     decrypt_message = unpad(decrypt_message)
#     return decrypt_message


@app.get("/certificate")
def get_certificate(name: str, db: Session = Depends(get_db)):
    return crud.get_certificate_by_name(db, name)
