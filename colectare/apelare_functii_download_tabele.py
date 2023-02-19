from colectare.citirea_pagina import \
citire_tabel_din_url, salvare_tabel_in_excel

from configx import url

tbx = citire_tabel_din_url(url, 2)

salvare_tabel_in_excel(tbx, "date_noi.xlsx")