import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from typing import List, Dict

# load_dotenv()
api_key = st.secrets["GROQ_API_KEY"]
print(api_key)

# Initialize the embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
llm = Groq(model='llama-3.3-70b-versatile', api_key=api_key, temperature=0.1)

# Configure global settings
Settings.embed_model = embed_model
Settings.llm = llm

class CodeSearchSystem:
    def __init__(self, persist_dir: str):
        """
        Initialize the search system with a JSON file path.
        
        Args:
            json_path (str): Path to the JSON file containing Code, Title, and Definition fields
        """

        self.index = self._create_index(persist_dir)
    
    
    def _create_index(self, persist_dir: str) -> VectorStoreIndex:
        """
        load a vector store index from index store.
        """
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context=storage_context,)
        return index
    
    def search(self, query: str, prompt: str, top_k: int = 1) -> List[Dict[str, str]]:
        """
        Search for entries matching the query and return their codes.
        
        Args:
            query (str): Search query
            top_k (int): Number of top results to return
            
        Returns:
            List[Dict[str, str]]: List of dictionaries containing code and title
        """
        query_engine = self.index.as_query_engine(
            similarity_top_k=top_k,
        )
        query_engine.update_prompts(prompt)
        response = query_engine.query(query)
        results = []
        
        # Extract source nodes from the response
        source_nodes = response.source_nodes
        
        for node in source_nodes:
            results.append({
                'code': node.metadata['code'],
                'title': node.metadata['title'],
                'definition': node.metadata['definition'],
                'includes': node.metadata['includes'],
                'excludes': node.metadata['excludes'],
                'score': node.score if hasattr(node, 'score') else None
            })
        
        return results
    
