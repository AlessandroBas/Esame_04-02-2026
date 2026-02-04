import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.roles=[]
        self.get_roles()

    def get_roles(self):
        self.roles = DAO.get_roles()
        return self.roles

    def build_graph(self, role):
        self.G.clear()
        self.artists = DAO.get_artists(role)
        for artist in self.artists:
            self.G.add_node(artist)

        for i, t1 in enumerate(self.artists):
            for t2 in self.artists[i + 1:]:
                w= int(t1.num_objects) - int(t2.num_objects)
                if w == 0:
                    continue
                if w>0:
                    self.G.add_edge(t1,t2,weight=w)
                else:
                    w=-w
                    self.G.add_edge(t2,t1,weight=w)


    def classifica(self):
        classifica = []
        for n in self.G.nodes:
            score = 0
            for e_out in self.G.out_edges(n, data=True):
                score += e_out[2]["weight"]
            for e_in in self.G.in_edges(n, data=True):
                score -= e_in[2]["weight"]

            classifica.append((n, score))

        return classifica.sort(reverse=True, key=lambda x: x[1])

    def get_num_of_nodes(self):
        return self.G.number_of_nodes()

    def get_num_of_edges(self):
        return self.G.number_of_edges()
