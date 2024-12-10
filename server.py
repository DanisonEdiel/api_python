from fastapi import FastAPI, Header, Request
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware

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

users_data = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
]

query = QueryType()

@query.field("user")
def resolve_user(_, info, id):
    return next((user for user in users_data if user["id"] == id), None)

@query.field("users")
def resolve_users(_, info):
    return users_data

schema = make_executable_schema(type_defs, query)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQL(schema, debug=True))

@app.get("/headers")
def check_headers(authorization: str = Header(None)):
    return {"Authorization": authorization}

@app.post("/webhook")
async def receive_webhook(request: Request):
    """
    Recibe y procesa eventos enviados al webhook
    """
    payload = await request.json() 
    print("Webhook received:", payload)

    event_type = payload.get("event", "unknown")
    if event_type == "payment_successful":
        order_id = payload["data"].get("order_id")
        amount = payload["data"].get("amount")
        print(f"Payment successful for order {order_id}: ${amount}")
    else:
        print("Unhandled event type:", event_type)

    return {"status": "success", "event": event_type}
