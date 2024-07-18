from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.countries = DAO.getAllCountries()
        self.myGraph = nx.Graph()
        self.dict = {}
        self.retailers = []
        self.somma = 0



    def buildGraph(self, country, year):
        self.retailers = DAO.getAllRetailers(country)
        for retailer in self.retailers:
            self.myGraph.add_node(retailer.code)
        for r1 in self.myGraph.nodes:
            for r2 in self.myGraph.nodes:
                if r1 != r2:
                    peso = DAO.getPesoArco(r1,r2,year)
                    if len(peso) > 0:
                        self.myGraph.add_edge(r1,r2,weight=len(peso))
        print(self.myGraph)
        for r in self.retailers:
            self.dict[r.code] = r.name

    def volumi(self):
        dict_volumi = {}
        for node in self.myGraph.nodes:
            volume = 0
            for neigh in self.myGraph.neighbors(node):
                volume += self.myGraph[node][neigh]['weight']
            dict_volumi[node] = volume
        return dict_volumi


    def ricorsione(self,parziale, n):
        n_first = parziale[0]
        n_last = parziale[-1]
        if len(parziale) == n-1:
            parziale.append(n_first)
            print(parziale)
            self.somma += 1
        else:
            neighbors = list(self.myGraph.neighbors(parziale[-1]))
            for neigh in neighbors:
                print(f"vedo se {neigh} è valido")
                if neigh not in parziale:
                    print("lo è")
                    parziale.append(neigh)
                    self.ricorsione(parziale, n)
                    parziale.pop()





    def parziale_valido(self, parziale, n):
        if len(parziale) == 1:
            return True
        if len(parziale) == 2 and n != 2:
            if parziale[0] == parziale[1]:
                return False
        else:
            print(f'parziale {parziale}')
            for i in range(len(parziale)):
                   if i != len(parziale) - 1:
                    print(f"nodo che verifico {parziale[i]}, ultimo nodo {parziale[-1]}")
                    if parziale[-1] == parziale[i]:
                        return False
            return True






