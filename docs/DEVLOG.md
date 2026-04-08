# Izstrādes žurnāls (DEVLOG) — Izdevumu izsekotājs

## 1. posms — Projekta uzsākšana
Sākotnēji tika definēta projekta ideja — izveidot izdevumu un ienākumu uzskaites sistēmu Python valodā.

Galvenais mērķis bija:
- saglabāt finanšu datus
- nodrošināt vienkāršu lietotāja saskarni
- eksportēt datus CSV formātā

---

## 2. posms — Pamata funkcionalitāte

Tika izstrādāta galvenā programma (app.py), kas ļauj:

- pievienot ienākumus un izdevumus
- ievadīt datumu, summu, kategoriju un aprakstu
- saglabāt datus JSON failā

Problēma:
- sākotnēji datu ievade nebija validēta

Risinājums:
- pievienota datuma un summas pārbaude
- aizliegti negatīvi skaitļi

---

## 3. posms — Datu struktūra un loģika

Tika izdalīta atsevišķa loģika:

- storage.py — JSON saglabāšana
- logic.py — aprēķini un validācija
- export.py — CSV eksports

Problēma:
- sākotnēji viss bija vienā failā

Risinājums:
- kods tika sadalīts moduļos, lai uzlabotu uzturēšanu

---

## 4. posms — Eksports un bilance

Tika pievienots CSV eksports un bilances aprēķins:

Bilance = ienākumi - izdevumi

Problēma:
- CSV failā bija encoding problēmas

Risinājums:
- pievienots utf-8-sig encoding

---

## 5. posms — Noslēgums

Projekts tika pilnveidots ar:

- JSON datu saglabāšanu
- CSV eksportu
- validācijas sistēmu
- modulāru struktūru

Rezultātā tika iegūta pilnībā funkcionāla CLI finanšu uzskaites sistēma.

---

## Pašnovērtējums

Projekts izdevās veiksmīgi un sasniedz izvirzītos mērķus. Tika apgūta datu apstrāde, failu struktūra un Python programmatūras arhitektūra.# filter update 
# export update 
