class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.value}"

    def add(self, value):
        if self.value == value:
            return
        if self.value > value:
            # Left
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            # Right
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = Node(value)

node_1 = Node(4)
node_1.add(2)
node_1.add(3)
node_1.add(6)
node_1.add(7)
node_1.add(5)
node_1.add(1)
node_1.add(5)
pass







