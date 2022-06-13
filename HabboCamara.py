import requests
import os
import json

HabboNombre = input("Escribe el habbo Nombre: ")
habbo = requests.get(f"https://www.habbo.es/api/public/users?name={HabboNombre}")
IDHabbo= habbo.json()["uniqueId"]
os.system("cls")

url = f"https://www.habbo.es/extradata/public/users/{IDHabbo}/photos"
data = requests.get(url).json()

Nombre_carpeta= input("Escribe el nombre de la carpeta: ")
os.system("cls")
Carpeta=f"{Nombre_carpeta}"
os.mkdir(os.path.join(os.getcwd(),Carpeta))
os.chdir(os.path.join(os.getcwd(),Carpeta))
i = 1 
for key in data:
    imagen_url = 'https:' + key['url']
    response = requests.get(imagen_url)
    NombreArchivo = data[0]['url'].split("/")[-1]
    if response.status_code == 200:
        with open(str(i)+".-"+NombreArchivo,  "wb") as f:
            f.write(response.content)
            print("Descargando...", i)

        i +=1
