# Doc Reader - PDF Question Answering App

## Description
Doc Reader is a Streamlit-based web application that allows users to upload PDF documents, extract their text content, and ask questions about the content. Powered by OpenAI's GPT-3.5-turbo model and Langchain embeddings, the app provides intelligent answers based on the uploaded document's text.

## Features
- Upload PDF files and extract text content
- Display extracted text for review
- Ask questions related to the PDF content
- Receive AI-generated answers based on document context
- User-friendly interface built with Streamlit

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key (You need to sign up at [OpenAI](https://openai.com/) and get an API key)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following content:
   ```
   OPEN_AI_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run main.py
   ```

2. Open the URL provided by Streamlit (usually http://localhost:8501) in your web browser.

3. Upload a PDF file using the file uploader.

4. View the extracted text displayed on the page.

5. Enter your question about the PDF content in the input box and submit.

6. View the AI-generated response based on your query.

## Technologies Used
- Python
- Streamlit
- PyPDF2
- Langchain (Text splitting, embeddings, FAISS vector store)
- OpenAI GPT-3.5-turbo API
- dotenv for environment variable management

## Contact
Created by Gustavo Silva Quieregato.  
Feel free to reach out for questions or collaboration.
