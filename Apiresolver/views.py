from django.shortcuts import render

# Create your views here.
import chromadb
from django.conf import settings
from rest_framework.response import Response
import dill
from chromadb.config import Settings as chroma_settings




# fetch api for a question from chromaDB
from rest_framework import viewsets
from rest_framework.decorators import api_view
from sentence_transformers import SentenceTransformer


@api_view(['GET'])
def ApiDetail(request, question):
    if question:
        client = chromadb.PersistentClient(path='chroma_db/')

        collection = client.get_or_create_collection(name="test")
        results = collection.query(
            query_texts=[question],
            n_results=1
        )
    desc = results["documents"][0]
    # ['\n         Description**: to get all items in todo.\n         Path: todo/\n         Method: GET\n         Parameters:\n         \n         ']

    import re
    path = re.search('Path: (.*)', str(desc))
    # break by newline
    pattern = r"^(.*?)\\n"

    # Applying the regex
    path = re.search(pattern, str(path))

    # Extracting the matched part (if exists)
    if path:
        path = path.group(1)
        path = path.match.replace(' ', '')
        path = path.strip()
        path = path[4:]


    method = re.search('Method: (.*)', str(desc))
    # Applying the regex
    method = re.search(pattern, str(method))

    # Extracting the matched part (if exists)
    if method:
        method = method.group(1)
        method = method.match.replace(' ', '')
        method = method.strip()
        method = method[7:]
    return Response({
        'question': question,
        'answer': results["documents"][0]
    })