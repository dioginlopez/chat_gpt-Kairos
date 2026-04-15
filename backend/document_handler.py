import os

def process_document(filename: str, content: bytes) -> str:
    """Process uploaded document and extract text"""
    file_ext = filename.split('.')[-1].lower()
    
    allowed_types = ["pdf", "txt", "docx", "md"]
    if file_ext not in allowed_types:
        raise ValueError(f"Tipo de arquivo não permitido: {file_ext}")
    
    try:
        if file_ext == "txt":
            return content.decode("utf-8")
        
        elif file_ext == "md":
            return content.decode("utf-8")
        
        elif file_ext == "pdf":
            return extract_pdf_text(content)
        
        elif file_ext == "docx":
            return extract_docx_text(content)
        
        else:
            return content.decode("utf-8", errors="ignore")
    
    except Exception as e:
        raise ValueError(f"Erro ao processar documento: {str(e)}")

def extract_pdf_text(content: bytes) -> str:
    """Extract text from PDF file"""
    try:
        import PyPDF2
        import io
        
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text
    
    except ImportError:
        raise ValueError("PyPDF2 não está instalado. Instale com: pip install PyPDF2")

def extract_docx_text(content: bytes) -> str:
    """Extract text from DOCX file"""
    try:
        from docx import Document
        import io
        
        doc = Document(io.BytesIO(content))
        text = ""
        
        for para in doc.paragraphs:
            text += para.text + "\n"
        
        return text
    
    except ImportError:
        raise ValueError("python-docx não está instalado. Instale com: pip install python-docx")
