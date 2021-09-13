from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)

from .models import ElasticNews

PUBLISHER_INDEX = Index('elastic_news')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):

    id = fields.IntegerField(attr='id')
    fielddata=True
    title = fields.TextField(
        fields={
            'keyword':{
                'type': 'keyword',
            }
            
        }
    )
    content = fields.TextField(
        fields={
            'keyword': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = ElasticNews