from chat_with_doc.interfaces.llm_api import LlmApi

class OpenAiLlm(LlmApi):
    """ OpenAI implementation of the LLM API interface. """
    
    def __init__(self):
        # TODO: Add configuration parameters
        pass
    
    def query(self, prompt: str) -> str:
        """ Implementation of query method for OpenAI's API.
        
        Args:
            prompt: The input prompt to send to OpenAI
            
        Returns:
            str: The model's response
        """
        # TODO: Implement actual OpenAI API call
        return ""
