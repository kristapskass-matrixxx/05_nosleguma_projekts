# Noslēguma projekta DEVLOG

## Projekta nosaukums:
Python datu eksportēšanas un apstrādes rīks

## Izmantotās Git branches:
- main (galvenā branch)
- feature/exporting (eksportēšanas funkcionalitāte)

## Darba gaita:

### 1. Branch izveide
Izveidojām feature/exporting branch:
git checkout -b feature/exporting

### 2. Failu izveide un saturs

**main.py**
from exporter import export_data

def main():
    data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    export_data(data, "output.csv")

if __name__ == "__main__":
    main()

**exporter.py**
import csv

def export_data(data, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "score"])
        writer.writeheader()
        writer.writerows(data)

### 3. Fails output.csv
Pārbaudījām, ka fails `output.csv` satur:
id,name,score
1,Alice,95
2,Bob,88
3,Charlie,92

### 4. Git darbības

Pievienojām un commitējām failus:
git add main.py exporter.py docs\DEVLOG.md output.csv
git commit -m "Add exporting feature and DEVLOG"
git push -u origin feature/exporting

Merge uz main branch:
git checkout main
git merge feature/exporting
git push origin main

### 5. Secinājumi
- Projekts tagad sagatavots demo un testēšanai
- Visi faili glabājas GitHub repo
- Dokumentācija pilnībā pieejama `docs/DEVLOG.md`