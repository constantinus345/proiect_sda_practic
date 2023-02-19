import pandas as pd

import config

def citire_tabel_din_url(url, nr_pagini):
    # paginarea cu -1 "&page=8"
    tabel_total = pd.DataFrame()

    for pg in range(nr_pagini):
        #range(nr_pagini) este un generator care merge de la 0 la 8
        print(f"Doing page {pg}")
        if pg > 0:
            url = f"{url}&page={pg}"
        
        tabel = pd.read_html(url)[0]
        tabel_total = pd.concat([tabel_total,tabel])

    return tabel_total


def salvare_tabel_in_excel(tabelul, path_to_excel):
    try:
        tabelul.to_excel(f"{config.Path_data}/{path_to_excel}")
        print(f"Saved to {path_to_excel}")
    except Exception as e: 
        print(e)

# file_excel_path = '/justitie.xlsx'

if __name__ == "__main__":
    # este o metoda care executa codul doar daca este rulat direct
    # codul din interiorul if nu va fi rulat daca este importat
    # __name__ este o variabila speciala care are valoarea __main__ daca este rulat direct
    print(7)
    

    

    
    