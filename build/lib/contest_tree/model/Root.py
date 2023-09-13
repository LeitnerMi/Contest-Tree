from contest_tree.model.Node import Node
from contest_tree.model.Tree import Tree


class Root(Node):
    def __init__(self, data: object = None):
        super().__init__(data)

    def init_tree(self):
        self.calc_length_of_child_nodes()
        self.set_root_on_children()

        return Tree(root_node=self)
