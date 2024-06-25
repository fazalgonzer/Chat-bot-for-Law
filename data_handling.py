from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_community.document_loaders import PyPDFDirectoryLoader
import os 
groq_api_key=os.getenv('GROQ_API_KEY')


embeddings=HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
loader=PyPDFDirectoryLoader("pdf") ## Data Ingestion
docs=loader.load() ## Document Loading
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) ## Chunk Creation
final_documents=text_splitter.split_documents(docs) #splitting
vectors=FAISS.from_documents(final_documents,embeddings) #vector OpenAI embeddings


