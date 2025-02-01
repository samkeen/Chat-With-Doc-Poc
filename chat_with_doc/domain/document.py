from abc import ABC, abstractmethod
from typing import BinaryIO
from pydantic import BaseModel

class Document(BaseModel):
    """Domain model representing a document."""
    content: str
    name: str
    type: str

class DocumentProcessor(ABC):
    """Abstract base class for document processing."""
    
    @abstractmethod
    def process(self, file: BinaryIO, filename: str) -> Document:
        """Process a document file and extract its content.
        
        Args:
            file: File-like object containing the document
            filename: Name of the file
            
        Returns:
            Document: Processed document with extracted content
            
        Raises:
            ValueError: If file type is not supported
        """
        pass
