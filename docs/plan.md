# Projekta plāns — Izdevumu izsekotājs

## Mērķis
Izveidot Python komandrindas lietotni, kas ļauj lietotājam sekot ienākumiem un izdevumiem, saglabāt datus JSON failā un eksportēt CSV formātā.

---

## Funkcijas

- Pievienot ienākumus
- Pievienot izdevumus
- Apskatīt visus ierakstus
- Dzēst ierakstus
- Filtrēt pēc mēneša
- Aprēķināt bilanci (ienākumi - izdevumi)
- Eksportēt datus CSV failā
- Saglabāt datus JSON failā

---

## Datu ievade

- Datums (YYYY-MM-DD)
- Ienākumi (pozitīvs skaitlis vai 0)
- Izdevumi (pozitīvs skaitlis vai 0)
- Kategorija
- Apraksts (var būt tukšs ar apstiprinājumu J/N)

---

## Robežgadījumi

- Nederīgs datums → ievade tiek noraidīta
- Negatīva summa → nav atļauta
- Tukšs apraksts → lietotājam jautā “Vai atstāt tukšu? (J/N)”
- Nepareiza izvēle izvēlnē → tiek prasīts ievadīt vēlreiz

---

## Tehnoloģijas

- Python 3
- JSON failu glabāšana
- CSV eksports
- datetime modulis
- CLI (komandrindas interfeiss)

---

## Projekta struktūra

- app.py — galvenā programma (izvēlne)
- logic.py — biznesa loģika
- storage.py — JSON lasīšana / rakstīšana
- export.py — CSV eksports

---

## Rezultāts

Pilnībā funkcionāls izdevumu izsekotājs, kas ļauj analizēt finanšu plūsmu un saglabāt datus starp sesijām.
