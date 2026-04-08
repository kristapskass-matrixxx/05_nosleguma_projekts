# === LABOJUMS: datuma validācija pievienota ===
# === JAUNUMS: ienākumi/izdevumi ar aprakstiem ===
# === LABOJUMS: .get() lai strādā vecie JSON dati ===
# === JAUNUMS: kopējā bilance (bankas kopsavilkums) ===

from datetime import datetime
import json
import os
import csv

FAILS = "finanses.json"


def ieladet_datus():
    if os.path.exists(FAILS):
        with open(FAILS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def saglabat_datus(dati):
    with open(FAILS, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=4)


def ievadit_datumu():
    while True:
        datums = input("Datums (YYYY-MM-DD) [2026-04-08]: ")

        if datums == "":
            return "2026-04-08"

        try:
            datetime.strptime(datums, "%Y-%m-%d")
            return datums
        except ValueError:
            print("❌ Nederīgs datums!")


def ievadit_summa(teksts):
    while True:
        ievade = input(teksts)

        if ievade.strip() == "":
            apstiprinajums = input("⚠ Atstāt tukšu? (J/N): ").lower()
            if apstiprinajums == "j":
                return 0.0
            continue

        try:
            vertiba = float(ievade)
            if vertiba >= 0:
                return vertiba
            print("❌ Tikai >= 0")
        except ValueError:
            print("❌ Nepareizs formāts")


def ievadit_aprakstu(teksts):
    while True:
        apr = input(teksts)

        if apr.strip() == "":
            apstiprinajums = input("⚠ Atstāt tukšu? (J/N): ").lower()
            if apstiprinajums == "j":
                return ""
            continue

        return apr


def pievienot_izdevumu(dati):
    datums = ievadit_datumu()

    print("Kategorija:")
    print("1) Pārtika")
    print("2) Transports")
    print("3) Izglītība")
    print("4) Izprieca")

    kategorijas = {
        "1": "Pārtika",
        "2": "Transports",
        "3": "Izglītība",
        "4": "Izprieca"
    }

    while True:
        k = input("Izvēlies (1-4): ")
        if k in kategorijas:
            kategorija = kategorijas[k]
            break

    ienakumi = ievadit_summa("Ienākumi (EUR): ")
    izdevumi = ievadit_summa("Izdevumi (EUR): ")

    ien_apr = ievadit_aprakstu("Ienākumi - apraksts: ")
    izd_apr = ievadit_aprakstu("Izdevumi - apraksts: ")

    bilance = ienakumi - izdevumi

    ieraksts = {
        "datums": datums,
        "kategorija": kategorija,
        "ienakumi": ienakumi,
        "ienakumu_apraksts": ien_apr,
        "izdevumi": izdevumi,
        "izdevumu_apraksts": izd_apr,
        "bilance": bilance
    }

    dati.append(ieraksts)
    saglabat_datus(dati)

    print(f"✓ {datums} | {kategorija} | Bilance: {bilance} EUR")


def paradit_kopsavilkumu(dati):
    ienakumi_sum = sum(d.get("ienakumi", 0) for d in dati)
    izdevumi_sum = sum(d.get("izdevumi", 0) for d in dati)
    bilance = ienakumi_sum - izdevumi_sum

    print("\n===== KOPĒJAIS KOPSAVILKUMS (BANKA) =====")
    print(f"Ienākumi kopā: {ienakumi_sum} EUR")
    print(f"Izdevumi kopā: {izdevumi_sum} EUR")
    print(f"KOPĒJĀ BILANCE: {bilance} EUR")
    print("=========================================\n")


def eksportet_csv(dati):
    with open("finanses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Datums",
            "Kategorija",
            "Ienākumi",
            "Ienākumu apraksts",
            "Izdevumi",
            "Izdevumu apraksts",
            "Bilance"
        ])

        for d in dati:
            writer.writerow([
                d.get("datums", ""),
                d.get("kategorija", ""),
                d.get("ienakumi", 0),
                d.get("ienakumu_apraksts", ""),
                d.get("izdevumi", 0),
                d.get("izdevumu_apraksts", ""),
                d.get("bilance", 0)
            ])

    print("✓ CSV eksportēts")


def galvena_programma():
    dati = ieladet_datus()

    while True:
        print("\n1) Pievienot izdevumu")
        print("2) Eksportēt CSV")
        print("3) Parādīt kopsavilkumu")
        print("4) Beigt")

        izvele = input("Izvēlies: ")

        if izvele == "1":
            pievienot_izdevumu(dati)
        elif izvele == "2":
            eksportet_csv(dati)
        elif izvele == "3":
            paradit_kopsavilkumu(dati)
        elif izvele == "4":
            break
        else:
            print("❌ Nederīga izvēle")


if __name__ == "__main__":
    galvena_programma()