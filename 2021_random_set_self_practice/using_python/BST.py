class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if self.value <= node.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        elif self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

    def print_nodes_inorder(self):
        root = self.value
        left_node = self.left
        right_node = self.right

        if left_node is not None:
            left_node.print_nodes_inorder()
        print(root, end=' ')
        if right_node is not None:
            right_node.print_nodes_inorder()

    def insert_many(self, nodes):
        for node in nodes:
            self.insert(Node(node))


if __name__ == "__main__":
    #     node2 = Node(2)
    #     node1 = Node(1)
    #     node3 = Node(3)
    #     node2.insert(node1)
    #     node2.insert(node3)

    #     node4 = Node(4)
    #     node4.insert(node2)
    """
        4
      2
    1   3

    """
    #     print(node2.right.value) # 3
    #     print(node2.left.value) # 1

    node4 = Node(4)
    node4.insert_many([2, 1, 2, 3, 2])
    node4.print_nodes_inorder()
