def filter_by_category(data, category):
    """Return only rows matching the given category."""
    return [row for row in data if row["category"] == category]

def filter_by_value(data, field, min_value):
    """Return only rows where field >= min_value."""
    return [row for row in data if float(row[field]) >= min_value]