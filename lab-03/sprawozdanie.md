Lab 3

Jan Domański



Moje commity

89f4a5e Dodano skrypt wczytujący plik CSV - pierwsza wersja skryptu, wczytuje dane.csv i wypisuje liczbę wierszy, razem z nim dodałem plik z danymi.

aea3df3 Dodano wypisanie nazw kolumn - skrypt dodatkowo wypisuje nazwy kolumn.

facf820 Dodano liczenie brakujących wartości - skrypt liczy braki w każdej kolumnie.

789f55b Merge pull request #1 - scalenie brancha lab-03-git do main przez Pull Request.

e246aad Zmieniono tytuł README na wersję A - zmiana pierwszej linii README na branchu konflikt-a.

3d4059e Zmieniono tytuł README na wersję B - zmiana tej samej linii na branchu konflikt-b.

7fe8a88 Rozwiązano konflikt w README - ręczne rozwiązanie konfliktu po scaleniu konflikt-b do konflikt-a.

e4b7874 Dodano .gitignore i zmieniono opis liczby wierszy - plik .gitignore dla plików tymczasowych i mała zmiana w skrypcie.

ddc01ef Błędna zmiana - celowo dodana błędna linia print(zle\_dane).

a761c1a Revert "Błędna zmiana" - cofnięcie poprzedniego commitu przez git revert.



Pull Request

Branch lab-03-git wypchnąłem na GitHub, utworzyłem Pull Request i scaliłem go do main (zrzut pr\_merged.png).\\



Zadanie 1

Na dwóch branchach zmieniłem tę samą pierwszą linię w README.md na różne wersje. Przy git merge konflikt-b Git zgłosił konflikt, bo nie wiedział, którą wersję wybrać. Rozwiązałem go ręcznie, usunąłem znaczniki <<<<<<<, ======= i >>>>>>> i zrobiłem commit.



Zadanie 2

Utworzyłem plik debug.log, który git status pokazywał jako untracked. Po dodaniu .gitignore z regułami \*.log, \_\_pycache\_\_/ i .ipynb\_checkpoints/ plik przestał się pokazywać. Potem zmieniłem jedną linię w skrypcie i sprawdziłem różnicę przez git diff.



Zadanie 3

Najpierw zmieniłem skrypt bez commitu i cofnąłem to przez git restore. Potem zrobiłem commit z błędną linią i cofnąłem go przez git revert HEAD. Błędna linia zniknęła z pliku, ale w historii zostały oba commity, bo revert nie kasuje historii, tylko dodaje nowy commit.

Zrzuty ekranu są w folderze lab-03/screenshots.

