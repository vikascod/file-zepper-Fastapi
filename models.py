from database import Base
from sqlalchemy import Column, Integer, String, LargeBinary

class CompressedFile(Base):
    __tablename__ = 'compressed_files'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    compressed_file = Column(LargeBinary)

    def __repr__(self):
        return f"<CompressedFile(id={self.id}, original_filename='{self.original_filename}', compressed_file='{self.compressed_file}')>"

class DecompressedFile(Base):
    __tablename__ = 'decompressed_files'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    decompressed_file = Column(LargeBinary)

    def __repr__(self):
        return f"<DecompressedFile(id={self.id}, original_filename='{self.original_filename}', decompressed_file='{self.decompressed_file}')>"
