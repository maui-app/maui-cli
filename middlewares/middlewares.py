from utilities.auth import fetch_auth_token
import functools
import typer


def auth_middleware(command):
    @functools.wraps(command)
    def middleware(kwargs):
        if fetch_auth_token() is None:
            return typer.secho("You are not authenticated.", fg=typer.colors.RED)

        return command(**kwargs)

    return middleware
