from datetime import datetime
from client import get as get_client
from graphql_operations.expense import ADDEXPENSE
import typer

def add_expense(name: str, amount: float, date: datetime):
    try:
        client = get_client()
        variables = { "name": name, "amount": amount, "date": str(date).split(' ')[0] }
        data = client.execute(ADDEXPENSE, variable_values=variables)['addExpense']
        currency = data.get("expense").get("user").get("currency")
        total = currency + "{:,}".format(data.get("sum"))
        text = f"Recorded {name} successfully. That brings your total spent to {total}."
        typer.echo(text)
    except Exception as exception:
        typer.echo(exception)