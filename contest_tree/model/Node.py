import uuid
from statistics import mean

from contest_tree.model.TreeSettings import TreeSettings


class Node:
    def __init__(self, data: object = None, children: list["Node"] = None, _uuid=None):
        self.root = self
        self.parent = self
        self.depth = -1

        if _uuid is None:
            self.uuid = uuid.uuid4()
        else:
            self.uuid = _uuid
        if data is None:
            self.data = {}
        else:
            self.data = data

        if children is None:
            self.children = []
        else:
            self.children = children

    def add_children(self, add_children: list["Node"]):
        self.children.extend(add_children)
        for child in add_children:
            child.parent = self

    def calc_length_of_child_nodes(self, result=None, depth=0) -> list[tuple]:
        if result is None:
            result = []
        for child in self.children:
            result = child.calc_length_of_child_nodes(result, depth + 1)

        self.depth = depth
        result.append((self.depth, self.data))
        return result

    def calc_length_of_leaves(self, result=None, depth=0) -> list[tuple]:
        if result is None:
            result = []
        for child in self.children:
            result = child.calc_length_of_leaves(result, depth + 1)

        if len(self.children) == 0:
            result.append((depth, self.data))
        return result

    def get_depth_stat_of_node(self) -> tuple[int, int, float, int]:
        depth_statistics = self.calc_length_of_leaves()
        depth_statistics = list(map(lambda x: x[0], depth_statistics))

        max_depth = max(depth_statistics)
        min_depth = min(depth_statistics)
        mean_depth = mean(depth_statistics)

        return max_depth, min_depth, mean_depth, self.depth

    def flatten_nodes(self, result=None):
        if result is None:
            result = []
        for child in self.children:
            result = child.flatten_nodes(result)

        result.append(self)

        return result

    def set_root_on_children(self, initial=None):
        if initial is None:
            initial = self

        for child in self.children:
            child.set_root_on_children(initial)

        self.root = initial

    def print_children(self, level: int, children: list, settings: TreeSettings) -> str:
        indentation = " - " * level

        children_str = ""
        if len(children) > 0:
            children_str = "\n"

        data = "| " + indentation
        if settings.print_data:
            if settings.print_data_with_accessing_field:
                data += f" {self.data[settings.accessing_field]}"
            else:
                data += f"{self.data}"

        children = (
            f""
            + children_str
            + "\n".join(
                [
                    child.print_children(level + 1, child.children, settings)
                    for child in children
                ]
            )
        )

        return f"{data}{children}"

    def __str__(self):
        return self.print_children(1, self.children, TreeSettings())

    def __repr__(self):
        return f"{{ {self.uuid} | {len(self.children)} | {self.data} }}"
