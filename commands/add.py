from datetime import datetime, date as dt
from client import get as get_client
from graphql_operations.expense import ADDEXPENSE
from utilities.date import get_formatted_date_string
from utilities.error import error_handler
import typer


def add_expense(name: str, amount: float, date: datetime):
    try:
        client = get_client()
        variables = {"name": name, "amount": amount, "date": str(date).split(" ")[0]}
        data = client.execute(ADDEXPENSE, variable_values=variables)["addExpense"]
        currency = data.get("expense").get("user").get("currency")
        total = currency + "{:,}".format(data.get("sum"))
        day = (
            "today"
            if str(dt.today()) == str(date).split(" ")[0]
            else "on {0}".format(get_formatted_date_string(date))
        )
        text = f"Recorded {name} successfully. That brings your total spent {day} to {total}."
        typer.echo(text)
    except Exception as exception:
        typer.echo(exception)
        error_handler()
