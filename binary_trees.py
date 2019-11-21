class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Insert a value in the binary tree. If the val is less than value of node,
        then check for insertion on left child else check for insertion
        on right child of the node.
        """

        node = self.root

        if node is None:
            self.root = Node(val=val)
            return

        while 1:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(val=val)
                    node.right.parent = node
                    break
            elif node.val >= val:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(val=val)
                    node.left.parent = node
                    break

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)

    def _preorder(self, root):
        if root:
            print(root.val)
            self._preorder(root.left)
            self._preorder(root.right)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val)

    def traversal(self, order_type="in"):
        root = self.root

        if order_type == "in":
            self._inorder(root=root)
        elif order_type == "pre":
            self._preorder(root=root)
        elif order_type == "post":
            self._postorder(root=root)
        else:
            print(
                "Invalid traversal type. Available types:  'in', 'post' or 'pre'"
            )
