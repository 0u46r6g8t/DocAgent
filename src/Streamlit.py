import streamlit as st
import PyPDF2
import re

from src.Agent import Agent

class StreamlitApp:
    """A simple Streamlit application class."""
    
    uploaded_file = None
    
    def __init__(self, title: str, name: str):
        self.name = name
        self.title = title
        
    def __setUploadedFile(self, file):
        """Set the uploaded file."""
        self.uploaded_file = file
        
    def __setFullText(self, text: str):
        """Set the full text extracted from the PDF."""
        self.full_text = self.__clearText(text)
        
    def get_full_text(self):
        """Get the full text extracted from the PDF."""
        return self.full_text
    
    def __clearText(self, text: str) -> str:
        """Clear the text by removing extra spaces and newlines."""
        texto_corrigido = re.sub(r'(?<![\.\!\?\:])\n(?!\n)', ' ', text)
        texto_corrigido = re.sub(r'\n{2,}', '\n\n', texto_corrigido)

        return re.sub(r'\s+', ' ', texto_corrigido.strip())
    
    def __readerUploadedFile(self):
        """Read the uploaded file."""
        pdf_reader = PyPDF2.PdfReader(self.uploaded_file)

        full_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()

            if text:
                full_text += text + "\n"
            else:
                st.write("Nenhum texto encontrado nesta página.")

        self.__setFullText(full_text)
        
        if self.get_full_text():
            st.subheader("Texto Extraído:")
            st.text_area("Texto do PDF", value=self.get_full_text(), height=300)
        else:
            st.warning("Nenhum texto foi extraído do PDF.")
            
    def run(self):
        """Run the Streamlit application."""
        st.title(self.title)
        st.set_page_config(page_title=self.title, layout="wide")
        
        st.write(f"Welcome to {self.name}!")
        
        # File uploader for PDF files
        self.__setUploadedFile(st.file_uploader("Choose a PDF file", type="pdf"))
        
        if self.uploaded_file is not None:
            st.success(f"File '{self.uploaded_file.name}' uploaded successfully!")

            # Read and display the content of the uploaded PDF file
            self.__readerUploadedFile()
            
            question = st.text_input("Enter your query here", placeholder="Type your question about the PDF...")
            
            st.button("Submit", on_click=lambda: st.write("Query submitted!"))
            
            if question:
                st.write(f"You asked: {question}")
                
                st.write("Processing your query...")
                
                agent = Agent()

                agent.set_question(question)
                
                try:
                    response = agent.run(self.get_full_text())

                    st.write("Response from the agent:")
                    st.text(response.content)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload a PDF file to continue.")