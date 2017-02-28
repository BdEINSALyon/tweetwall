import graphene
from graphene import ObjectType, Node, Schema, Field
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from . import models


class Message(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (Node,)
        filter_fields = {
            'text': ['exact', 'icontains', 'istartswith'],
            'author_name': ['exact', 'icontains', 'istartswith'],
            'author_username': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }


class Feed(DjangoObjectType):
    class Meta:
        model = models.Feed
        interfaces = (Node,)


class Provider(DjangoObjectType):
    class Meta:
        model = models.Provider
        interfaces = (Node,)
        exclude_fields = ['app_id', 'app_secret']


class Query(ObjectType):
    message = Field(Message)
    all_messages = DjangoFilterConnectionField(Message)

schema = graphene.Schema(query=Query)
