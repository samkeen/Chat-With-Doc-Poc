from abc import ABC, abstractmethod

class LlmApi(ABC):
    """ Abstract interface for LLM API interactions. """
    
    @abstractmethod
    def query(self, prompt: str) -> str:
        """ Send a query to the LLM and return the response.
        
        Args:
            prompt: The input prompt to send to the LLM
            
        Returns:
            str: The LLM's response
        """
        pass
