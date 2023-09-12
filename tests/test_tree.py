from contest_tree.model.Node import Node
from contest_tree.model.Root import Root

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

print(tree.all_nodes)
print(root.get_depth_stat_of_node())
