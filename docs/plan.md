\# Projekta plāns



\## A. Programmas apraksts

Izdevumu izsekotājs reģistrē lietotāja izdevumus, grupē pa kategorijām un mēnešiem, nodrošina kopsummas un CSV eksporta iespēju.



\## B. Datu struktūra

Viens izdevuma ieraksts:

{

&#x20; "date": "2025-02-25",

&#x20; "amount": 12.50,

&#x20; "category": "Ēdiens",

&#x20; "description": "Pusdienas kafejnīcā"

}



\## C. Moduļu plāns

\- app.py: CLI izvēlne, lietotāja mijiedarbība

\- storage.py: JSON failu load/save

\- logic.py: filtrēšana, kopsummas, datu analīze

\- export.py: CSV eksports



\## D. Lietotāja scenāriji

1\. Lietotājs pievieno izdevumu; programma validē datumu un summu.

2\. Lietotājs filtrē pēc mēneša; programma rāda tikai izvēlēto mēnesi.



\## E. Robežgadījumi

\- expenses.json neeksistē: load\_expenses() atgriež \[]

\- Nepareiza summa vai datums: tiek parādīts kļūdas paziņojums

\- Tukšs saraksts: "Nav izdevumu"

