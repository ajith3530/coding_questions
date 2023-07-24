class Binary_Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.value}"

# Create a binary tree structure
"""
           5
        /    \
       4      6
      / \    / \
     2   3  7   8
    /            \
   1              9
       
"""
node_1 = Binary_Tree(1)
node_2 = Binary_Tree(2)
node_3 = Binary_Tree(3)
node_4 = Binary_Tree(4)
node_5 = Binary_Tree(5)
node_6 = Binary_Tree(6)
node_7 = Binary_Tree(7)
node_8 = Binary_Tree(8)
node_9 = Binary_Tree(9)
node_10 = Binary_Tree(10)
node_11 = Binary_Tree(11)
node_12 = Binary_Tree(12)
node_13 = Binary_Tree(13)

node_2.left, node_2.right = node_1, node_11
node_3.left, node_3.right = node_12, node_13
node_4.left, node_4.right = node_2, node_3
node_5.left, node_5.right = node_4, node_6
node_6.left, node_6.right = node_7, node_8
node_8.right, node_8.left = node_9, node_10

root = node_5

def breath_first_search(root_node):
    head = root_node
    stack = [head]
    search_pattern = []

    while len(stack) != 0:
        current_node = stack.pop()
        for node in [current_node.left, current_node.right]:
            if node is not None:
                stack.insert(0, node)
        search_pattern.append(current_node.value)
    return search_pattern

def depth_first_search(root_node, search_pattern=[]):

    # Unnecessary dictionary structure
    visited_lookup = dict()
    if root_node is None or visited_lookup.get(root_node.value) is True:
        return
    # Mark the node
    visited_lookup[root_node.value] = True
    search_pattern.append(root_node.value)
    # Search both the right and left sections recursively
    depth_first_search(root_node.left)
    depth_first_search(root_node.right)
    return search_pattern

print(breath_first_search(root_node=root))
print(depth_first_search(root_node=root))
pass