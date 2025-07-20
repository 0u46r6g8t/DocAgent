import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.Embedder import Embedders
from src.Config import Config

load_dotenv()

class Agent(Config):
    def __init__(self):
        super().__init__()
        self._agent = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0
        )
        self._messages = []
        self.embedders = Embedders()
    
    def set_question(self, question: str):
        """Set the question for the agent."""
        if not question:
            raise ValueError("Question cannot be empty.")
        
        self._question = question
    
    def get_message(self,context):
        """Set the message for the agent."""

        messages = [
            {"role": "system", "content": "Answer the question based on the provided context."},
            {"role": "user", "content": f"{self._question}\n\n{context}"}
        ]
        
        return messages

    def __invoke(self, message):
        """Invoke the agent with the provided message."""
        
        if not self._agent:
            raise ValueError("Agent is not initialized. Please initialize the agent before invoking.")
        
        if not message:
            raise ValueError("Message cannot be empty. Please provide a valid message.")
        
        return self._agent.invoke(message)

    def run(self, text: str):
        """Run the agent with a given prompt."""
        
        db = self.embedders.create(text)
        
        docs = db.similarity_search(self._question)

        if not docs:
            raise ValueError("No relevant documents found.")
            
        context = "\n".join([doc.page_content for doc in docs])

        message = self.get_message(context)

        return self.__invoke(message)
        