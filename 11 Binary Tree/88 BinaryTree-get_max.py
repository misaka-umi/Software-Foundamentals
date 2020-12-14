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

def create_a_tree():
    tree = BinaryTree(2)
    tree.insert_left(6)
    tree.insert_right(100)
    right = tree.get_right()
    left = tree.get_left()
    left.insert_right(8)
    right.insert_right(1)
    return tree
tree = create_a_tree()   #创建一个树


def get_max(tree, is_integer):
    if tree == None:
        return -9999
    if is_integer:
        max_number = tree.get_data()
        if tree.get_left()!=None:
            if get_max(tree.get_left(),is_integer) > max_number:
                max_number = get_max(tree.get_left(),is_integer)
        if tree.get_right()!=None:
            if get_max(tree.get_right(),is_integer) > max_number:
                max_number = get_max(tree.get_right(),is_integer)
        return max_number
    else:
        max_number = tree.get_data()
        if tree.get_left()!=None:
            if get_max(tree.get_left(),is_integer) > ord(max_number):
                max_number = get_max(tree.get_left(),is_integer)
        if tree.get_right()!=None:
            if get_max(tree.get_right(),is_integer) > ord(max_number):
                max_number = get_max(tree.get_right(),is_integer)
        return max_number
print(get_max(tree,1))
