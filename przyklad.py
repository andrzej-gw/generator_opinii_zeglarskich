"""Moduł zwierający klasy i funkcje do generowania opinii."""
from generator_opinii_zeglarskich import (Zalogant, Zeglarz, Kapitan, Jacht, Rejs,
OpiniaKapitana, Osoba, wypisz_karte_rejsu, wypisz_naglowek, wypisz_opinie, wypisz_stopke, wypisz_mayday, wypisz_TabelkaWachtowa)

#dane zalogi mozna wziac np. z arkusza i odpowiednio sformatowac
DANE_ZALOGI = """Jan Kowalski	ISNS	654345643	jan.kowalski@op.pl	żeglarz jachtowy	PU/43543	załoga
Bogdan Brzozowski		753456432	bogbrz3030@gmail.com	JSM	PU/32345	I Oficer
Miłosz Piotrkowski	WNE	345622234	milosz.piotrkowski@gmail.com	żeglarz jachtowy	PU/23453	II Oficer
Bożena Zbroch	Wydział Fizyki	645234566	bozena.zbroch.a@gmail.com	żeglarz jachtowy	PU/34522	załoga
Karolina Czajkowska	Fuw	453654333	ka.czajkowska@student.uw.edu.pl	Jakieś tam mam	PU/75435	III Oficer
Paweł Stępiński	MISMAP (matematyka)	544334323	pawel.p.stepinski@gmail.com	żeglarz jachtowy	PU/23345	załoga
Julia Kostek	Wdib	453643132	juliakostek@wp.pl	brak	brak	załoga
Bartosz Frankowski	WPiA	+48123432234	ba.frankowski@student.uw.edu.pl	żeglarz jachtowy	 	załoga"""
DANE_ZALOGI = DANE_ZALOGI.split('\n')
for i, dana in enumerate(DANE_ZALOGI):
    DANE_ZALOGI[i] = dana.split("\t")
#zaloga to lista skladajaca sie z obiektow klasy Zalogant
zaloga = []
for z in DANE_ZALOGI:
    zaloga.append(
        Zalogant(imie_i_nazwisko = z[0],
        stopien_zeglarski = z[4],
        nr_patentu = z[5],
        nr_telefonu = z[2],
        adres_email = z[3],
        funkcja = z[6])
    )

kapitan = Kapitan(imie_i_nazwisko = "Andrzej Gwiazda", stopien_zeglarski = "Kapitan Jachtowy",
nr_patentu = "4052", nr_telefonu = "+48 788 132 046", adres_email = "jedrekgwiazda@gmail.com")

jacht=Jacht(nazwa="s/y Figaro", typ="Bavaria 45 BT ‘12")

rejs=Rejs(
    data_zaokretowania="23.09.2023",
    port_zaokretowania="Sukošan",
    plywowy_zaokretowania="NIE",
    data_wyokretowania="30.09.2023",
    port_wyokretowania="Sukošan",
    plywowy_wyokretowania="NIE",
    odwiedzone_porty="Rogoznica, Šibenik,\n Skradin,\n Murter",
    liczba_portow_plywowych="0",
    pod_zaglami="22",
    na_silniku="18",
    zagle_i_silnik="-",
    razem_godz_zeglugi=40,
    po_wodach_plywowych="0",
    powyzej_6B="2",
    w_portach_i_na_kotwicy="118",
    przebyto_mil_morskich="160"
)

#przykladowa pozytywna opinia
pozytywna_opinia=OpiniaKapitana(pozytywna=0, wywiazywanie_z_obowiazkow=1, choroba_morska=0,
odpornosc_w_trudnych_warunkach=0, uwagi="Super załogant!")

#przykladowa negatywna opinia
negatywna_opinia=OpiniaKapitana(pozytywna=1, wywiazywanie_z_obowiazkow=3, choroba_morska=2,
odpornosc_w_trudnych_warunkach=2, uwagi="Beznadziejny załogant!")

armator = Osoba(imie_i_nazwisko="Czarter jachtów", nr_telefonu="+54 345 322 654",
adres_email="czarter@jachtow.pl")

#naglowek potrzebny jest do rozpoczecia dokumentu w .tex (wywolac dokladnie raz na poczatku)
wypisz_naglowek()

wypisz_karte_rejsu(jacht=jacht, rejs=rejs, uwagi_kapitana="Super rejs.", kapitan=kapitan,
zaloga=zaloga, armator=armator, logo=True)

for z in zaloga:
    wypisz_opinie(z, jacht=jacht, rejs=rejs, logo=True, opinia_kapitana=pozytywna_opinia,
    kapitan=kapitan)

wypisz_opinie(zaloga[0], jacht=jacht, rejs=rejs, logo=True, opinia_kapitana=pozytywna_opinia,
kapitan=kapitan)

wypisz_opinie(zaloga[0], jacht=jacht, rejs=rejs, logo=False, opinia_kapitana=negatywna_opinia,
kapitan=kapitan)

wypisz_opinie(zaloga[0], jacht=jacht, rejs=rejs, logo=True, kapitan=kapitan)
wypisz_opinie()
wypisz_karte_rejsu()
wypisz_opinie(logo=True)
wypisz_karte_rejsu(logo=True)
wypisz_opinie(jezyk="eng")
wypisz_karte_rejsu(jezyk="eng")
wypisz_opinie(jezyk="eng", logo=True)
wypisz_karte_rejsu(jezyk="eng", logo=True)

wypisz_mayday(jacht=jacht, logo = True)
wypisz_TabelkaWachtowa(4,7,logo=True)

#stopka potrzebna jest do zakonczenia dokumentu .tex (wywolac dokladnie raz na koncu)
wypisz_stopke()
