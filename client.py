from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from utilities.auth import fetch_auth_token
import os

def get():
    transport = RequestsHTTPTransport(
        url=os.environ.get("GRAPHQL_URL"),
        use_json=True,
        headers=get_headers(),
        verify=False,
        retries=3,
    )
    client = Client(
        transport=transport,
        fetch_schema_from_transport=True,
    )
    return client


def get_headers():
    headers = {"Content-Type": "application/json"}
    token = fetch_auth_token()
    if token:
        headers["Authorization"] = "Bearer " + token
    return headers