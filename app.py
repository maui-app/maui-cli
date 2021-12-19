from commands.authenticate import authenticate
import typer
import config

app = typer.Typer(name="maui-cli", help="CLI tool for the Maui application. Visit https://mauii.app to find out more.")

# Loading the relevant config as environment variables
config.set()

@app.callback(invoke_without_command=True)
def callback():
    authenticate()

if __name__ == '__main__':
    app()
