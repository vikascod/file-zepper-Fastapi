from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, status
from huffman import HuffmanCoding
from database import Base, engine, get_db
import schemas, models
from sqlalchemy.orm import Session
from typing import Optional

models.Base.metadata.create_all(engine)


app = FastAPI()

@app.post("/compress")
async def compress(file: UploadFile, db:Session=Depends(get_db)):
    h = HuffmanCoding(file.filename)
    output_path = h.compress()

    return {"file_path": output_path}

@app.post("/decompress")
async def decompress(file: UploadFile, db:Session=Depends(get_db)):
    h = HuffmanCoding(file.filename)
    decom_path = h.decompress(file.filename)

    return {"file_path": decom_path}



# @app.get("/compressed/files")
# async def get_files(skip: int = 0, limit: int = 100, search:Optional[str]="", db: Session = Depends(get_db)):
#     files = db.query(models.CompressedFile).filter(models.CompressedFile.filename.contains(search)).offset(skip).limit(limit).all()
#     return {"files": [files for file in files]}


# @app.get("/decompressed/files")
# async def get_files(skip: int = 0, limit: int = 100, search:Optional[str]="", db: Session = Depends(get_db)):
#     files = db.query(models.DecompressedFile).filter(models.CompressedFile.filename.contains(search)).offset(skip).limit(limit).all()
#     return {"files": [files for file in files]}