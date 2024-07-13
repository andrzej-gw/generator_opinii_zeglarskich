"""Moduły do tworzenia ładniejszych klas z danymi i do liczenia dni pomiędzy datami"""
import dataclasses
from datetime import datetime

def slownik(fraza, jezyk):
    if jezyk=="pl":
        return fraza
    if jezyk=="eng":
        return {
            "OPINIA Z REJSU" : "CREW MEMBER'S CERT. OF PASSAGE",
            "INFORMACJE O UCZESTNIKU REJSU" : "INFORMATION ABOUT THE CRUISE PARTICIPANT",
            "imię i nazwisko" : "name \& surname",
            "stop. żegl./mot." : "sailing/mot. cert.",
            "nr patentu" : "cert. no.",
            "funkcja" : "rank",
            "INFORMACJE O JACHCIE" : "INFORMATION ABOUT YACHT",
            "nazwa" : "name",
            "typ" : "type",
            "nr rej." : "reg. no.",
            "port macierzysty" : "home port",
            "moc silnika" : "engine power",
            "INFORMACJE O REJSIE" : "CRUISE INFORMATION",
            "Wpisu dokonano na podstawie dziennika jachtowego, nr pływania" : "Based on Vessel Log Book, voyage no.",
            "Port zaokrętowania" : "Port of embarkation",
            "Data" : "Date",
            "Pływowy" : "Tidal",
            "Port wyokrętowania" : "Port of disembarkation",
            "Odwiedzone miejsca" : "Visited places",
            "W tym liczba portów pływowych" : "Number of tidal ports",
            "Liczba dni rejsu" : "Number of cruise days",
            "GODZINY ŻEGLUGI" : "UNDER WAY",
            "GODZINY POSTOJU" : "MOORING HOURS",
            "PRZEBYTO MIL MORSKICH" : "NUMBER OF NAUTICAL MILES",
            "pod żaglami" : "under sails",
            "na silniku" : "using engine",
            "żagle i silnik" : "sails and engine",
            "razem godz. żegl." : "total under way",
            "po wodach pływowych" : "in tidal waters",
            "powyżej" : "over",
            "w portach i na kotwicy" : "in harbours, on anchor",
            "OPINIA KAPITANA" : "CAPTAIN'S OPINION",
            "pozytywna" : "positive",
            "negatywna" : "negative",
            "Z obowiązków wywiązywał/a się" : "He/she fulfilled his/her duties",
            "bardzo dobrze" : "very well", 
            "dobrze" : "well",
            "dostatecznie" : "sufficiently",
            "niedostatecznie" : "insufficiently",
            "Chorobie morskiej" : "Sea sickness",
            "nie podlegał/a" : "no",
            "chorował/a ciężko" : "yes",
            "chorował/a sporadycznie i mógł/mogła pracować" : "occasionally and could work",
            "Odporność w trudnych warunkach" : "Resistance in harsh conditions at sea",
            "dobra" : "good",
            "dostateczna" : "sufficient",
            "niedostateczna" : "insufficient",
            "nie sprawdzono" : "not verified",
            "UWAGI KAPITANA" : "CAPTAIN'S COMMENTS",
            "INFORMACJE O KAPITANIE" : "INFORMATION ABOUT CAPTAIN",
            "nr telefonu" : "phone no.",
            "miejscowość, data" : "place, date",
            "podpis kapitana" : "captain's signature",
            "KARTA REJSU" : "CAPTAIN’S  CERTIFICATE  OF  PASSAGE",
            "INFORMACJE O ZAŁODZE" : "INFORMATION ABOUT CREW",
            "lp." : "no.",
            "INFORMACJE O ARMATORZE" : "INFORMATION ABOUT OWNER",
            "podpis armatora jachtu" : "owner's signature",
            "TAK" : "YES",
            "NIE" : "NO",
            "TAK/NIE" : "YES/NO"
        }[fraza]
    assert False, "Nieznany język: "+jezyk

@dataclasses.dataclass
class Osoba:
    """Klasa reprezentująca osobę"""
    imie_i_nazwisko: str = "."*27
    nr_telefonu: str = "."*27
    adres_email: str = "."*27

@dataclasses.dataclass
class Zeglarz(Osoba):
    """Klasa reprezentująca żeglarza. Dziedziczy po osobie, ma dodatkowe parametry: stopień
    żeglarski i nr patentu"""
    stopien_zeglarski: str = "."*27
    nr_patentu: str = "."*27

@dataclasses.dataclass
class Zalogant(Zeglarz):
    """Klasa reprezentująca załoganta. Dziedziczy po żeglarzu, ma dodatkowy parametr: funkcja"""
    funkcja: str = "."*27
    def wypisz(self, jezyk):
        print("""\\section*{"""+slownik("INFORMACJE O UCZESTNIKU REJSU", jezyk)+"""}
\\begin{tabularx}{\\textwidth}{X X X}
"""+slownik("imię i nazwisko", jezyk)+": \\textit{"+str(self.imie_i_nazwisko)+"} & "+slownik("stop. żegl./mot.", jezyk)+": \\textit{"+
str(self.stopien_zeglarski)+"} & "+slownik("nr patentu", jezyk)+": \\textit{"+str(self.nr_patentu)+"""} \\\\
nr telefonu: \\textit{"""+str(self.nr_telefonu)+"""} & e-mail: \\textit{"""
+str(self.adres_email)+"} & "+slownik("funkcja", jezyk)+": \\textit{"+str(self.funkcja)+"""} \\\\
\\end{tabularx}
""")

@dataclasses.dataclass
class Kapitan(Zeglarz):
    """Klasa reprezentująca kapitana. Dziedziczy po żeglarzu."""
    def wypisz(self, jezyk):
        print("""\\section*{"""+slownik("INFORMACJE O KAPITANIE", jezyk)+"""}
\\begin{tabularx}{\\textwidth}{X X X}
"""+slownik("imię i nazwisko", jezyk)+": \\textit{"+str(self.imie_i_nazwisko)+"} & "+slownik("stop. żegl./mot.", jezyk)+": \\textit{"+
str(self.stopien_zeglarski)+"} & "+slownik("nr patentu", jezyk)+": \\textit{"+str(self.nr_patentu)+"""} \\\\
nr telefonu: \\textit{"""+str(self.nr_telefonu)+"""} & e-mail: \\textit{"""
+str(self.adres_email)+"""} \\\\
\\end{tabularx}
""")

@dataclasses.dataclass
class Jacht:
    """Klasa reprezentująca jacht, zawierająca dane techniczne"""
    nazwa: str = "."*27
    typ: str = "."*27
    nr_rej: str = "."*27
    lc: str = "."*27
    port_macierzysty: str = "."*27
    moc_silnika: str = "."*27
    def wypisz(self, jezyk):
        print("\\section*{"+slownik("INFORMACJE O JACHCIE", jezyk)+"""}

\\begin{tabularx}{\\textwidth}{X X X}
"""+slownik("nazwa", jezyk)+": \\textit{"+str(self.nazwa)+"} & "+slownik("typ", jezyk)+": \\textit{"
+str(self.typ)+"} & "+slownik("nr rej.", jezyk)+": \\textit{"+str(self.nr_rej)+"""} \\\\
lc[m]: \\textit{"""+str(self.lc)+"} & "+slownik("port macierzysty", jezyk)+": \\textit{"+str(self.port_macierzysty)
+"} & "+slownik("moc silnika", jezyk)+" [kW]: \\textit{"+str(self.moc_silnika)+"""} \\\\
\\end{tabularx}
""")

@dataclasses.dataclass
class Rejs:
    """Klasa reprezentująca rejs, zawiera informacje o portach i liczby godzin"""
    nr_plywania: str = "."*27
    data_zaokretowania: str = ""
    port_zaokretowania: str = ""
    plywowy_zaokretowania: str = "TAK/NIE"
    data_wyokretowania: str = ""
    port_wyokretowania: str = ""
    plywowy_wyokretowania: str = "TAK/NIE"
    odwiedzone_porty: str = ""
    liczba_portow_plywowych: str = ""
    pod_zaglami: str = ""
    na_silniku: str = ""
    zagle_i_silnik: str = "-"
    razem_godz_zeglugi: str = ""
    po_wodach_plywowych: str = ""
    powyzej_6B: str = ""
    w_portach_i_na_kotwicy: str = ""
    przebyto_mil_morskich: str = ""
    def wypisz(self, jezyk):
        print("\\section*{"+slownik("INFORMACJE O REJSIE", jezyk)+"""}

"""+slownik("Wpisu dokonano na podstawie dziennika jachtowego, nr pływania", jezyk)+": \\textit{"+str(self.nr_plywania)
+"""}
\\\\

\\begin{tabularx}{\\textwidth}{|X|X|X|}
\\hline
"""+slownik("Port zaokrętowania", jezyk)+": \\textit{"+str(self.port_zaokretowania)+"} & "+slownik("Data", jezyk)+": \\textit{"
+str(self.data_zaokretowania)+"} & "+slownik("Pływowy", jezyk)+": \\textit{"+slownik(self.plywowy_zaokretowania, jezyk)+"""} \\\\
\\hline
"""+slownik("Port wyokrętowania", jezyk)+": \\textit{"+str(self.port_wyokretowania)+"} & "+slownik("Data", jezyk)+": \\textit{"
+str(self.data_wyokretowania)+"} & "+slownik("Pływowy", jezyk)+": \\textit{"+slownik(self.plywowy_wyokretowania, jezyk)+"""} \\\\
\\hline
\\multicolumn{3}{|l|}{"""+slownik("Odwiedzone miejsca", jezyk)+":")

        if self.odwiedzone_porty=="":
            print("""\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
\\multicolumn{3}{|l|}{\\dotfill} \\\\
""")
        else:
            tmp=self.odwiedzone_porty.split("\n")
            for i in range(4):
                if i==0:
                    print("\\textit{"+tmp[i]+"}\\dotfill}\\\\")
                elif i<len(tmp):
                    print("\\multicolumn{3}{|l|}{\\textit{"+str(tmp[i])+"}\\dotfill} \\\\")
                else:
                    print("\\multicolumn{3}{|l|}{\\dotfill} \\\\")
        print("""\\hline
\\multicolumn{2}{|l|}{"""+slownik("W tym liczba portów pływowych", jezyk)+": \\textit{"+str(self.liczba_portow_plywowych)
+"}} & "+slownik("Liczba dni rejsu", jezyk)+": \\textit{"+("" if self.data_zaokretowania=="" or
self.data_wyokretowania=="" else str((datetime.strptime(self.data_wyokretowania, '%d.%m.%Y')
-datetime.strptime(self.data_zaokretowania, '%d.%m.%Y')).days+1))+"""}\\\\
\\hline
\\end{tabularx}
\\\\\\\\

\\begin{tabularx}{\\textwidth}{
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X"""+("""
|>{\\centering\\arraybackslash}X""" if self.zagle_i_silnik!="-" else "")+"""
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|>{\\centering\\arraybackslash}X
|}
\\hline
\\multicolumn{"""+("6" if self.zagle_i_silnik!="-" else "5")
+"}{|c|}{"+slownik("GODZINY ŻEGLUGI", jezyk)+"} & "+slownik("GODZINY POSTOJU", jezyk)+" & \\multirow{2}{2cm}{"+slownik("PRZEBYTO MIL MORSKICH", jezyk)+"""} \\\\
\\cline{1-"""+("7" if self.zagle_i_silnik!="-" else "6")+"""}
"""+slownik("pod żaglami", jezyk)+" & "+slownik("na silniku", jezyk)+" & "+(slownik("żagle i silnik", jezyk)+" &" if self.zagle_i_silnik!="-" else "")+
"\\textbf{"+slownik("razem godz. żegl.", jezyk)+"} & "+slownik("po wodach pływowych", jezyk)+" & "+slownik("powyżej", jezyk)+" $6^\\circ$B &"""+
" "+slownik("w portach i na kotwicy", jezyk)+""" & \\\\
\\hline
& &"""+(" &" if self.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\\huge """+str(self.pod_zaglami)+"&\\huge "+str(self.na_silniku)+" &\\huge "
+(str(self.zagle_i_silnik)+" &\\huge " if self.zagle_i_silnik!="-" else "")
+str(self.razem_godz_zeglugi)+
" &\\huge "+str(self.po_wodach_plywowych)+" &\\huge "+str(self.powyzej_6B)+" &\\huge """
+str(self.w_portach_i_na_kotwicy)+" &\\huge """+str(self.przebyto_mil_morskich)+""" \\\\
& &"""+(" &" if self.zagle_i_silnik!="-" else "")+""" & & & & \\\\
\\hline
\\end{tabularx}
""")

@dataclasses.dataclass
class OpiniaKapitana:
    """Klasa reprezentująca opinię kapitana"""
    pozytywna: int=None
    wywiazywanie_z_obowiazkow: int = None
    choroba_morska: int = None
    odpornosc_w_trudnych_warunkach: int= None
    uwagi: str = ""
    def wypisz(self, jezyk):
        def box(zaznaczone):
            if zaznaczone:
                return "\\XBox"
            return "\\Box"
        print("\\section*{"+slownik("OPINIA KAPITANA", jezyk)+" ~~~~~~~~ $"+box(self.pozytywna==0)
    +"$ "+slownik("pozytywna", jezyk)+" ~~~~~~~~ $"+box(self.pozytywna==1)+"$ "+slownik("negatywna", jezyk)+"""}

\\begin{tabularx}{\\textwidth}{X X X X}
\\multicolumn{4}{l}{\\textbf{"""+slownik("Z obowiązków wywiązywał/a się", jezyk)+""":}}\\\\
$"""+box(self.wywiazywanie_z_obowiazkow==0)+"$ "+slownik("bardzo dobrze", jezyk)+" & $"
+box(self.wywiazywanie_z_obowiazkow==1)+"$ "+slownik("dobrze", jezyk)+" & $"
+box(self.wywiazywanie_z_obowiazkow==2)+"$ "+slownik("dostatecznie", jezyk)+" & $"
+box(self.wywiazywanie_z_obowiazkow==3)+"$ "+slownik("niedostatecznie", jezyk)+"""\\\\
\\\\
\\multicolumn{4}{l}{\\textbf{"""+slownik("Chorobie morskiej", jezyk)+""":}}\\\\
$"""+box(self.choroba_morska==0)+"$ "+slownik("nie podlegał/a", jezyk)+" & $"
+box(self.choroba_morska==1)+"$ "+slownik("chorował/a ciężko", jezyk)+" & \\multicolumn{2}{l}{$"
+box(self.choroba_morska==2)+"$ "+slownik("chorował/a sporadycznie i mógł/mogła pracować", jezyk)+"""}\\\\
\\\\
\\multicolumn{4}{l}{\\textbf{"""+slownik("Odporność w trudnych warunkach", jezyk)+""":}}\\\\
$"""+box(self.odpornosc_w_trudnych_warunkach==0)+"$ "+slownik("dobra", jezyk)+" & $"
+box(self.odpornosc_w_trudnych_warunkach==1)+"$ "+slownik("dostateczna", jezyk)+" & $\\Box$ "+slownik("niedostateczna", jezyk)+" & $"
+box(self.odpornosc_w_trudnych_warunkach==2)+"$ "+slownik("nie sprawdzono", jezyk)+"""\\\\
\\end{tabularx}
""")
        print("\\section*{"+slownik("UWAGI KAPITANA", jezyk)+"""}

""")
        tmp=self.uwagi.split("\n")
        for i in range(3):
            if i<len(tmp):
                print("\\textit{"+str(tmp[i])+"}\\dotfill \\\\")
            else:
                print(".\\dotfill \\\\")

def wypisz_naglowek():
    """Funkcja wypisująca nagłówek dokumentu LaTeX"""
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

def wypisz_opinie(zalogant=Zalogant(), jacht=Jacht(), rejs=Rejs(),
opinia_kapitana=OpiniaKapitana(), kapitan=Kapitan(), logo=False, jezyk="pl"):
    """Funkcja wypisująca opinię jako kod dokumentu LaTeX"""
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
 \\textbf{\\huge """+slownik("OPINIA Z REJSU",jezyk)+"""} \\\\
 \\\\
\\hline
\\end{tabularx}
\\end{minipage}
""")

    else:
        print("""\\newpage
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \\hline
 \\\\
 \\textbf{\\huge """+slownik("OPINIA Z REJSU", jezyk)+"""} \\\\
 \\\\
\\hline
\\end{tabularx}
""")

    zalogant.wypisz(jezyk)

    jacht.wypisz(jezyk)

    rejs.wypisz(jezyk)

    opinia_kapitana.wypisz(jezyk)

    kapitan.wypisz(jezyk)
    
    print("""\\begin{tabularx}{\\textwidth}{X X}
\\\\\\\\
...................................... & ......................................\\\\
"""+slownik("miejscowość, data", jezyk)+" & "+slownik("podpis kapitana", jezyk)+"""\\\\
\\end{tabularx}""")


def wypisz_karte_rejsu(jacht=Jacht(), rejs=Rejs(), uwagi_kapitana="", kapitan=Kapitan(), zaloga=None,
armator=Osoba(), logo=False, jezyk="pl"):
    """Funkcja wypisująca kartę rejsu jako kod dokumentu LaTeX"""
    if zaloga is None:
        zaloga=[]
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
 \\textbf{\\huge """+slownik("KARTA REJSU", jezyk)+"""} \\\\
 \\\\
\\hline
\\end{tabularx}
\\end{minipage}
""")

    else:
        print("""\\newpage
\\begin{tabularx}{\\textwidth} { 
  | >{\\centering\\arraybackslash}X | }
 \\hline
 \\\\
 \\textbf{\\huge """+slownik("KARTA REJSU", jezyk)+"""} \\\\
 \\\\
\\hline
\\end{tabularx}
""")

    kapitan.wypisz(jezyk)

    jacht.wypisz(jezyk)

    rejs.wypisz(jezyk)

    print("\\section*{"+slownik("INFORMACJE O ZAŁODZE", jezyk)+"""}
    \\begin{tabular}{|m{0.013\\textwidth}|m{0.1727\\textwidth}|m{0.14\\textwidth}|m{0.08\\textwi"""
    +"""dth}||m{0.013\\textwidth}|m{0.1727\\textwidth}|m{0.14\\textwidth}|m{0.08\\textwidth}|}
    \\hline
    """+slownik("lp.", jezyk)+" & "+slownik("imię i nazwisko", jezyk)+" & "+slownik("stop. żegl./mot.", jezyk)+" & "+slownik("funkcja", jezyk)+" & "+slownik("lp.", jezyk)+" & "+slownik("imię i nazwisko", jezyk)+" &"
    +slownik("stop. żegl./mot.", jezyk)+" & "+slownik("funkcja", jezyk)+"""\\\\
    \\hline
    """)
    for i in range(6):
        if len(zaloga)>i:
            print(i+1, "&", zaloga[i].imie_i_nazwisko, "&", zaloga[i].stopien_zeglarski, "&",
            (zaloga[i].funkcja if "."*27!=zaloga[i].funkcja else ""), "&", end="")
        else:
            print("&&&&", end="")
        if len(zaloga)>i+6:
            print(i+7, "&", zaloga[i+6].imie_i_nazwisko, "&", zaloga[i+6].stopien_zeglarski, "&",
            (zaloga[i+6].funkcja if "."*27!=zaloga[i+6].funkcja else ""), end="")
        else:
            print("&&&", end="")
        print("""\\\\
\\hline""")
    print("""
    \\end{tabular}
    
    """)

    print("\\section*{"+slownik("UWAGI KAPITANA", jezyk)+"""}

""")
    tmp=uwagi_kapitana.split("\n")
    for i in range(2):
        if i<len(tmp):
            print("\\textit{"+str(tmp[i])+"}\\dotfill \\\\")
        else:
            print(".\\dotfill \\\\")

    print("""\\begin{tabularx}{\\textwidth}{X X}
\\\\\\
...................................... & ......................................\\\\
"""+slownik("miejscowość, data", jezyk)+" & "+slownik("podpis kapitana", jezyk)+"""\\\\
\\end{tabularx}""")

    print("\\section*{"+slownik("INFORMACJE O ARMATORZE", jezyk)+"""}

\\begin{tabularx}{\\textwidth}{X X}
"""+slownik("imię i nazwisko", jezyk)+"/"+slownik("nazwa", jezyk)+": \\textit{"+str(armator.imie_i_nazwisko)+"""} \\\\
"""+slownik("nr telefonu", jezyk)+": \\textit{"+str(armator.nr_telefonu)+"} & e-mail: \\textit{"
+str(armator.adres_email)+"""}\\\\
\\\\\\\\
...................................... & ......................................\\\\
"""+slownik("miejscowość, data", jezyk)+" & "+slownik("podpis armatora jachtu", jezyk)+"""\\\\
\\end{tabularx}""")

def wypisz_stopke():
    """Funkcja wypisująca zakończenie dokumentu LaTeX"""
    print("\\end{document}")
