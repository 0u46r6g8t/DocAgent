from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

class Embedders:
    def __init__(self):
        pass

    def __setChunks(self, chunks: list):
        """Set the chunks for embedding."""
        self.chunks = chunks

    def __createDocument(self, text: str) -> Document:
        """Create a Document object from the text."""
        doc = Document(page_content=text)
        return [doc]

    def get_chunks(self):
        """Get the chunks for embedding."""
        return self.chunks

    def create(self, text: str):
        """Embed the text using a text splitter."""
        
        try:
            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

            document = self.__createDocument(text)
            
            chunks = splitter.split_documents(document)
            
            self.__setChunks(chunks)
            
            return FAISS.from_documents(chunks, OpenAIEmbeddings())
        except Exception as e:
            print(e)
            raise ValueError(f"Error while splitting text: {e}")
            