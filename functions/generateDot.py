import operator
import os
from functions.dataProccess import getIndexOfElement, objCoincidence
from functions.getPath import getPath
from functions.node import Node
class generateDot:
    def __init__(self):
        self.node=Node()

    def graphNoDiHeader(self,title):
        return """
        graph  grafi{key}
            rankdir=TB;
            labelloc=\"t\";
            label=\"{tit}\";
        """.format(key='{',tit=title)
    def graphDiHeader(self,title):
        return """
        digraph  grafi{key}
            rankdir=TB;
            labelloc=\"t\";
            label=\"{tit}\";
        """.format(key='{',tit=title)

    def headerSubGraph(self,tit,color):
        return """
        subgraph cluster_{num} {key}
            node [style=filled shape="circle"];
            style=\"filled\";
            color=\"{col}\";
            label=\"{title}\";
        """.format(num=self.node.addCount(),key='{',title=tit,col=color)

    def invisibleNode(self):
        return "inv"+self.node.addCount()+"[label=\"\" shape=\"plaintext\"];\n"

    def GeneralNode(self,name,form):
        return name+"[shape=\""+form+"\"];\n"


    def generateGraphHospital(self,json):
        typeFile=input("Ingrese el tipo de Archivo que desea:\n")
        obj=self.orderJsonHospital(json)
        for i in (range(obj["Iterations"])):
            os.system('cls')
            self.node.resetCount()
            code=self.graphNoDiHeader(obj["Name"])
            code+="\n"
            for station in obj["Stations"]:
                code+=self.headerSubGraph(station["Nombre"],station["Color"])
                code+=self.headerSubGraph("Paciente en Atencion","honeydew4")
                if len(station["Patients"])>0:
                    code+=station["Patients"].pop(0)+";\n"
                else:
                    code+=self.invisibleNode()
                code+="}\n"
                code+=self.headerSubGraph("En espera","gray")
                if len(station["Patients"])>0:
                    code+=";\n".join(station["Patients"])
                    code+=";\n"
                else:
                    code+=self.invisibleNode()
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

    def relations(self,father,sons):
        return """
        {f}-> {kopen}
        {body};
        {kclose}
        """.format(f=father,kopen='{',kclose='}',body=";\n".join(sons))  
    
    def generateGraphOrganigrama(self,json):
        typeFile=input("Ingrese el tipo de Archivo que desea:\n")
        code=self.graphDiHeader(json["Nombre"])
        for nod in json["Nodos"]:
            code+=self.GeneralNode(nod["Name"],"circle")
            if len(nod["Sons"])>0:
                code+=self.relations(nod["Name"],nod["Sons"])
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



