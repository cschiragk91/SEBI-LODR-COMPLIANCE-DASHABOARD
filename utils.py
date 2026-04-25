from datetime import datetime, timedelta

def get_quarter_end(today):
    quarter_month = ((today.month - 1)//3 + 1)*3
    return datetime(today.year, quarter_month, 1)

def calculate_due(item):
    today = datetime.today()

    if item["frequency"] == "quarterly":
        q_end = get_quarter_end(today)
        return q_end + timedelta(days=item["due_days"])

    elif item["frequency"] == "yearly":
        fy_end = datetime(today.year, 3, 31)
        return fy_end + timedelta(days=item["due_days"])

    elif item["frequency"] == "yearly_fixed":
        day, month = map(int, item["fixed_date"].split("-"))
        return datetime(today.year, month, day)

    return None
