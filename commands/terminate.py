from utilities.auth import app_dir
import typer
import os


def terminate():
    config_path = app_dir / "config.json"
    os.remove(config_path)
    typer.echo("Your session has been ended.")
