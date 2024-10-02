from django.shortcuts import render

# Create your views here.
import chromadb
from django.conf import settings
from rest_framework.response import Response




# fetch api for a question from chromaDB
from rest_framework import viewsets
from rest_framework.decorators import api_view
from sentence_transformers import SentenceTransformer


@api_view(['GET'])
def ApiDetail(request, question):
    if question:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        question_embedding = model.encode([question])
        client = chromadb.Client()
        # get collection
        collection = client.get_collection('api_docs')
        results = collection.query(
            embeddings=question_embedding,
            n_results=1
        )
        relevant_doc = results['metadatas'][0]['document']
    return Response({
        'question': question,
        'answer': relevant_doc
    })