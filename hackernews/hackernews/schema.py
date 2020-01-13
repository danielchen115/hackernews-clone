import graphene
import links.schema


class Query(links.schema.Querym, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
