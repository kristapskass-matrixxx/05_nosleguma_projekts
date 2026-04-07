import csv

def export_to_csv(data, filename):
    """Saglabā datus CSV failā"""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Pirmais rads: galvenes
        writer.writerow(data[0].keys())
        # Dati
        for row in data:
            writer.writerow(row.values())

# Piemēra dati
if __name__ == "__main__":
    sample_data = [
        {"Name": "Alice", "Age": 30, "City": "Riga"},
        {"Name": "Bob", "Age": 25, "City": "Liepaja"}
    ]
    export_to_csv(sample_data, "output.csv")
    print("Dati saglabāti output.csv")