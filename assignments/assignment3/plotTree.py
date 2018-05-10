import pydot
import twoThree

def plotTree(node, name):
    def describe(node):
        if node.nodeType == 2:
            return str(node.d1)
        elif node.nodeType == 3:
            return str(node.d1) + " " + str(node.d2)
    def draw(parentNode, childNode):
        edge = pydot.Edge(describe(parentNode), describe(childNode))
        graph.add_edge(edge)
    def visit(node):
        if node == None:
            return
        if node.parent != None:
            draw(node.parent, node)
        if node.nodeType == 2:
            visit(node.c1)
            visit(node.c2)
        elif node.nodeType == 3:
            visit(node.c1)
            visit(node.c2)
            visit(node.c3)
    graph = pydot.Dot(graph_type='graph')
    graph.add_node(pydot.Node(describe(node)))
    visit(node)
    graph.write_png(name)
