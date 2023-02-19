import re
import configx

import sys
print(sys.path)


extr = lambda strx: "".join(re.findall('[a-zA-Z\d]+', strx))
#functie lambda care extrage doar caracterele cifre&litere dintr-un string

def transform_dosare_json(dosar_json):
    
    for client in dosar_json['clienti']:
        client['nr_dosar'] = extr(client['nr_dosar'])
        #am folosit functia lambda de mai sus extr
    #am modificat cheia dosar_json['clienti'][x]['nr_dosar'] in caractere alfanumerice
    #apoi am returnat dosar_json modificat
    return dosar_json

def filter_json_cu_valori_goale(dosar_json):
    
    for client in dosar_json['clienti']:
        if client['data_informare'] == '':
            dosar_json['clienti'].remove(client)
    
    
    #imi returneaza dosarul filtrat
    return dosar_json



