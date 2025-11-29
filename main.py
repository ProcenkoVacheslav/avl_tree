class _Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None


class AVLTree:
    class __Node:
        def __init__(self, value: int):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1
            self.balance = 0

        def __repr__(self):
            return f'node({self.value})'

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def search(self, value):
        return self.__search(self.root, value)

    @staticmethod
    def __height(node):
        if node is None:
            return 0
        return node.height

    @staticmethod
    def __min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __update_height(self, node):
        if node is not None:
            left_height = self.__height(node.left)
            right_height = self.__height(node.right)
            node.height = max(left_height, right_height) + 1
            node.balance = right_height - left_height

    def __insert(self, node, value):
        if node is None:
            return self.__Node(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)
        elif value > node.value:
            node.right = self.__insert(node.right, value)
        else:
            node.value = value
            return node

        return self.__balance_node(node)

    def __balance_node(self, node):
        self.__update_height(node)

        if node.balance < -1:
            if node.left.balance > 0:
                node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        if node.balance > 1:
            if node.right.balance < 0:
                node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node

    def __rotate_right(self, y):
        x = y.left
        t_2 = x.right

        x.right = y
        y.left = t_2

        self.__update_height(y)
        self.__update_height(x)

        return x

    def __rotate_left(self, x):
        y = x.right
        t_2 = y.left

        y.left = x
        x.right = t_2

        self.__update_height(x)
        self.__update_height(y)

        return y

    def __delete(self, node, value) -> __Node | None:
        if node is None:
            return node

        if value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.__min_value_node(node.right)
            node.value = temp.value
            node.right = self.__delete(node.right, temp.value)

        return self.__balance_node(node)

    def __search(self, node, value) -> __Node | None:
        if node is None or node.value == value:
            return node.value if node else None

        if value < node.value:
            return self.__search(node.left, value)
        return self.__search(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def __str__(self):
        result = self.inorder_traversal()
        return f'avl_tree({result})'


if __name__ == "__main__":
    avl = AVLTree()

    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(50)
    avl.insert(60)
    avl.insert(70)
    avl.insert(80)

    search_node = avl.search(30)

    print(avl)
