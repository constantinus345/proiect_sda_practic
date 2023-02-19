import pandas
from helpers.json_transform import extr, filter_json_cu_valori_goale
import configx

def transforma_tabel_alfanumeric(tabel):
    
    tabel[configx.col_dosar_name] = tabel[configx.col_dosar_name].apply(extr)
    
    #df['A'] = df['A'].apply(add_2)
    return tabel

def filtreaza_tabel_de_interes_puclient(jsonx):
    
    lista_dosare_de_informat = []
    # lista_to_inform = filter_json_cu_valori_goale(configx.dosare_de_urmarit)
    # print(lista_to_inform)
    dosar_de_informat = filter_json_cu_valori_goale(jsonx)
    print(dosar_de_informat)
    for el in dosar_de_informat:
        lista_dosare_de_informat.append(extr(el['nr_dosar']))
    
    print(lista_dosare_de_informat)
    
    return lista_dosare_de_informat

def tabel_filtrat(tabel, lista_dosare_de_informat):
    tabel_filtrat = tabel[tabel[configx.col_dosar_name].isin(lista_dosare_de_informat)]
    return tabel_filtrat

