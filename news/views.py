from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import JsonResponse
import requests
import json
from news.models import *

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def generate_random_data():
    url = 'http://localhost:3000/news'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    
    # print (payload)
    print ("type of payload is: ", type(payload))
    for data in payload:
        # print("title: ", data['title'])
        # print("content: ", data['content'])
        ElasticNews.objects.create(
            title = data['title'],
            content = data['content']
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})
    # return HttpResponse("Hello, the world")


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)