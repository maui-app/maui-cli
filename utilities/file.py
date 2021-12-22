from pathlib import Path
import typer
import json
import os

APP_NAME = 'maui-cli'
app_dir = Path(typer.get_app_dir(APP_NAME))

def store_auth_token(token: str):
    if not app_dir.is_dir():
        create_config_dir(app_dir)

    config_path = app_dir / 'config.json'
    
    if not config_path.is_file():
        create_config_file(config_path)

    with open(config_path, "w") as writer:
        data = { "token": token }
        json.dump(data, writer)

def create_config_dir(dir_path: Path):
    os.makedirs(dir_path)
    
def create_config_file(config_path: Path):
    f = open(config_path, "x")
    f.close()
