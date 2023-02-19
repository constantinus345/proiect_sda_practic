from git import Repo
#pip3 install GitPython

github_url= 'https://github.com/constantinus345/proiect_sda_practic'
folder_to_clone_to = 'D:/Python_Code/proiect_sda_practic/folder_cursanti'

Repo.clone_from(github_url, folder_to_clone_to)