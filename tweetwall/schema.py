import graphene
from graphene_django.debug import DjangoDebug
from social.graphql import Query as SocialQuery


class Query(SocialQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
