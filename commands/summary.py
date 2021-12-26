from client import get as get_client
from graphql_operations.income import INCOMESTATS
import typer


def view_summary():
    try:
        client = get_client()
        response = client.execute(INCOMESTATS)["incomeStats"]
        text = parse_summary_text(response)
        typer.echo(text)
    except Exception as exception:
        typer.echo(exception)


def parse_summary_text(data):
    income_total, income_spent, income_remainder, currency = [
        data[k]
        for k in ("income_total", "income_spent", "income_remainder", "currency")
    ]

    formatted_total = currency + "{:,}".format(income_total)
    formatted_spent = currency + "{:,}".format(income_spent)
    formatted_remainder = currency + "{:,}".format(income_remainder)

    text = "Here are your income statistics since you started using Maui.\n"
    text += f"Total Income Earned - {formatted_total}\n"
    text += f"Income Spent - {formatted_spent}\n"
    text += f"Income Remaining - {formatted_remainder}"
    
    return text
