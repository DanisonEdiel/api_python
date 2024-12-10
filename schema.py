import graphene

# Modelo Simulado (Lista de Usuarios)
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

# Query Principal
class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        # Devuelve una lista de usuarios simulados
        return [
            User(id="1", name="Alice", email="alice@example.com"),
            User(id="2", name="Bob", email="bob@example.com"),
        ]

schema = graphene.Schema(query=Query)
