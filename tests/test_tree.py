from contest_tree.model.Node import Node
from contest_tree.model.Root import Root

def test1():
    root = Root(data="root")
    node1 = Node(data="1")
    node11 = Node(data="11")
    node12 = Node(data="12")
    node21 = Node(data="21")
    node22 = Node(data="22")
    node23 = Node(data="23")
    node31 = Node(data="31")

    node111 = Node(data="111")
    node112 = Node(data="112")
    node113 = Node(data="113")

    node23.add_children([node31])
    node11.add_children([node111, node112, node113])
    node12.add_children([node21, node22, node23])

    root.add_children([node1, node11, node12])

    tree = root.init_tree()
    print(tree)

    print("\nDepth statistics are displayed in: (max, min, mean, own_level): ")
    print(f"    Root node: has following depth statistics: {root.get_depth_stat_of_node()}")
    print(f"    Node 11: has following depth statistics: {node11.get_depth_stat_of_node()}")
    print(f"    Node 12: has following depth statistics: {node12.get_depth_stat_of_node()}")
    print(f"    Node 23: has following depth statistics: {node23.get_depth_stat_of_node()}")
    print(f"    Node 31: has following depth statistics: {node31.get_depth_stat_of_node()}")



def test2():
    root = Root("root")
    node1 = Node(data=1)
    node2 = Node(data=2)
    node3 = Node(data=3)
    node31 = Node(data=31)
    node4 = Node(data=4)
    node41 = Node(data=41)

    node3.add_children([node4])
    node31.add_children([node41])
    node2.add_children([node3, node31])
    node1.add_children([node2])
    root.add_children([node1])
    tree = root.init_tree()
    print(tree)
    print(root.get_depth_stat_of_node())

    print(tree.to_polars_readable_format())


test1()