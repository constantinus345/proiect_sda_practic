import pandas as pd

url = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&Tematica_dosarului=&Tipul_dosarului=All&items_per_page=50'


# paginarea cu -1 "&page=8"
tabel_total = pd.DataFrame()
# TODO = de facut functii
# TODO = cu re de extras doar numerele de la dosar
# TODO = 

for pg in range(9):
    #range(9) este un generator care merge de la 0 la 8
    print(f"Doing page {pg}")
    if pg > 0:
        url = f"{url}&page={pg}"
    
    tabel = pd.read_html(url)[0]
    tabel_total = pd.concat([tabel_total,tabel])

print(len(tabel_total))


file_excel_path = 'D:/Python_Code/proiect_sda_practic/data/justitie.xlsx'
try:
    tabel_total.to_excel(file_excel_path)
    print(f"Saved to {file_excel_path}")
except Exception as e: 
    print(e)



    

    
    