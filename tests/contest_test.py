# /home/michaelleitner/Documents/contest/ConTest-Tree/out/trace-length-ts-admin-basic-info-service-sprintstarterweb_1.5.22-final.csv
import polars as pl
from polars import col

from contest_tree.model.Node import Node
from contest_tree.model.Root import Root

df = pl.read_csv(
    "/home/michaelleitner/Documents/contest/ConTest-Tree/out/trace-length-ts-admin-basic-info-service-sprintstarterweb_1.5.22-final.csv"
)
print(df.shape)

root_spans = df.filter(col("childSpanId") == None)
final_df_list =[]


def build_tree(cur_node: Node):
    lookup = cur_node.data[1]
    found_spans = df.filter(col("childSpanId") == lookup)
    for span in found_spans.iter_rows():
        node = Node(data=span)
        cur_node.add_children([node])
        build_tree(node)


for cur_root in root_spans.iter_rows():
    root = Root(data=cur_root)

    build_tree(root)
    tree = root.init_tree()
    # print(tree)

    # print(tree.all_nodes)
    final_df_list.append(pl.from_dicts(tree.to_polars_readable_format()))


final = pl.concat(final_df_list)
print(final.shape)