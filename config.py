from dotenv import load_dotenv
import os.path as path

# Load the variables contained in the .env file into the environment
def set():
    directory = path.abspath(path.dirname(__file__))
    env_path = path.join(directory, '.env')
    load_dotenv(env_path)
