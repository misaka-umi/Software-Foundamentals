class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            subtree = BinaryTree(new_data, left=self.__left)
            self.__left = subtree
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            subtree = BinaryTree(new_data, right=self.__right)
            self.__right = subtree
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

def get_height(tree):
    if tree == None:
        return 0
    if tree.get_left() != None:
        return 1 + get_height(tree.get_left())
    if tree.get_right() != None:
        return 1 + get_height(tree.get_right())
    return 1 + max(get_height(tree.get_left()), get_height(tree.get_right()))
def create_a_tree():
    tree = BinaryTree(9)
    tree.insert_left(3)
    tree.insert_right(6)
    right = tree.get_right()
    left = tree.get_left()
    left.insert_right(7)
    right.insert_right(2)
    return tree
b_tree = create_a_tree()
print(get_height(b_tree))


    
