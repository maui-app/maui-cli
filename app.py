from commands.add import add_expense
from callbacks.maui import maui_callback
from middlewares.middlewares import auth_middleware
from datetime import datetime
import typer
import config

app = typer.Typer(
    name="maui-cli",
    help="CLI tool for the Maui application. Visit https://mauii.app to find out more.",
)

# Loading the relevant config as environment variables
config.set()


@app.callback(invoke_without_command=True)
def callback():
    maui_callback()


@auth_middleware
@app.command("add")
def cli_add_expense(
    name: str = typer.Argument(..., help="Name of the expense to add"),
    amount: float = typer.Argument(..., help="Amount spent on the expense being added"),
    date: datetime = typer.Option(
        datetime.now().strftime("%Y-%m-%d"),
        "--date",
        "-d",
        formats=["%Y-%m-%d"],
        help="Date this expense was incurred",
    ),
):
    """command to add new expenses"""
    add_expense(name, amount, date)


if __name__ == "__main__":
    app()
