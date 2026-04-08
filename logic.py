from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def calculate_balance(income, expense):
    return income - expense


def category_summary(data):
    summary = {}

    for d in data:
        cat = d.get("category", "N/A")
        summary[cat] = summary.get(cat, 0) + d.get("expense", 0)

    return summary


def filter_by_month(data, month):
    # month formāts: "2026-04"
    return [
        d for d in data
        if d.get("date", "").startswith(month)
    ]