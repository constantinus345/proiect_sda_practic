import os
pa = pa = 'parola_secreta'
os.environ['pa_sec'] = pa
#cele doua linii de mai sus stocheaza parola secreta 
# in sistemul de operare

par = os.environ.get('pa_sec')
#linia de mai sus extrage parola secreta din sistemul de operare
print(par)