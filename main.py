# main.py
from exporter import export_data

def main():
    data = {
        "vards": "Kristaps",
        "uzvards": "Kass",
        "projekts": "05_nosleguma_projekts"
    }

    print("Datu apstrāde notiek...")
    export_data(data)
    print("Dati eksportēti veiksmīgi!")

if __name__ == "__main__":
    main()