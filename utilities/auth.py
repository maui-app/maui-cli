from pathlib import Path
import typer
import json
import os

APP_NAME = "maui-cli"
app_dir = Path(typer.get_app_dir(APP_NAME))

# Method to check for the user's token in the maui config file.
def fetch_auth_token():
    config_path = app_dir / "config.json"

    if not app_dir.is_dir() or not config_path.is_file():
        return None

    with open(config_path, "r") as reader:
        data = json.load(reader)

    return data.get("token")


# Method to store the user's auth token in the maui-cli config
# file. This token will be used for subsequent api requests to
# the maui api
def store_auth_token(token: str):
    if not app_dir.is_dir():
        create_config_dir(app_dir)

    config_path = app_dir / "config.json"

    if not config_path.is_file():
        create_config_file(config_path)

    with open(config_path, "w") as writer:
        data = {"token": token}
        json.dump(data, writer)


# Method to create the directory for the maui-cli config file
# if it does not exist
def create_config_dir(dir_path: Path):
    os.makedirs(dir_path)


# Method to create the maui-cli config file if it does not exist
def create_config_file(config_path: Path):
    f = open(config_path, "x")
    f.close()
