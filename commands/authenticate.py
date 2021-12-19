import typer
import random
import string
import os

def authenticate():
    token = "".join(random.choices(string.ascii_letters + string.digits, k=40))
    cli_url = os.environ.get("APP_URL") + "/cli/session/new/" + token
    typer.launch(cli_url)