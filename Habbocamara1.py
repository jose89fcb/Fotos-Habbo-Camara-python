import requests
import os
import json
import pathlib

HabboNombre = input("Escribe el habbo Nombre: ")
HabboHotel= input("Escribe el hotel: ")
habbo = requests.get(f"https://www.habbo.{HabboHotel}/api/public/users?name={HabboNombre}")
IDHabbo= habbo.json()["uniqueId"]
IDHOTEL = habbo.json()['uniqueId'].split("-")[-2]
os.system("cls")

url = f"https://www.habbo.{HabboHotel}/extradata/public/users/{IDHabbo}/photos"
data = requests.get(url).json()





Nombre_carpeta= input("Escribe el nombre de la carpeta: ")
os.system("cls")
Carpeta=f"{Nombre_carpeta}"
pathlib.Path(Carpeta).mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),Carpeta)) 

#os.mkdir(os.path.join(os.getcwd(),Carpeta))

i = 1 
reemplazar=f"https://habbo-stories-content.s3.amazonaws.com/servercamera/purchased/{IDHOTEL}/"
for key in data:
    link=""
    link = 'https:' + key['url']
    response = requests.get(link)
    NombreArchivo = data[0]['url'].split("/")[-1]
    if response.status_code == 200:
        if link and not "image/png;" in link:
            with open(f"{link}".replace(f"{reemplazar}",""), "wb") as f:
                img = requests.get(link)
                f.write(img.content)
                print(f"Descargando...",i, link.replace(f"{reemplazar}",""))
            i += 1
