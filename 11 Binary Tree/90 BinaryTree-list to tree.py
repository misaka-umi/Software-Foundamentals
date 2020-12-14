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
    tree.insert_right(3)
    right = tree.get_right()
    left = tree.get_left()
    left.insert_right(8)
    left.insert_left(9)
    right.insert_right(1)
    right.insert_left(13)
    return tree
tree = create_a_tree()   #创建一个树
def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

def create_tree_from_nested_list(list1):
    def insert(tree,list1):
        if list1[1] != None:
            tree.insert_left(list1[1][0])
            insert(tree.get_left(),list1[1])
        if list1[2] != None:
            tree.insert_right(list1[2][0])
            insert(tree.get_right(),list1[2])
    tree = BinaryTree(list1[0])
    insert(tree,list1)
    return tree
t = create_tree_from_nested_list([10, [5, None, None], [15, [11, None, None], [22, None, None]]])
print_tree(t, 0)
