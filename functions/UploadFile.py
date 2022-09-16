import json 
import os 
class Files:
    def uploadFile(directory):
        try:
            archie=open(directory,"r")
            content=archie.read()
            archie.close()
            os.system('cls')
            print("Archivo cargado con exito proceda a generar el diagrama :)\n")
            return json.loads(content)
            
        except:
            print("Error con su archivo :(\n")
            return[]
        
        