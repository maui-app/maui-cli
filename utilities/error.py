from utilities.date import get_month_string
from datetime import datetime
import typer


def error_handler(error_id=None, date: datetime = None):
    text = "There was a problem carrying out the operation."

    if error_id == "PeriodIncomeDoesNotExist":
        text = "You do not have income recorded for {0}.".format(get_month_string(date))

    typer.secho(text, fg=typer.colors.RED)
