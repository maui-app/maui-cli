from commands.authenticate import authenticate
from utilities.file import store_auth_token
import typer
import config

app = typer.Typer(name="maui-cli", help="CLI tool for the Maui application. Visit https://mauii.app to find out more.")

# Loading the relevant config as environment variables
config.set()

@app.callback(invoke_without_command=True)
def callback():
    auth_token = authenticate()
    if auth_token is None:
        return typer.echo("There was a problem authenticating.")

    store_auth_token(auth_token)
    typer.echo("Authenticated successfully. Run maui --help to see a list of available commands")

if __name__ == '__main__':
    app()
