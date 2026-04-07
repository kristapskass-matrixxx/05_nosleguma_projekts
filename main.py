from exporter import export_to_csv

def get_data():
    """Simulē datu iegūšanu no lietotāja"""
    return [
        {"Name": "Alice", "Age": 30, "City": "Riga"},
        {"Name": "Bob", "Age": 25, "City": "Liepaja"}
    ]

if __name__ == "__main__":
    data = get_data()
    export_to_csv(data, "output.csv")
    print("Programma veiksmīgi izpildīta!")