from commands.authenticate import authenticate
from utilities.auth import store_auth_token
from callbacks.maui import maui_callback
import typer
import config

app = typer.Typer(name="maui-cli", help="CLI tool for the Maui application. Visit https://mauii.app to find out more.")

# Loading the relevant config as environment variables
config.set()

@app.callback(invoke_without_command=True)
def callback():
    maui_callback()

if __name__ == '__main__':
    app()
