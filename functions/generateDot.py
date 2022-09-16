import operator
import os
from functions.dataProccess import getIndexOfElement, objCoincidence
from functions.getPath import getPath
from functions.graphviz import Graphviz
class generateDot:
    def __init__(self):
        self.graph=Graphviz()
        

    def generateGraphHospital(self,json):
        typeFile=input("Ingrese el tipo de Archivo que desea:\n")
        obj=self.orderJsonHospital(json)
        for i in (range(obj["Iterations"])):
            os.system('cls')
            self.graph.node.resetCount()
            code=self.graph.graphNoDiHeader(obj["Name"])
            code+="\n"
            for station in obj["Stations"]:
                code+=self.graph.headerSubGraph(station["Nombre"],station["Color"])
                code+=self.graph.headerSubGraph("Paciente en Atencion","honeydew4")
                if len(station["Patients"])>0:
                    code+=station["Patients"].pop(0)+";\n"
                else:
                    code+=self.graph.invisibleNode()
                code+="}\n"
                code+=self.graph.headerSubGraph("En espera","gray")
                if len(station["Patients"])>0:
                    code+=";\n".join(station["Patients"])
                    code+=";\n"
                else:
                    code+=self.graph.invisibleNode()
                code+="}\n"
                
                code+="}\n"
            code+="}\n"
            directionDot=getPath()+'\\\\dotFiles\\\\generate.dot'
            directionFile=getPath()+'\\\\generateFiles\\\\example'+str(i)+'.'+typeFile
            archie=open(directionDot,"w")
            archie.write(code)
            archie.close()
            os.system("dot -T"+typeFile+" "+directionDot+" -o "+directionFile)
            os.system(directionFile)
            input("Presione cualquier tecla para continuar...............")
        os.system('cls')

   
    
    def generateGraphOrganigrama(self,json):
        typeFile=input("Ingrese el tipo de Archivo que desea:\n")
        code=self.graph.graphDiHeader(json["Nombre"])
        for nod in json["Nodos"]:
            code+=self.graph.GeneralNode(nod["Name"],"circle")
            if len(nod["Sons"])>0:
                code+=self.graph.relations(nod["Name"],nod["Sons"])
        code+="}\n"
        directionDot=getPath()+'\\\\dotFiles\\\\organigrama.dot'
        directionFile=getPath()+'\\\\generateFiles\\\\example2.'+typeFile
        archie=open(directionDot,"w")
        archie.write(code)
        archie.close()
        os.system("dot -T"+typeFile+" "+directionDot+" -o "+directionFile)
        os.system(directionFile)
            

    def orderJsonHospital(self,json):
        arrRepet=objCoincidence(json["Pacientes"])
        norep=max(arrRepet.items(),key=operator.itemgetter(1))[0]   
        count= 1
        copy={"Name":json["Nombre"],"Stations":json["Estaciones"]}
        for pa in json["Pacientes"]:
            pos=getIndexOfElement(copy["Stations"],'Nombre',pa)
            if pos!=-1:
                if "Patients" in copy["Stations"][pos]:
                    copy["Stations"][pos]["Patients"].append("P"+str(count))
                else:
                    copy["Stations"][pos]["Patients"]=[]
                    copy["Stations"][pos]["Patients"].append("P"+str(count))
            count+=1
        copy["Iterations"]=arrRepet[norep]
        return copy



