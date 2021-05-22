# 节点
class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name


# 普通边
class Edge(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_dest(self):
        return self.dest

    def __repr__(self):
        return f"{self.get_source()}->{self.get_source()}"


# 加权边
class WeightEdge(object):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_source(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.get_weight()

    def __repr__(self):
        return f"{self.get_source()}->({self.get_weight()}){self.get_dest()}"


# 图
class Digraph(object):

    def __init__(self):
        self.nodes = list()
        self.edges = dict()

    def add_node(self, node):
        if node in self.nodes:
            raise KeyError
        self.add_node(node)
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_source()

        if not (src in self.nodes and dest in self.nodes):
            raise KeyError("边的节点不在图里面")
        self.edges[src].append(dest)

    # 判断是否有关联
    def children_of(self, node):
        return self.edges[node]

    # 节点是否在图里面
    def has_node(self, node):
        return node in self.nodes
