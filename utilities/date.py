from datetime import datetime

now = datetime.now()

def generate_current_date():
    return now.strftime("%Y-%m-%d")


def get_formatted_date_string(date: datetime = now):
    dt = int(date.strftime("%d"))
    dt = get_day_suffix(dt)
    return "{0}, {1} {2}".format(
        date.strftime("%A"), dt, date.strftime("%B, %Y")
    )

def get_day_suffix(day: int):
    return (
        str(day) + "th"
        if 11 <= day <= 13
        else str(day) + {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    )
