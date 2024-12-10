from fastapi import FastAPI, Header
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware


# Define el esquema con soporte para variables
type_defs = """
    type Query {
        user(id: ID!): User
        users: [User!]!
    }

    type User {
        id: ID!
        name: String!
        email: String!
    }
"""

# Datos simulados
users_data = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
]

# Resolver para las consultas
query = QueryType()

@query.field("user")
def resolve_user(_, info, id):
    # Datos simulados
    users_data = [
        {"id": "1", "name": "Alice", "email": "alice@example.com"},
        {"id": "2", "name": "Bob", "email": "bob@example.com"},
    ]
    # Busca un usuario por ID
    return next((user for user in users_data if user["id"] == id), None)


@query.field("users")
def resolve_users(_, info):
    return users_data

# Crear el esquema ejecutable
schema = make_executable_schema(type_defs, query)

# Configurar la aplicación FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.add_route("/graphql", GraphQL(schema, debug=True))

# Prueba de Headers
@app.get("/headers")
def check_headers(authorization: str = Header(None)):
    return {"Authorization": authorization}
