from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Union

from langchain.schema import Document


class BaseRetriever(ABC):
    """Base class for document retrievers."""
    
    @abstractmethod
    def add_documents(self, file_paths: List[Union[str, Path]], **kwargs) -> None:
        """
        Add documents to the retriever's database.
        
        Args:
            file_paths: List of paths to documents
            **kwargs: Additional arguments for document processing
        """
        pass
    
    @abstractmethod
    def get_relevant_documents(self, query: str, **kwargs) -> List[Document]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: The search query
            **kwargs: Additional arguments for retrieval
            
        Returns:
            List[Document]: List of relevant documents
        """
        pass
    
    # @abstractmethod
    # def delete_documents(self, document_ids: List[str]) -> None:
    #     """
    #     Delete documents from the retriever's database.
    #
    #     Args:
    #         document_ids: List of document IDs to delete
    #     """
    #     pass