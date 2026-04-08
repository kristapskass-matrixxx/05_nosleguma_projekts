import csv

def export_csv(data, filename="export.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Date",
            "Category",
            "Income",
            "Expense",
            "Balance",
            "Description"
        ])

        for d in data:
            writer.writerow([
                d.get("date"),
                d.get("category"),
                d.get("income"),
                d.get("expense"),
                d.get("balance"),
                d.get("description")
            ])