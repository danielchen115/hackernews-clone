import graphene
from graphene_django import DjangoObjectType
from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    link = graphene.Field(LinkType, link_id=graphene.String())

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_link(self, info, link_id):
        return Link.objects.get(pk=link_id)
