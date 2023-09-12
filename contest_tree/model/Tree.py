from contest_tree.model.Node import Node


class Tree:
    def __init__(self, root_node: Node):
        self.root_node = root_node
        self.all_nodes = root_node.flatten_nodes()


    def __str__(self):
        return self.root_node.__str__()