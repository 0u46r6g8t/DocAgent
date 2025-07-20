import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class to manage environment variables."""
    
    def __init__(self):
        os.environ['OPENAI_API_KEY'] = os.getenv('OPEN_AI_KEY')
        
    