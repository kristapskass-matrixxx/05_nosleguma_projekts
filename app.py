import json
import os
from datetime import datetime

FAILS = "finanses.json"


# ---------------------------
# JSON ielāde / saglabāšana
# ---------------------------
def ieladet():
    if not os.path.exists(FAILS):
        return []
    with open(FAILS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def saglabat(dati):
    with open(FAILS, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)


# ---------------------------
# DATUMA VALIDĀCIJA
# ---------------------------
def ievadi_datu():
    while True:
        datums = input("Datums (YYYY-MM-DD) [šodiena]: ").strip()

        if datums == "":
            return datetime.today().strftime("%Y-%m-%d")

        try:
            datetime.strptime(datums, "%Y-%m-%d")
            return datums
        except ValueError:
            print("❌ Nederīgs datums!")


# ---------------------------
# SUMMAS IEVADĪŠANA
# ---------------------------
def ievadi_summu(nosaukums):
    while True:
        v = input(f"{nosaukums} (EUR): ").strip()

        if v == "":
            return 0.0

        try:
            v = float(v)
            if v < 0:
                print("❌ Nedrīkst būt negatīvs!")
                continue
            return v
        except ValueError:
            print("❌ Ievadi skaitli!")


# ---------------------------
# KOMENTĀRA LOĢIKA
# ---------------------------
def ievadi_komentaru(nosaukums, summa):
    if summa == 0:
        return ""

    while True:
        komentars = input(f"{nosaukums} komentārs: ").strip()

        if komentars != "":
            return komentars

        print("⚠ Komentārs tukšs!")
        atb = input("Vai atstāt tukšu? (J/N): ").strip().upper()

        if atb == "J":
            return ""
        elif atb == "N":
            continue
        else:
            print("❌ Ievadi J vai N!")


# ---------------------------
# PIEVIENOT IERAKSTU
# ---------------------------
def pievienot(dati):
    print("\n--- Jauns ieraksts ---")

    datums = ievadi_datu()
    ienakumi = ievadi_summu("Ienākumi")
    izdevumi = ievadi_summu("Izdevumi")

    ienakumu_kom = ievadi_komentaru("Ienākumu", ienakumi)
    izdevumu_kom = ievadi_komentaru("Izdevumu", izdevumi)

    bilance = ienakumi - izdevumi

    ieraksts = {
        "datums": datums,
        "ienakumi": ienakumi,
        "izdevumi": izdevumi,
        "ienakumu_komentars": ienakumu_kom,
        "izdevumu_komentars": izdevumu_kom,
        "bilance": bilance
    }

    dati.append(ieraksts)
    saglabat(dati)

    print(f"\n✓ Pievienots: {datums} | Bilance: {bilance:.2f} EUR")


# ---------------------------
# SKATĪT IERAKSTUS
# ---------------------------
def skatit(dati):
    if not dati:
        print("Nav ierakstu.")
        return

    print("\n--- Visi ieraksti ---")
    for i, r in enumerate(dati, 1):
        print(f"{i}. {r['datums']} | +{r['ienakumi']} -{r['izdevumi']} | Bilance: {r['bilance']}")


# ---------------------------
# DZĒST IERAKSTU
# ---------------------------
def dzest(dati):
    skatit(dati)
    if not dati:
        return

    try:
        nr = int(input("Kuru ierakstu dzēst (numurs): "))
        if 1 <= nr <= len(dati):
            izdzests = dati.pop(nr - 1)
            saglabat(dati)
            print(f"✓ Dzēsts: {izdzests['datums']}")
        else:
            print("❌ Nepareizs numurs")
    except ValueError:
        print("❌ Jāievada skaitlis")


# ---------------------------
# FILTRS PĒC MĒNEŠA
# ---------------------------
def filtrs_menesis(dati):
    menesis = input("Ievadi mēnesi (YYYY-MM): ").strip()

    atrastie = [r for r in dati if r["datums"].startswith(menesis)]

    if not atrastie:
        print("Nav datu šim mēnesim.")
        return

    print("\n--- Filtrēti ieraksti ---")
    for r in atrastie:
        print(f"{r['datums']} | +{r['ienakumi']} -{r['izdevumi']} | Bilance: {r['bilance']}")


# ---------------------------
# CSV EKSPORTS
# ---------------------------
def eksportet_csv(dati):
    import csv

    with open("finanses.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Datums",
            "Ienākumi",
            "Izdevumi",
            "Ienākumu komentārs",
            "Izdevumu komentārs",
            "Bilance"
        ])

        for i in dati:
            writer.writerow([
                i.get("datums", ""),
                i.get("ienakumi", 0),
                i.get("izdevumi", 0),
                i.get("ienakumu_komentars", ""),
                i.get("izdevumu_komentars", ""),
                i.get("bilance", 0)
            ])

    print("✓ CSV eksportēts")


# ---------------------------
# GALVENĀ PROGRAMMA
# ---------------------------
def galvena():
    dati = ieladet()

    while True:
        print("\n1) Pievienot ierakstu")
        print("2) Skatīt ierakstus")
        print("3) Dzēst ierakstu")
        print("4) Filtrēt pēc mēneša")
        print("5) Eksportēt CSV")
        print("6) Beigt")

        izvele = input("Izvēlies: ").strip()

        if izvele == "1":
            pievienot(dati)
        elif izvele == "2":
            skatit(dati)
        elif izvele == "3":
            dzest(dati)
        elif izvele == "4":
            filtrs_menesis(dati)
        elif izvele == "5":
            eksportet_csv(dati)
        elif izvele == "6":
            break
        else:
            print("❌ Nederīga izvēle!")


if __name__ == "__main__":
    galvena()