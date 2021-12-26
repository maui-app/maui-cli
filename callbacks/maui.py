from utilities.auth import store_auth_token, fetch_auth_token
from commands.authenticate import authenticate
import typer

# Callback for the CLI app. Displays a default message if user is
# authenticated. If user is not authenticated, it tries to
# authenticate them.
def maui_callback():
    token = fetch_auth_token()

    if token is None:
        auth_token = authenticate()
        if auth_token is None:
            return typer.echo("There was a problem authenticating. Trying again...")

        store_auth_token(auth_token)
        return typer.echo(
            "Authenticated successfully. Run maui --help to see a list of available commands"
        )
