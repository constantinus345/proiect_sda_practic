import pandas as pd
import logging
import os
import configx


logging.basicConfig(level=logging.DEBUG,filename=configx.path_logs, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
#file_handler = logging.FileHandler(config.path_logs)
#logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
""" 
Niveluri de logging dupa ordinea importantei:
Debug - codul: logging.debug("mesaj")
Info  - codul: logging.info("mesaj_2")
Warning
Errror
Critical
"""




def citire_tabel_din_url(url, nr_pagini):
    # paginarea cu -1 "&page=8"
    tabel_total = pd.DataFrame()

    for pg in range(nr_pagini):
        #range(nr_pagini) este un generator care merge de la 0 la 8
        print(f"Doing page {pg}")
        if pg > 0:
            url = f"{url}&page={pg}"
        
        try:
            tabel = pd.read_html(url)[0]
            tabel_total = pd.concat([tabel_total,tabel])
            logger.info(f"Page {pg} done")
        except Exception as e:
            logger.error(f"Error on page {pg}")

    logger.info(f"Done {nr_pagini} pages, tabelul are {len(tabel_total)} linii")
    return tabel_total


def salvare_tabel_in_excel(tabelul, path_to_excel):
    try:
        tabelul.to_excel(f"{configx.Path_data}/{path_to_excel}")
        #tabelul.to_excel("D:/Python/data/date_noi")
        #print(f"Saved to {path_to_excel}")
        logger.info(f"Saved to {path_to_excel}")
    except Exception as e: 
        logger.critical(f"Error on saving table to {path_to_excel}")
        print(e)


if __name__ == "__main__":
    # este o metoda care executa codul doar daca este rulat direct
    # codul din interiorul if nu va fi rulat daca este importat
    # __name__ este o variabila speciala care are valoarea __main__ daca este rulat direct
    print(7)
    

    

    
    