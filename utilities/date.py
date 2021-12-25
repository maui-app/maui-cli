from datetime import datetime


def generate_current_date():
    return datetime.now().strftime("%Y-%m-%d")
