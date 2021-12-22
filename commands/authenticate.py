from api.auth import fetch_auth_token
import typer
import random
import string
import time
import requests
import os

def authenticate():
    token = "".join(random.choices(string.ascii_letters + string.digits, k=40))
    cli_url = os.environ.get("APP_URL") + "/cli/" + token
    typer.echo("Opening up the Maui app for you to authenticate...")
    typer.launch(cli_url)
    return poll_auth(token)

def poll_auth(cli_token: str):
    time.sleep(8)
    i = 1
    try:
        while i < 5:
            response = fetch_auth_token(cli_token)
            if response['auth-token'] is not None:
                return response['auth-token']
            i += 1
            time.sleep(10)
        return None
    except requests.HTTPError:
        typer.echo("Problem with network connection. Retrying...")
