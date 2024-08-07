import io
import base64
from typing import Optional
from pypdf import PdfReader
from pydantic import BaseModel, Field

class PDF_Ops(BaseModel):
    pdf_content: bytes
    pdf_reader: Optional[PdfReader] = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)

        pdf_io_bytes_content = io.BytesIO(self.pdf_content)
        self.pdf_reader = PdfReader(pdf_io_bytes_content)

    def get_page_text(self, page_number: int) -> str:
        if page_number < 1 or page_number > len(self.pdf_reader.pages):
            raise ValueError("Invalid page number")
        return self.pdf_reader.pages[page_number - 1].extract_text()

    def get_base64_pdf(self):
        return base64.b64encode(self.pdf_content).decode('utf-8')
    