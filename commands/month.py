from client import get as get_client
from graphql_operations.income import CURRENTMONTHINCOME
from utilities.date import get_month_string
from datetime import datetime
import typer


def view_month(date: datetime):
    try:
        client = get_client()
        variables = {"date": str(date).split(" ")[0]}
        response = client.execute(CURRENTMONTHINCOME, variable_values=variables)[
            "currentMonthIncome"
        ]
        text = parse_this_month_text(response, date)
        typer.echo(text)
    except Exception as exception:
        typer.echo(exception)


def parse_this_month_text(data, date: datetime):
    total, remainder, percent_remainder, expenses_count, user = [
        data[k]
        for k in ("total", "remainder", "percent_remainder", "expenses_count", "user")
    ]

    formatted_total = user["currency"] + "{:,}".format(total)
    formatted_spent = user["currency"] + "{:,}".format(total - remainder)
    formatted_remainder = user["currency"] + "{:,}".format(remainder)
    percent_spent = 100 - (float(percent_remainder[:-1]))
    percent_spent = "{:.2f}".format(percent_spent) + "%"

    text = "Here is your roundup for {0}\n".format(get_month_string(date))
    text += "{0} in total income\n".format(formatted_total)
    text += "{0} spent {1}\n".format(formatted_spent, percent_spent)
    text += "{0} remaining {1}\n".format(formatted_remainder, percent_remainder)
    text += "{0} unique expenses".format(expenses_count)

    return text
