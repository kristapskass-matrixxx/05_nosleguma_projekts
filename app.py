import json
import os
import csv
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
# DATUMA VALIDĀCIJA (UZLABOTA)
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
            print("❌ Nederīgs datums! Lieto YYYY-MM-DD")


# ---------------------------
# SUMMA
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
# KOMENTĀRS
# ---------------------------
def ievadi_komentaru(nosaukums, summa):
    if summa == 0:
        return ""

    while True:
        komentars = input(f"{nosaukums} komentārs: ").strip()

        if komentars:
            return komentars

        atb = input("Vai atstāt tukšu? (J/N): ").strip().upper()
        if atb == "J":
            return ""
        elif atb == "N":
            continue


# ---------------------------
# PIEVIENOT
# ---------------------------
def pievienot(dati):
    print("\n--- Jauns ieraksts ---")

    datums = ievadi_datu()
    ienakumi = ievadi_summu("Ienākumi")
    izdevumi = ievadi_summu("Izdevumi")

    ieraksts = {
        "datums": datums,
        "ienakumi": ienakumi,
        "izdevumi": izdevumi,
        "ienakumu_komentars": ievadi_komentaru("Ienākumu", ienakumi),
        "izdevumu_komentars": ievadi_komentaru("Izdevumu", izdevumi),
        "bilance": round(ienakumi - izdevumi, 2)
    }

    dati.append(ieraksts)
    saglabat(dati)

    print(f"\n✓ Pievienots: {datums} | Bilance: {ieraksts['bilance']:.2f} EUR")


# ---------------------------
# SKATĪT
# ---------------------------
def skatit(dati):
    if not dati:
        print("Nav ierakstu.")
        return

    print("\n--- Visi ieraksti ---")
    print(f"{'Datums':<12}{'Ienākumi':>10}{'Izdevumi':>10}{'Bilance':>10}")
    print("-" * 45)

    for r in dati:
        print(f"{r['datums']:<12}{r['ienakumi']:>10.2f}{r['izdevumi']:>10.2f}{r['bilance']:>10.2f}")


# ---------------------------
# DZĒST
# ---------------------------
def dzest(dati):
    skatit(dati)
    if not dati:
        return

    try:
        nr = int(input("Kuru dzēst (numurs): "))
        if 1 <= nr <= len(dati):
            izdzests = dati.pop(nr - 1)
            saglabat(dati)
            print(f"✓ Dzēsts: {izdzests['datums']}")
        else:
            print("❌ Nepareizs numurs")
    except ValueError:
        print("❌ Jāievada skaitlis")


# ---------------------------
# FILTRS (UZLABOTS ar datetime)
# ---------------------------
def filtrs_menesis(dati):
    menesis = input("Ievadi mēnesi (YYYY-MM): ").strip()

    try:
        datetime.strptime(menesis, "%Y-%m")
    except ValueError:
        print("❌ Nepareizs formāts!")
        return

    atrastie = [r for r in dati if r["datums"].startswith(menesis)]

    if not atrastie:
        print("Nav datu šim mēnesim.")
        return

    print("\n--- Filtrēti ieraksti ---")
    for r in atrastie:
        print(f"{r['datums']} | +{r['ienakumi']} -{r['izdevumi']} | {r['bilance']}")


# ---------------------------
# CSV EKSPORTS (UZLABOTS)
# ---------------------------
def eksportet_csv(dati):
    faila_nosaukums = input("Faila nosaukums [finanses.csv]: ").strip()

    if faila_nosaukums == "":
        faila_nosaukums = "finanses.csv"

    with open(faila_nosaukums, "w", encoding="utf-8-sig", newline="") as f:
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
                i["datums"],
                i["ienakumi"],
                i["izdevumi"],
                i["ienakumu_komentars"],
                i["izdevumu_komentars"],
                i["bilance"]
            ])

    print(f"✓ CSV eksportēts -> {faila_nosaukums}")


# ---------------------------
# GALVENĀ IZVĒLNE (UZLABOTA CLI)
# ---------------------------
def galvena():
    dati = ieladet()

    while True:
        print("\n════════════════════")
        print("  IZDEVUMU SISTĒMA")
        print("════════════════════")
        print("1) Pievienot ierakstu")
        print("2) Skatīt ierakstus")
        print("3) Dzēst ierakstu")
        print("4) Filtrēt pēc mēneša")
        print("5) Eksportēt CSV")
        print("6) Iziet")

        izvele = input("\nIzvēlies: ").strip()

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
            print("Uz redzēšanos!")
            break
        else:
            print("❌ Nederīga izvēle!")


if __name__ == "__main__":
    galvena()