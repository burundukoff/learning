class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None  #корень

    def newNode(self, data):            #добавление узла в дерево
        return Node(data,None,None)
    

tree = Node(4)  #создали вершину с 1
tree.left = Node(2)  #создали слева вершину с 
tree.left.left = Node(1)  # еще ниже с 1
tree.left.right =Node(3) 
tree.right = Node(7)

