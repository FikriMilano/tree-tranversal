class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_node(self, value):
        if value < self.value:
            self.left = Node(value)
        else:
            self.right = Node(value)


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def pre_order(self, root):
        if root is None:
            return

        print(root.value, end=" ")

        self.pre_order(root.left)

        self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)

        print(root.value, end=" ")

        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return

        self.post_order(root.left)

        self.post_order(root.right)

        print(root.value, end=" ")


tree1 = Tree("Retno")
tree1.root.insert_node("Bramantyo")
tree1.root.insert_node("Subagyo")

tree1.pre_order(tree1.root)
print("\n")
tree1.in_order(tree1.root)
print("\n")
tree1.post_order(tree1.root)
