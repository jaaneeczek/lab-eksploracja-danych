Lab 4

Jan Domański

Wybrany zbiór:

Nazwa: Medical records

Źródło: https://www.kaggle.com/datasets/madhurishinde26788/medical-records

Licencja: MIT

Opis zbioru:
Zbiór ma dwa pliki, data.csv i patient_data.csv (razem 28 kolumn). 
W data.csv jest 14 kolumn: id, claim_amount, owner, type, date, gender, weight, height, blood_grp, BP, BMI, AGE, Diabetes i food_allergies.
Autor nie dodał żadnego opisu zbioru, więc nie wiadomo, skąd pochodzą dane i czy są prawdziwe. 
Wyglądają raczej na testowe, bo ten sam pacjent (PAT0088) ma w różnych wierszach raz płeć female, a raz male, a wzrost w części wierszy to 5 albo 6, a w innych normalne wartości do 169.

Dane osobowe i wrażliwe:
W data.csv nie ma imion, nazwisk ani adresów, pacjenci mają tylko kody typu PAT0088.
To jest pseudonimizacja, a nie anonimizacja, bo ktoś, kto ma klucz, może te kody przypisać do konkretnych osób. 
Zbiór zawiera dane o zdrowiu (waga, wzrost, grupa krwi, ciśnienie, BMI, cukrzyca, alergie pokarmowe), czyli dane wrażliwe w rozumieniu RODO, a do tego kwoty roszczeń. 
Wiek, płeć i data (kolumna date) razem mogą dodatkowo pomóc wskazać konkretną osobę.
Przed użyciem: zostawić tylko kolumny potrzebne do modelu (minimalizacja), nie łączyć zbioru z innymi danymi, które mogłyby pomóc wskazać osobę, ograniczyć dostęp do pliku i nie trzymać go dłużej niż trzeba. 
Przed użyciem w projekcie komercyjnym trzeba by ustalić prawdziwe źródło danych, bo bez tego nie da się sprawdzić, czy autor w ogóle miał prawo je udostępnić.


Ochrona danych:

| Pytanie | Odpowiedź |
|---|---|
| Czy dane są zanonimizowane lub spseudonimizowane? | Spseudonimizowane, zamiast imion są kody pacjentów (np. PAT0088). Autor nic nie pisze o anonimizacji. |
| Jaka jest licencja zbioru? | MIT |
| Czy licencja pozwala na użycie komercyjne? | Tak, trzeba tylko zachować informację o autorze i licencji. MIT to jednak licencja do oprogramowania, a nie do danych, i nie wiadomo, czy wybrał ją pierwotny autor danych. |
| Czy zbiór zawiera dane wrażliwe? | Tak, dane o zdrowiu: waga, wzrost, grupa krwi, ciśnienie, BMI, cukrzyca, alergie pokarmowe. |
| Czy znam źródło danych? | Nie, zbiór nie ma opisu. |
| Ocena bezpieczeństwa (1-5) | 2 |

Wnioski: 
Licencja formalnie pozwala na użycie komercyjne, ale nieznane źródło, dane o zdrowiu i tylko pseudonimizacja to za duże ryzyko, żeby użyć tego zbioru w projekcie komercyjnym bez dodatkowego sprawdzenia.


Zadanie 1 

| Zbiór | Licencja | Użycie komercyjne | Wymagania |
|---|---|---|---|
| Medical records | MIT | Tak | Zachować informację o autorze i licencji |
| Healthcare Dataset, https://www.kaggle.com/datasets/prasad22/healthcare-dataset | CC0: Public Domain | Tak | Brak, autor zrzekł się praw |

Wnioski:
Oba zbiory dotyczą pacjentów. Bezpieczniej byłoby użyć Healthcare Dataset, bo ma licencję CC0, czyli bez żadnych warunków, a do tego autor pisze, że dane są w całości wygenerowane biblioteką Faker i nie zawierają informacji o prawdziwych pacjentach. 
Przy Medical records licencja MIT też pozwala na użycie komercyjne, ale nie wiadomo, skąd są dane, więc nie ma pewności, czy autor mógł je w ogóle udostępnić. 
Żadna z tych licencji nie wymaga udostępniania opracowań na tej samej licencji.


Zadanie 2
Osoby są wymyślone.
Dane oryginalne:

| Imię i nazwisko | Data urodzenia | Kod pocztowy | Płeć | Diagnoza |
|---|---|---|---|---|
| Adam Nowicki | 1992-05-14 | 20-400 | M | astma |
| Ewa Wróbel | 1978-11-02 | 21-100 | K | cukrzyca typu 2 |
| Michał Zając | 2001-08-23 | 20-093 | M | nadciśnienie |

Kolumna, która bezpośrednio identyfikuje osobę: imię i nazwisko.

Kolumny, które razem mogą pozwolić zidentyfikować osobę: data urodzenia, kod pocztowy i płeć.

Wersja spseudonimizowana:

| Kod | Data urodzenia | Kod pocztowy | Płeć | Diagnoza |
|---|---|---|---|---|
| P-001 | 1992-05-14 | 20-400 | M | astma |
| P-002 | 1978-11-02 | 21-100 | K | cukrzyca typu 2 |
| P-003 | 2001-08-23 | 20-093 | M | nadciśnienie |

Klucz:

| Kod | Imię i nazwisko |
|---|---|
| P-001 | Adam Nowicki |
| P-002 | Ewa Wróbel |
| P-003 | Michał Zając |

Wersja zanonimizowana:

| Rocznik | Region | Płeć | Diagnoza |
|---|---|---|---|
| lata 90. | woj. lubelskie | M | astma |
| lata 70. | woj. lubelskie | K | cukrzyca typu 2 |
| lata 2000. | woj. lubelskie | M | nadciśnienie |

Po pseudonimizacji ryzyko dalej jest duże, bo dokładna data urodzenia, kod pocztowy i płeć razem często wskazują jedną osobę. 
Po anonimizacji ryzyko jest dużo mniejsze, ale nie znika całkiem. 
Przy małej grupie albo rzadkiej diagnozie połączenie rocznika, regionu i płci nadal może wskazać konkretną osobę.


Zadanie 3

| Biblioteka | Licencja | Typ | Czy można użyć komercyjnie |
|---|---|---|---|
| scikit-learn | BSD 3-Clause | permisywna | Tak |
| pandas | BSD 3-Clause | permisywna | Tak |
| TensorFlow | Apache 2.0 | permisywna | Tak |

Licencje sprawdziłem w plikach LICENSE (w scikit-learn plik nazywa się COPYING) w repozytoriach na GitHubie. Żadna z tych licencji nie wymaga udostępniania kodu mojej aplikacji, trzeba tylko zachować informację o prawach autorskich i treść licencji.
Gdyby biblioteka była na GPL, a ja rozpowszechniałbym aplikację, to musiałbym udostępnić całą aplikację też na licencji GPL, razem z kodem źródłowym.
W projekcie komercyjnym, w którym kod ma zostać zamknięty, oznaczałoby to, że takiej biblioteki nie da się użyć.
