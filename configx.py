import os

dosare_de_urmarit = {"clienti":[{
                     "nume_client":"Ion",
                     "nr_dosar":"18-2p/o-2352-15112013",
                     "data_inregistrare":"2023-11-15",
                     "data_informare":""},
                     {"nume_client":"Ana",
                     "nr_dosar":"20-1-7892-03072013",
                     "data_inregistrare":"2023-01-18",
                     "data_informare":"2023-04-14"
                     }]}


url = 'https://instante.justice.md/ro/hotaririle-instantei?Instance=All&Numarul_dosarului=&Denumirea_dosarului=&Tematica_dosarului=&Tipul_dosarului=All&items_per_page=50'

Path_data = 'D:/Python_Code/proiect_sda_practic/data'


#__________________________________
#logs
current_dir = os.getcwd().replace('\\','/')
Folder_logger_partial = 'logs'

if not os.path.exists(f"{current_dir}/{Folder_logger_partial}"):
    os.makedirs(f"{current_dir}/{Folder_logger_partial}")
#am creat folderul de logs daca el nu exista
    
path_logs = f"{current_dir}/{Folder_logger_partial}/loguri.log"

col_dosar_name = 'Numărul dosarului'

tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
id_Constantin = 1307289323

if __name__=='__main__':
    print(path_logs)

