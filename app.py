from commands.add import add_expense
from commands.view import view_expenses
from callbacks.maui import maui_callback
from middlewares.middlewares import auth_middleware
from datetime import datetime
from utilities.date import generate_current_date
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
        generate_current_date(),
        "--date",
        "-d",
        formats=["%Y-%m-%d"],
        help="Date this expense was incurred",
    ),
):
    """add a new expense"""
    add_expense(name, amount, date)


@auth_middleware
@app.command("view")
def cli_view_expenses(
    date: datetime = typer.Option(
        generate_current_date(),
        "--date",
        "-d",
        formats=["%Y-%m-%d"],
        help="Date this expense was incurred",
    )
):
    """view expenses"""
    view_expenses(date)


if __name__ == "__main__":
    app()
