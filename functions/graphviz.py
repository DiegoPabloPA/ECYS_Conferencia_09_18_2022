from functions.node import Node
class Graphviz:

    def __init__(self):
        self.node=Node()

    def relations(self,father,sons):
        return """
        {f}-> {kopen}
        {body};
        {kclose}
        """.format(f=father,kopen='{',kclose='}',body=";\n".join(sons))

    def graphNoDiHeader(self,title):
        return """
            graph  grafi{key}
                rankdir=TB;
                labelloc=\"t\";
                label=\"{tit}\";
                node[shape=\"circle\"
                fixedsize=true
                width=0.8
                height=0.8
                ];
        """.format(key='{',tit=title)

    def graphDiHeader(self,title):
        return """
            digraph  grafi{key}
                rankdir=TB;
                labelloc=\"t\";
                label=\"{tit}\";
                node[shape=\"circle\"
                fixedsize=true
                width=3
                height=3
                ];
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