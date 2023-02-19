

dosare_de_urmarit = ['18-2p/o-2352-15112013',
                     '20-1-7892-03072013',
                     '28-2p/o-1282-09072016',
                     '22-5r-1336-17032014']


url = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&Tematica_dosarului=&Tipul_dosarului=All&items_per_page=50'

Path_data = 'D:/Python_Code/proiect_sda_practic/data'

import os
pa = pa = 'parola_secreta'
os.environ['pa_sec'] = pa
#cele doua linii de mai sus stocheaza parola secreta 
# in sistemul de operare

par = os.environ.get('pa_sec')
#linia de mai sus extrage parola secreta din sistemul de operare
print(par)



