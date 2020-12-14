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

def basic_print(tree): #pre-order
    if tree != None:
        print(tree.get_data())
        basic_print(tree.get_left())
        basic_print(tree.get_right())
    '''
    in-order
    def basic_print(tree):
        if tree != None:
            basic_print(tree.get_left())
            print(tree.get_data())
            basic_print(tree.get_right())
    post-order
    def basic_print(tree):
        if tree != None:
            basic_print(tree.get_left())
            basic_print(tree.get_right())
            print(tree.get_data())
    '''
def convert_tree_to_list(tree):
    if tree == None:
        return None
    else:
        result = []
        result.append(str(tree.get_data()))
        result.append(convert_tree_to_list(tree.get_left()))
        result.append(convert_tree_to_list(tree.get_right()))
        return result
def sum_tree(tree):
    if tree == None:
        return 0
    else:
        sum = tree.get_data()
        sum += sum_tree(tree.get_left())
        sum += sum_tree(tree.get_right())
        return sum
def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)
def create_a_tree():
    tree = BinaryTree(9)
    tree.insert_left(3)
    tree.get_left().insert_right(7)
    tree.insert_right(6)
    tree.get_right().insert_right(2)
    return tree
b_tree = create_a_tree()
print_tree(b_tree, 0)
