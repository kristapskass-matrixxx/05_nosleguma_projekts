from storage import load_data, save_data
from logic import validate_date, calculate_balance
from export import export_csv

def add_record(data):
    date = input("Datums (YYYY-MM-DD): ")

    if not validate_date(date):
        print("❌ Nederīgs datums")
        return

    print("Kategorija:")
    print("1) Pārtika")
    print("2) Transports")
    print("3) Izglītība")
    print("4) Izprieca")

    categories = {
        "1": "Pārtika",
        "2": "Transports",
        "3": "Izglītība",
        "4": "Izprieca"
    }

    cat = categories.get(input("Izvēlies: "), "Cits")

    income = float(input("Ienākumi: "))
    expense = float(input("Izdevumi: "))

    description = input("Apraksts: ")

    balance = calculate_balance(income, expense)

    record = {
        "date": date,
        "category": cat,
        "income": income,
        "expense": expense,
        "balance": balance,
        "description": description
    }

    data.append(record)
    save_data(data)

    print(f"✓ Saglabāts | Bilance: {balance} EUR")


def show_summary(data):
    total_income = sum(d.get("income", 0) for d in data)
    total_expense = sum(d.get("expense", 0) for d in data)

    print("\n===== KOPSAVILKUMS =====")
    print(f"Ienākumi: {total_income}")
    print(f"Izdevumi: {total_expense}")
    print(f"Bilance: {total_income - total_expense}")
    print("========================\n")


def main():
    data = load_data()

    while True:
        print("\n1) Pievienot ierakstu")
        print("2) Eksportēt CSV")
        print("3) Kopsavilkums")
        print("4) Beigt")

        choice = input("Izvēlies: ")

        if choice == "1":
            add_record(data)
        elif choice == "2":
            export_csv(data)
            print("✓ CSV eksportēts")
        elif choice == "3":
            show_summary(data)
        elif choice == "4":
            break


if __name__ == "__main__":
    main()