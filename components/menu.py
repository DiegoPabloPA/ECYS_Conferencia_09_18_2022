import os
from functions.UploadFile import Files
from functions.dataProccess import objCoincidence
from functions.generateDot import generateDot
class Menu:
    def __init__(self):
        self.generate=generateDot()
    
    def startMenu(self):
        opt=0
        json=[]
        while opt!=3:
            print("Bienvenido al Programa Realizado para la Conferencia:")
            print("1.Cargar Archivo \n2.Realizar Graficos \n3.Salir")
            opt=int(input("Selección: "))
            if opt==1:
                os.system('cls')
                dire=input("Ingrese la dirección del archivo Formato JSON:\n")
                json=Files.uploadFile(dire)
            elif opt==2:
                os.system('cls')
                if json.__len__()==0:
                    print("Debe cargar un archivo antes de generar un grafico")
                else:
                    if json["Tipo"]=='D':
                        self.generate.generateGraphOrganigrama(json)
                    else:
                        self.generate.generateGraphHospital(json)     
            elif opt==3:
                os.system('cls')
                print ("Programa realizado con fin didáctico Realizado por Diego Pérez\nHasta la proxima!\n")
            else:
                os.system('cls')
                print("Opción inválida por favor seleccione una opción correcta\n") 

    
    