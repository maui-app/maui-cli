from datetime import datetime, date as dt
from client import get as get_client
from graphql_operations.expense import DAILYEXPENSES
from utilities.date import get_formatted_date_string
import typer


def view_expenses(date: datetime):
    try:
        client = get_client()
        variables = {"date": str(date).split(" ")[0], "all": True}
        response = client.execute(DAILYEXPENSES, variable_values=variables)[
            "dailyExpenses"
        ]
        text = parse_expenses_text(response, date)
        typer.echo(text)
    except Exception as exception:
        typer.echo(exception)


def parse_expenses_text(data, date: datetime):
    expenses = data.get("expenses")
    day = (
        "today"
        if str(date).split(" ")[0] == str(dt.today())
        else "on {0}".format(get_formatted_date_string(date))
    )

    if len(expenses) == 0:
        return f"No expenses found for {day}"

    total = expenses[0]["user"]["currency"] + "{:,}".format(data.get("sum"))
    text = f"{total} spent {day}. Here is the breakdown\n"
    index = 1

    for expense in expenses:
        name = expense["name"]
        amount = expense["user"]["currency"] + "{:,}".format(expense["amount"])
        new_line = "" if index == len(expenses) else "\n"
        text = text + "{0} - {1}{2}".format(name, amount, new_line)
        index += 1

    return text
