from utilities.auth import fetch_auth_token
import functools
import typer


def auth_middleware(command):
    @functools.wraps(command)
    def middleware(kwargs):
        typer.echo("Olamileke")
        if fetch_auth_token() is None:
            return typer.secho(
                "You are not authenticated.", bg=typer.colors.RED, fg=typer.colors.WHITE
            )

        return command(**kwargs)

    return middleware
