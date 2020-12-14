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
    right.get_left().insert_left(1)
    return tree
tree = create_a_tree()   #创建一个树


def convert_tree_to_list(tree):
    list1 = []
    if tree == None:
        return 0
    list1.append(tree.get_data())
    if tree.get_left() == None and tree.get_right() == None:
        return tree.get_data()
    if tree.get_left() != None:
        list1.append(convert_tree_to_list(tree.get_left()))
    else:
        list1.append(None)
    if tree.get_right() != None:
        list1.append(convert_tree_to_list(tree.get_right()))
    else:
        list1.append(None)
    return list1
print(convert_tree_to_list(tree))
        


