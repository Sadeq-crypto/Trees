class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,root,name=''):
        self.root = root
        self.name = name

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(3)
node.left.right = Node(7)
node.right.left = Node(13)
node.right.right = Node(17)

my_tree = Tree(node, 'Sadeq\'s Tree')

print(my_tree.name)
print(my_tree.root.left.data)
print(my_tree.root.right.right.data)
