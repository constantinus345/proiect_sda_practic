import re
import configx

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
    clienti_to_inform = []
    for client in dosar_json['clienti']:
        if client['data_informare'] == '':
            clienti_to_inform.append(client)
            
    print(f"Din {len(dosar_json['clienti'])} clienti \
        avem {len(clienti_to_inform)} clienti de informat".replace("  ",""))
        
    #imi returneaza lista de clienti care trebuie sa-i informez
    return clienti_to_inform

if __name__=="__main__":
    lista_to_inform = filter_json_cu_valori_goale(configx.dosare_de_urmarit)
    print(lista_to_inform)


