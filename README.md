# PB1_PD18 - Kalkulators ar CI



Šis projekts parāda darbplūsmu ar Git, GitHub un automatizētu testēšanu (CI), izmantojot GitHub Actions.



## Kā palaist lokāli


1. Pārliecinies, ka tev ir instalēts Python 3.10 vai jaunāka versija.
2. Terminālī, projekta mapē, raksti:



```bash

python kalkulators.py

```



## Kā palaist testus



Izmantot šo komandu gan lokāli, gan CI vidē:



```bash

python -m unittest descover

```



## Continuous Integration (CI)



Fails ' .github/workflows/main.yml' automātiski palaižas pēc katra 'git push' un pārbauda, vai visi testi iziet. Ja testi iziet veiksīgi, GitHub Actions statuss ir zaļš; ja kāds tests neiziet, statuss ir sarkans.



## Definition of Done (DoD)



* Funkcija 'saskaitīt' strādā pareizi.
* Testi lokāli izpildās veiksmīgi.
* GitHub Actions rāda zaļu statusu.
* Dokumentācija ir atjaunināta.

