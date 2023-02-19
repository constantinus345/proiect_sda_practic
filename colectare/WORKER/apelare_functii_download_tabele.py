from colectare.citirea_pagina import \
citire_tabel_din_url, salvare_tabel_in_excel

from configx import url, dosare_de_urmarit, id_Constantin
from helpers.tabel_helpers import transforma_tabel_alfanumeric,\
    filtreaza_lista_dosare_de_interes_puclient, tabel_filtrat
# from helpers.tabel_helpers import *
from helpers.telegram_mesaj import send_telegram_message

import asyncio


tbx = citire_tabel_din_url(url, 2)
tabel_tr = transforma_tabel_alfanumeric(tbx)

#salvare_tabel_in_excel(tbx, "date_noi.xlsx")
lista_dosare_de_informat = filtreaza_lista_dosare_de_interes_puclient(dosare_de_urmarit)
tabel_filtrat = tabel_filtrat(tabel_tr, lista_dosare_de_informat)

print(tabel_filtrat.columns)

judecatori = tabel_filtrat['Judecător'].tolist()
print(judecatori)
#TODO scoate date din tabel filtrat

for index,dosar in enumerate(lista_dosare_de_informat):
    mesaj = f"""Dosarul Dvs {dosar} are o noua hotarare,
    care va fi judecat de catre {judecatori[index]}
    """
    #trimite mesaj pe telegram
    asyncio.run(send_telegram_message(id_Constantin,mesaj))
    
    
    
