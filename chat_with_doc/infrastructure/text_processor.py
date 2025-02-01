from typing import BinaryIO
from chat_with_doc.domain.document import Document, DocumentProcessor

class TextProcessor(DocumentProcessor):
    """Processor for text and markdown files."""
    
    SUPPORTED_EXTENSIONS = {'.txt', '.md'}
    
    def process(self, file: BinaryIO, filename: str) -> Document:
        """Process a text or markdown file and extract its content.
        
        Args:
            file: File-like object containing the text
            filename: Name of the file
            
        Returns:
            Document: Processed document with extracted content
            
        Raises:
            ValueError: If file type is not supported
        """
        ext = filename[filename.rfind('.'):].lower() if '.' in filename else ''
        if ext not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Only {', '.join(self.SUPPORTED_EXTENSIONS)} files are supported")
        
        content = file.read().decode('utf-8')
        return Document(
            content=content,
            name=filename,
            type='text/plain' if ext == '.txt' else 'text/markdown'
        )
