from contest_tree.model.Node import Node


class Tree:
    def __init__(self, root_node: Node):
        self.root_node = root_node
        self.all_nodes = root_node.flatten_nodes()

    def __str__(self):
        return self.root_node.__str__()

    def to_polars_readable_format(self):
        res_dict = {"spanID": [], "max_depth": [], "min_depth": []}

        for node in self.all_nodes:
            max_depth, min_depth = node.get_depth_stat_of_node()
            res_dict["max_depth"].append(max_depth[0])
            res_dict["min_depth"].append(min_depth[0])
            res_dict["spanID"].append(node.data[1])

        return res_dict
