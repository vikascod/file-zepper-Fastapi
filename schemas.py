from pydantic import BaseModel

class CompressedFile(BaseModel):
    file_path: str
    file_data: bytes

class DecompressedFile(BaseModel):
    file_path: str
    file_data: str
