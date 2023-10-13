from datetime import datetime
class Osoba:
     def __init__(self, imie_i_nazwisko="...........................", nr_telefonu="...........................", adres_email="..........................."):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nr_telefonu = nr_telefonu
        self.adres_email = adres_email

class Zeglarz(Osoba):
    def __init__(self, imie_i_nazwisko="...........................", stopien_zeglarski="...........................", nr_patentu="...........................", nr_telefonu="...........................", adres_email="...........................", funkcja="..........................."):
        super().__init__(imie_i_nazwisko, nr_telefonu, adres_email)
        self.stopien_zeglarski = stopien_zeglarski
        self.nr_patentu = nr_patentu

class Zalogant(Zeglarz):
    def __init__(self, imie_i_nazwisko="...........................", stopien_zeglarski="...........................", nr_patentu="...........................", nr_telefonu="...........................", adres_email="...........................", funkcja="..........................."):
        super().__init__(imie_i_nazwisko, stopien_zeglarski, nr_patentu, nr_telefonu, adres_email)
        self.funkcja = funkcja

class Kapitan(Zeglarz):
    def __init__(self, imie_i_nazwisko="...........................", stopien_zeglarski="...........................", nr_patentu="...........................", nr_telefonu="...........................", adres_email="..........................."):
        super().__init__(imie_i_nazwisko, stopien_zeglarski, nr_patentu, nr_telefonu, adres_email)
        
class Jacht:
    def __init__(self, nazwa="...........................", klasa="...........................", nr_rej="...........................", lc="...........................", port_macierzysty="...........................", moc_silnika="..........................."):
        self.nazwa = nazwa
        self.klasa = klasa
        self.nr_rej = nr_rej
        self.lc = lc
        self.port_macierzysty = port_macierzysty
        self.moc_silnika = moc_silnika
    
class Rejs:
    def __init__(self, nr_plywania="...........................", data_zaokretowania="", port_zaokretowania="", plywowy_zaokretowania="TAK/NIE", data_wyokretowania="", port_wyokretowania="", plywowy_wyokretowania="TAK/NIE", odwiedzone_porty="", liczba_portow_plywowych="", 
    pod_zaglami="", na_silniku="", zagle_i_silnik="-", razem_godz_zeglugi="", po_wodach_plywowych="", powyzej_6B="", w_portach_i_na_kotwicy="", przebyto_mil_morskich=""):
        self.nr_plywania=nr_plywania
        self.data_zaokretowania=data_zaokretowania
        self.port_zaokretowania=port_zaokretowania
        self.plywowy_zaokretowania=plywowy_zaokretowania
        self.data_wyokretowania=data_wyokretowania
        self.port_wyokretowania=port_wyokretowania
        self.plywowy_wyokretowania=plywowy_wyokretowania
        self.odwiedzone_porty=odwiedzone_porty
        self.liczba_portow_plywowych=liczba_portow_plywowych
        self.pod_zaglami=pod_zaglami
        self.na_silniku=na_silniku
        self.zagle_i_silnik=zagle_i_silnik
        self.razem_godz_zeglugi=razem_godz_zeglugi
        self.po_wodach_plywowych=po_wodach_plywowych
        self.powyzej_6B=powyzej_6B
        self.w_portach_i_na_kotwicy=w_portach_i_na_kotwicy
        self.przebyto_mil_morskich=przebyto_mil_morskich
        
class Opinia_kapitana:
    def __init__(self, pozytywna=None, wywiazywanie_z_obowiazkow=None, choroba_morska=None, odpornosc_w_trudnych_warunkach=None, uwagi=""):
        self.pozytywna=pozytywna
        self.wywiazywanie_z_obowiazkow=wywiazywanie_z_obowiazkow
        self.choroba_morska=choroba_morska
        self.odpornosc_w_trudnych_warunkach=odpornosc_w_trudnych_warunkach
        self.uwagi=uwagi

def wypisz_naglowek():
    print("""\\documentclass{article}
\\usepackage{polski}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=1cm, a4paper, bottom=2cm]{geometry}
\\usepackage{graphicx}
\\usepackage{amssymb} %for \\varnothing (empty set)
\\usepackage{multirow}
\\usepackage{tabularx}
\\usepackage{wasysym}

\\setlength{\\parindent}{0pt}
\\author{Andrzej Gwiazda}
\\pagenumbering{gobble}

\\begin{document}
""")

def wypisz_opinie(zalogant=Zalogant(), jacht=Jacht(), rejs=Rejs(), opinia_kapitana=Opinia_kapitana(), kapitan=Kapitan(), logo=False, jezyk="pl"):
    def box(zaznaczone):
        if zaznaczone:
            return "\\XBox"
        else:
            return "\\Box"
    if logo:
        print("""\\newpage
\\begin{minipage}{0.11\\textwidth}
\\includegraphics[width=\\textwidth]{logo.png}
\\end{minipage}
\\begin{minipage}{0.89\\textwidth}
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \\hline
 \\textbf{KLUB ŻEGLARSKI UNIWERSYTETU WARSZAWSKIEGO} \\\\
 \\hline
 \\\\
 \\textbf{\\huge OPINIA Z REJSU} \\\\
 \\\\
\\hline
\\end{tabularx}
\\end{minipage}
""")

    else:
        print("""\\newpage
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \hline
 \\\\
 \\textbf{\\huge OPINIA Z REJSU} \\\\
 \\\\
\\hline
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O UCZESTNIKU REJSU}
\\begin{tabularx}{\\textwidth}{X X X}
imię i nazwisko: \\textit{"""+str(zalogant.imie_i_nazwisko)+"""} & stop. żegl./mot.: \\textit{"""+str(zalogant.stopien_zeglarski)+"""} & nr patentu: \\textit{"""+str(zalogant.nr_patentu)+"""} \\\\
nr telefonu: \\textit{"""+str(zalogant.nr_telefonu)+"""} & e-mail: \\textit{"""+str(zalogant.adres_email)+"""} & funkcja: \\textit{"""+str(zalogant.funkcja)+"""} \\\\
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O JACHCIE}

\\begin{tabularx}{\\textwidth}{X X X}
nazwa jachtu: \\textit{"""+str(jacht.nazwa)+"""} & klasa: \\textit{"""+str(jacht.klasa)+"""} & nr rej.: \\textit{"""+str(jacht.nr_rej)+"""} \\\\
lc[m]: \\textit{"""+str(jacht.lc)+"""} & port macierzysty: \\textit{"""+str(jacht.port_macierzysty)+"""} & moc silnika [kW]: \\textit{"""+str(jacht.moc_silnika)+"""} \\\\
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O REJSIE}

Wpisu dokonano na podstawie dziennika jachtowego, nr pływania: \\textit{"""+str(rejs.nr_plywania)+"""}
\\\\

\\begin{tabularx}{\\textwidth}{|X|X|X|}
\\hline
Port zaokrętowania: \\textit{"""+str(rejs.port_zaokretowania)+"""} & Data: \\textit{"""+str(rejs.data_zaokretowania)+"""} & Pływowy: \\textit{"""+str(rejs.plywowy_zaokretowania)+"""} \\\\
\\hline
Port wyokrętowania: \\textit{"""+str(rejs.port_wyokretowania)+"""} & Data: \\textit{"""+str(rejs.data_wyokretowania)+"""} & Pływowy: \\textit{"""+str(rejs.plywowy_wyokretowania)+"""} \\\\
\\hline
\\multicolumn{3}{|l|}{Odwiedzone miejsca:""")

    if rejs.odwiedzone_porty=="":
        print("""\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
""")
    else:
        tmp=rejs.odwiedzone_porty.split("\n")
        for i in range(4):
            if i==0:
                print("\\textit{"+tmp[i]+"}\\dotfill}\\\\")
            elif i<len(tmp):
                print("\\multicolumn{3}{|l|}{\\textit{"+str(tmp[i])+"}\\dotfill} \\\\")
            else:
                print("\\multicolumn{3}{|l|}{\\dotfill} \\\\")
    print("""\\hline
\\multicolumn{2}{|l|}{W tym liczba portów pływowych: \\textit{"""+str(rejs.liczba_portow_plywowych)+"""}} & Liczba dni rejsu: \\textit{"""+
("" if rejs.data_zaokretowania=="" or rejs.data_wyokretowania=="" else str((datetime.strptime(rejs.data_wyokretowania, '%d.%m.%Y')
-datetime.strptime(rejs.data_zaokretowania, '%d.%m.%Y')).days+1))+"""}\\\\
\\hline
\\end{tabularx}
\\\\\\\\

\\begin{tabularx}{\\textwidth}{
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X"""+("""
|>{\\centering\\arraybackslash}X""" if rejs.zagle_i_silnik!="-" else "")+"""
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|}
\\hline
\\multicolumn{"""+("6" if rejs.zagle_i_silnik!="-" else "5")+"""}{|c|}{GODZINY ŻEGLUGI} & GODZINY POSTOJU & \\multirow{2}{2cm}{PRZEBYTO MIL MORSKICH} \\\\
\\cline{1-"""+("7" if rejs.zagle_i_silnik!="-" else "6")+"""}
pod żaglami & na silniku & """+("żagle i silnik &" if rejs.zagle_i_silnik!="-" else "")+"""\\textbf{razem godz. żegl.} & po wodach pływowych & powyżej $6^\\circ$B & w portach i na kotwicy & \\\\ 
\\hline
& &"""+(" &" if rejs.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\huge """+str(rejs.pod_zaglami)+"&\huge "+str(rejs.na_silniku)+" &\huge "+(str(rejs.zagle_i_silnik)+" &\huge " if rejs.zagle_i_silnik!="-" else "")+str(rejs.razem_godz_zeglugi)+
" &\huge "+str(rejs.po_wodach_plywowych)+" &\huge "+str(rejs.powyzej_6B)+" &\huge """+str(rejs.w_portach_i_na_kotwicy)+" &\huge """+str(rejs.przebyto_mil_morskich)+""" \\\\
& &"""+(" &" if rejs.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\\hline
\\end{tabularx}
""")

    print("""\\section*{OPINIA KAPITANA ~~~~~~~~ $"""+box(opinia_kapitana.pozytywna==0)+"$ pozytywna ~~~~~~~~ $"+box(opinia_kapitana.pozytywna==1)+"""$ negatywna}

\\begin{tabularx}{\\textwidth}{X X X X}
\\multicolumn{4}{l}{\\textbf{Z obowiązków wywiązywał/a się:}}\\\\
$"""+box(opinia_kapitana.wywiazywanie_z_obowiazkow==0)+"$ bardzo dobrze & $"+box(opinia_kapitana.wywiazywanie_z_obowiazkow==1)+"$ dobrze & $"+box(opinia_kapitana.wywiazywanie_z_obowiazkow==2)+"$ dostatecznie & $"+box(opinia_kapitana.wywiazywanie_z_obowiazkow==3)+"""$ niedostatecznie\\\\
\\\\
\\multicolumn{4}{l}{\\textbf{Chorobie morskiej:}}\\\\
$"""+box(opinia_kapitana.choroba_morska==0)+"$ nie podlegał/a & $"+box(opinia_kapitana.choroba_morska==1)+"$ chorowała/a ciężko & \\multicolumn{2}{l}{$"+box(opinia_kapitana.choroba_morska==2)+"""$ chorował/a sporadycznie i mógł/mogła pracować}\\\\
\\\\
\\multicolumn{4}{l}{\\textbf{Odporność w trudnych warunkach:}}\\\\
$"""+box(opinia_kapitana.odpornosc_w_trudnych_warunkach==0)+"$ dobra & $"+box(opinia_kapitana.odpornosc_w_trudnych_warunkach==1)+"$ dostateczna & $\\Box$ niedostateczna & $"+box(opinia_kapitana.odpornosc_w_trudnych_warunkach==2)+"""$ nie sprawdzono\\\\
\\end{tabularx}
""")

    print("""\section*{UWAGI KAPITANA}

""")
    tmp=opinia_kapitana.uwagi.split("\n")
    for i in range(3):
        if i<len(tmp):
            print("\\textit{"+str(tmp[i])+"}\\dotfill \\\\")
        else:
            print(".\\dotfill \\\\")    


    print("""\\section*{INFORMACJE O KAPITANIE}

\\begin{tabularx}{\\textwidth}{X X}
imię i nazwisko: \\textit{"""+str(kapitan.imie_i_nazwisko)+"} & stop. żegl./mot. i nr patentu: \\textit{"+
(kapitan.stopien_zeglarski+" nr "+kapitan.nr_patentu if kapitan.stopien_zeglarski+kapitan.nr_patentu!="......................................................" else "...........................")+"""}\\\\
nr telefonu: \\textit{"""+str(kapitan.nr_telefonu)+"} & e-mail: \\textit{"+str(kapitan.adres_email)+"""}\\\\
\\\\\\\\
...................................... & ......................................\\\\
miejscowość, data & podpis kapitana\\\\
\\end{tabularx}""")


def wypisz_karte_rejsu(jacht=Jacht(), rejs=Rejs(), uwagi_kapitana="", kapitan=Kapitan(), zaloga=[], armator=Osoba(), logo=False, jezyk="pl"):
    if logo:
        print("""\\newpage
\\begin{minipage}{0.11\\textwidth}
\\includegraphics[width=\\textwidth]{logo.png}
\\end{minipage}
\\begin{minipage}{0.89\\textwidth}
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \\hline
 \\textbf{KLUB ŻEGLARSKI UNIWERSYTETU WARSZAWSKIEGO} \\\\
 \\hline
 \\\\
 \\textbf{\\huge KARTA REJSU} \\\\
 \\\\
\\hline
\\end{tabularx}
\\end{minipage}
""")

    else:
        print("""\\newpage
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \hline
 \\\\
 \\textbf{\\huge KARTA REJSU} \\\\
 \\\\
\\hline
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O KAPITANIE}
\\begin{tabularx}{\\textwidth}{X X X}
imię i nazwisko: \\textit{"""+str(kapitan.imie_i_nazwisko)+"""} & stop. żegl./mot.: \\textit{"""+str(kapitan.stopien_zeglarski)+"""} & nr patentu: \\textit{"""+str(kapitan.nr_patentu)+"""} \\\\
nr telefonu: \\textit{"""+str(kapitan.nr_telefonu)+"""} & e-mail: \\textit{"""+str(kapitan.adres_email)+"""} \\\\
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O JACHCIE}

\\begin{tabularx}{\\textwidth}{X X X}
nazwa jachtu: \\textit{"""+str(jacht.nazwa)+"""} & klasa: \\textit{"""+str(jacht.klasa)+"""} & nr rej.: \\textit{"""+str(jacht.nr_rej)+"""} \\\\
lc[m]: \\textit{"""+str(jacht.lc)+"""} & port macierzysty: \\textit{"""+str(jacht.port_macierzysty)+"""} & moc silnika [kW]: \\textit{"""+str(jacht.moc_silnika)+"""} \\\\
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O REJSIE}

Wpisu dokonano na podstawie dziennika jachtowego, nr pływania: \\textit{"""+str(rejs.nr_plywania)+"""}
\\\\

\\begin{tabularx}{\\textwidth}{|X|X|X|}
\\hline
Port zaokrętowania: \\textit{"""+str(rejs.port_zaokretowania)+"""} & Data: \\textit{"""+str(rejs.data_zaokretowania)+"""} & Pływowy: \\textit{"""+str(rejs.plywowy_zaokretowania)+"""} \\\\
\\hline
Port wyokrętowania: \\textit{"""+str(rejs.port_wyokretowania)+"""} & Data: \\textit{"""+str(rejs.data_wyokretowania)+"""} & Pływowy: \\textit{"""+str(rejs.plywowy_wyokretowania)+"""} \\\\
\\hline
\\multicolumn{3}{|l|}{Odwiedzone miejsca:""")

    if rejs.odwiedzone_porty=="":
        print("""\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
""")
    else:
        tmp=rejs.odwiedzone_porty.split("\n")
        for i in range(4):
            if i==0:
                print("\\textit{"+tmp[i]+"}\\dotfill}\\\\")
            elif i<len(tmp):
                print("\\multicolumn{3}{|l|}{\\textit{"+str(tmp[i])+"}\\dotfill} \\\\")
            else:
                print("\\multicolumn{3}{|l|}{\\dotfill} \\\\")
    print("""\\hline
\\multicolumn{2}{|l|}{W tym liczba portów pływowych: \\textit{"""+str(rejs.liczba_portow_plywowych)+"""}} & Liczba dni rejsu: \\textit{"""+
("" if rejs.data_zaokretowania=="" or rejs.data_wyokretowania=="" else str((datetime.strptime(rejs.data_wyokretowania, '%d.%m.%Y')
-datetime.strptime(rejs.data_zaokretowania, '%d.%m.%Y')).days+1))+"""}\\\\
\\hline
\\end{tabularx}
\\\\\\\\

\\begin{tabularx}{\\textwidth}{
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X"""+("""
|>{\\centering\\arraybackslash}X""" if rejs.zagle_i_silnik!="-" else "")+"""
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|}
\\hline
\\multicolumn{"""+("6" if rejs.zagle_i_silnik!="-" else "5")+"""}{|c|}{GODZINY ŻEGLUGI} & GODZINY POSTOJU & \\multirow{2}{2cm}{PRZEBYTO MIL MORSKICH} \\\\
\\cline{1-"""+("7" if rejs.zagle_i_silnik!="-" else "6")+"""}
pod żaglami & na silniku & """+("żagle i silnik &" if rejs.zagle_i_silnik!="-" else "")+"""\\textbf{razem godz. żegl.} & po wodach pływowych & powyżej $6^\\circ$B & w portach i na kotwicy & \\\\ 
\\hline
& &"""+(" &" if rejs.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\huge """+str(rejs.pod_zaglami)+"&\huge "+str(rejs.na_silniku)+" &\huge "+(str(rejs.zagle_i_silnik)+" &\huge " if rejs.zagle_i_silnik!="-" else "")+str(rejs.razem_godz_zeglugi)+
" &\huge "+str(rejs.po_wodach_plywowych)+" &\huge "+str(rejs.powyzej_6B)+" &\huge """+str(rejs.w_portach_i_na_kotwicy)+" &\huge """+str(rejs.przebyto_mil_morskich)+""" \\\\
& &"""+(" &" if rejs.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\\hline
\\end{tabularx}
""")

    print("""\\section*{INFORMACJE O ZAŁODZE}
    \\begin{tabular}{|m{0.013\\textwidth}|m{0.1727\\textwidth}|m{0.14\\textwidth}|m{0.08\\textwidth}||m{0.013\\textwidth}|m{0.1727\\textwidth}|m{0.14\\textwidth}|m{0.08\\textwidth}|}
    \\hline
    lp. & imię i nazwisko & stopień żegl./mot. & funkcja na jachcie & lp. & imię i nazwisko & stopień żegl./mot. & funkcja na jachcie\\\\
    \\hline
    """)
    for i in range(6):
        if len(zaloga)>i:
            print(i+1, "&", zaloga[i].imie_i_nazwisko, "&", zaloga[i].stopien_zeglarski, "&", zaloga[i].funkcja, "&", end="")
        else:
            print("&&&&", end="")
        if len(zaloga)>i+6:
            print(i+7, "&", zaloga[i+6].imie_i_nazwisko, "&", zaloga[i+6].stopien_zeglarski, "&", zaloga[i+6].funkcja, end="")
        else:
            print("&&&", end="")
        print("""\\\\
\\hline""")
    print("""
    \\end{tabular}
    
    """)

    print("""\section*{UWAGI KAPITANA}

""")
    tmp=uwagi_kapitana.split("\n")
    for i in range(3):
        if i<len(tmp):
            print("\\textit{"+str(tmp[i])+"}\\dotfill \\\\")
        else:
            print(".\\dotfill \\\\")    


    print("""\\section*{INFORMACJE O ARMATORZE}

\\begin{tabularx}{\\textwidth}{X X}
imię i nazwisko/nazwa: \\textit{"""+str(armator.imie_i_nazwisko)+"""} \\\\
nr telefonu: \\textit{"""+str(armator.nr_telefonu)+"} & e-mail: \\textit{"+str(armator.adres_email)+"""}\\\\
\\\\\\\\
...................................... & ......................................\\\\
miejscowość, data & podpis armatora jachtu\\\\
\\end{tabularx}""")
    
def wypisz_stopke():
    print("\end{document}")
