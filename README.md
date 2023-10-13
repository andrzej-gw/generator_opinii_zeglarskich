# Generator opinii żeglarskich

Prosty generator opinii żeglarskich w Latex'u, działający na bazie Python'a.

Krótki poradnik obsługi generatora opinii:

Błędy należy zgłaszać mailowo na adres: jedrekgwiazda@gmail.com

Plik przykładowy dość dobrze pokazuje całą funkcjonalność i przykładowe wykorzystanie biblioteki.

Wszystkie zmienne mają wartości domyślne, które tworzą puste pola do uzupełnienia długopisem.

Odwiedzone porty jeśli nie mieszczą się w jednej linii, powinny być w odpowiednich miejscach oddzielone znakiem '\n' (pokazane w pliku przykład).
Tak samo uwagi kapitana.

Wartość zagle_i_silnik jest domyślnie ustawiona na "-" i wtedy komórka ta nie pojawia się w tabeli godzin. Po zamianie na inną wartość
(również "0" lub "") pozycja żagle i silnik pojawi się.

Opinia kapitana: None - wszystkie pola puste, 0 - zaznacz zerowe pole, 1 - zaznacz pierwsze pole, itd.

Dostarczam również plik makefile. Aby utworzyć plik "opinia.tex" i "opinia.pdf", należy stworzyć plik "opinia.py" i wykonać "make opinia".
Można również zrobić to ręcznie poleceniem "python3 opinia.py > opinia.tex; pdflatex opinia.tex".

W przyszłości planowane jest dodanie języka angielskiego.

W katalogu wzorce znajdują się puste opinie według różnych wzorów.
