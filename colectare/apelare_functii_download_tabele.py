from colectare.citirea_pagina import \
citire_tabel_din_url, salvare_tabel_in_excel

from configx import url, dosare_de_urmarit
from helpers.tabel_helpers import transforma_tabel_alfanumeric,\
    filtreaza_tabel_de_interes_puclient, tabel_filtrat
# from helpers.tabel_helpers import *


tbx = citire_tabel_din_url(url, 2)
tabel_tr = transforma_tabel_alfanumeric(tbx)
#salvare_tabel_in_excel(tbx, "date_noi.xlsx")
lista_dosare_de_informat = filtreaza_tabel_de_interes_puclient(dosare_de_urmarit)
tabel_filtrat = tabel_filtrat(tabel_tr, lista_dosare_de_informat)

for dosar in lista_dosare_de_informat:
    mesaj = f"Dosarul Dvs {dosar} are o noua hotarare"
    print(mesaj)
    
