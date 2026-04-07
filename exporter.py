import csv

def export_to_csv(data, filename):
    """Export list of dictionaries to a CSV file."""
    if not data:
        print("No data to export.")
        return
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data exported to {filename}")