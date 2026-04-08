import json
import os
import csv
from datetime import datetime

FAILS = "finanses.json"

IZDEVUMU_VEIDI = [
    "Ikdienas patēriņš",
    "Izklaide",
    "Neplānotie izdevumi",
    "Ikmēneša pakalpojumi",
    "Ārstniecība un Izglītība"
]


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


def ievadi_datu():
    while True:
        datums = input("Datums (YYYY-MM-DD vai YYYYMMDD) [šodiena]: ").strip()

        if datums == "":
            datums = datetime.today().strftime("%Y-%m-%d")

        try:
            if len(datums) == 8 and datums.isdigit():
                datums = f"{datums[:4]}-{datums[4:6]}-{datums[6:]}"

            datetime.strptime(datums, "%Y-%m-%d")

            gads, menesis, diena = datums.split("-")

            print(f"✓ Datums saglabāts kā: {datums}")

            return datums, int(gads), int(menesis), int(diena)

        except ValueError:
            print("❌ Nederīgs datums! Lieto YYYY-MM-DD vai YYYYMMDD")


def izveleties_vairakus_veidus():
    veidi = []

    while True:
        print("\nIzvēlies izdevumu veidu:")
        for i, v in enumerate(IZDEVUMU_VEIDI, 1):
            print(f"{i}) {v}")

        try:
            izvēle = int(input("Izvēlies (1-5): "))
            if 1 <= izvēle <= len(IZDEVUMU_VEIDI):
                veidi.append(IZDEVUMU_VEIDI[izvēle - 1])
        except ValueError:
            print("❌ Nepareiza izvēle!")
            continue

        vel = input("Vai pievienot vēl? (J/N): ").strip().upper()
        if vel == "N":
            break

    return veidi


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


def ievadi_komentaru(nosaukums, summa):
    if summa == 0:
        return ""

    while True:
        komentars = input(f"{nosaukums} komentārs: ").strip()

        if komentars == "":
            atb = input("Komentārs tukšs! Vai atstāt tukšu? (J/N): ").strip().upper()
            if atb == "J":
                return ""
            elif atb == "N":
                continue

        print(f"Ievadītais komentārs: {komentars}")

        labot = input("Vai labot komentāru? (J/N): ").strip().upper()

        if labot == "J":
            continue
        elif labot == "N":
            return komentars
        else:
            print("❌ Ievadi J vai N!")


def pievienot(dati):
    print("\n--- Jauns ieraksts ---")

    datums, gads, menesis, diena = ievadi_datu()

    ienakumi = ievadi_summu("Ienākumi")
    ienakumu_komentars = ievadi_komentaru("Ienākumu", ienakumi)

    izdevumi = ievadi_summu("Izdevumi")

    izdevumu_veidi = []
    izdevumu_komentars = ""

    if izdevumi > 0:
        izdevumu_veidi = izveleties_vairakus_veidus()
        izdevumu_komentars = ievadi_komentaru("Izdevumu", izdevumi)

    ieraksts = {
        "datums": datums,
        "gads": gads,
        "menesis": menesis,
        "diena": diena,
        "ienakumi": ienakumi,
        "izdevumi": izdevumi,
        "izdevumu_veidi": izdevumu_veidi,
        "ienakumu_komentars": ienakumu_komentars,
        "izdevumu_komentars": izdevumu_komentars,
        "bilance": round(ienakumi - izdevumi, 2)
    }

    print("\n--- PĀRSKATS ---")
    print(f"Datums: {datums}")
    print(f"Ienākumi: {ienakumi} EUR ({ienakumu_komentars})")
    print(f"Izdevumi: {izdevumi} EUR ({izdevumu_komentars})")
    print(f"Veidi: {', '.join(izdevumu_veidi) if izdevumu_veidi else '-'}")
    print(f"Bilance: {ieraksts['bilance']:.2f} EUR")

    apstiprinat = input("\nSaglabāt šo ierakstu? (J/N): ").strip().upper()

    if apstiprinat != "J":
        print("❌ Ieraksts netika saglabāts")
        return

    dati.append(ieraksts)
    saglabat(dati)

    print("✅ Ieraksts saglabāts!")


def skatit(dati):
    if not dati:
        print("Nav ierakstu.")
        return

    print("\n--- Visi ieraksti ---")
    print(f"{'Datums':<12}{'Izdevumi':>10} {'Veidi'}")
    print("-" * 50)

    for r in dati:
        veidi = ", ".join(r.get("izdevumu_veidi", []))
        print(f"{r['datums']:<12}{r['izdevumi']:>10.2f} {veidi}")


def dzest(dati):
    skatit(dati)

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


def filtrs_menesis(dati):
    menesis = input("Ievadi mēnesi (YYYY-MM): ").strip()

    try:
        datetime.strptime(menesis, "%Y-%m")
    except ValueError:
        print("❌ Nepareizs formāts!")
        return

    atrastie = [r for r in dati if r["datums"].startswith(menesis)]

    if not atrastie:
        print("Nav datu.")
        return

    total = 0

    print("\n--- Filtrēti ieraksti ---")
    for r in atrastie:
        print(f"{r['datums']} | -{r['izdevumi']} | {', '.join(r.get('izdevumu_veidi', []))}")
        total += r["izdevumi"]

    print("--------------------------")
    print(f"KOPĀ: {total:.2f} EUR")


def eksportet_csv(dati):
    faila_nosaukums = input("Faila nosaukums [finanses.csv]: ").strip()
    if faila_nosaukums == "":
        faila_nosaukums = "finanses.csv"

    with open(faila_nosaukums, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Datums", "Izdevumi", "Veidi"])

        for i in dati:
            writer.writerow([
                i["datums"],
                i["izdevumi"],
                ", ".join(i.get("izdevumu_veidi", []))
            ])

    print(f"✓ CSV eksportēts -> {faila_nosaukums}")


def statistika(dati):
    if not dati:
        print("Nav datu.")
        return

    total_ienakumi = sum(r["ienakumi"] for r in dati)
    total_izdevumi = sum(r["izdevumi"] for r in dati)
    bilance = total_ienakumi - total_izdevumi

    print("\n--- STATISTIKA ---")
    print(f"Kopējie ienākumi: {total_ienakumi:.2f} EUR")
    print(f"Kopējie izdevumi: {total_izdevumi:.2f} EUR")
    print(f"Kopējā bilance: {bilance:.2f} EUR")


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
        print("6) Statistika")
        print("7) Iziet")

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
            statistika(dati)
        elif izvele == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("❌ Nederīga izvēle!")


if __name__ == "__main__":
    galvena()