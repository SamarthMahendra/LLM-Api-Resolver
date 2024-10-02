from django.db import models
import chromadb
from chromadb.config import Settings as chroma_settings
# import django Settings
from django.conf import settings
from sentence_transformers import SentenceTransformer

# Create your models here.
from django.contrib import admin

class Api(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    description = models.TextField()
    Parameters = models.TextField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # convert it into
    # **Description**: Retrieves the current weather information for a specified city.
    # **API Path**: /weather/current
    # **Method**: GET
    # **Parameters**:
    #   - city (string): Name of the city.
    #   - units (string, optional): Units of measurement (metric or imperial).
    # **Headers**:
    #   - Authorization: Bearer token.
    # **Example Request**:
    #   GET /weather/current?city=London&units=metric
    # **Example Response**:
    #   {
    #     "city": "London",
    #     "temperature": 15,
    #     "units": "metric",
    #     "description": "Partly cloudy"
    #   }

    # save it to chroma db
    def save(self, *args, **kwargs):
        super(Api, self).save(*args, **kwargs)
        data = """
         Description**: __Description__
         Path: __Path__
         Method: __Method__
         Parameters:
         __Parameters__
         """
        data = data.replace('__Description__', self.description)
        data = data.replace('__Path__', self.url)
        data = data.replace('__Method__', 'GET')
        data = data.replace('__Parameters__', self.Parameters)
        # save to db

        client = chromadb.Client()

        # model = SentenceTransformer('all-MiniLM-L6-v2')
        # api_documents = [...]  # List of your API documents as strings
        # embeddings = model.encode(api_documents)

        api_documents = [data]

        client = chromadb.Client()
        collection = client.create_collection(name='api_docs')

        for doc_id, data in enumerate(api_documents):
            collection.add(
                documents=[data],
                ids=[str(doc_id)]
            )
        print('Api saved to chromaDB')
        question = "show list of todos"
        client = chromadb.Client()
        # get collection
        collection = client.get_collection('api_docs')
        results = collection.query(
            query_texts = [question],
            n_results=1
        )
        relevant_doc = str(results)
        print(relevant_doc)




