class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Insert a value in the binary tree. If the val is less than value of node,
        then check for insertion on left child else check for insertion
        on right child of the node.

        Time complexity: O(h), h is the height of the tree.
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
        """
        Traversal: L -> P -> R
        """
        if root:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)

    def _preorder(self, root):
        """
        Traversal: P -> L -> R
        """
        if root:
            print(root.val)
            self._preorder(root.left)
            self._preorder(root.right)

    def _postorder(self, root):
        """
        Traversal: L -> R -> P
        """
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val)

    def traversal(self, order_type="in"):
        """
        Print the binary tree, based on the type of traversal.
        All traversals have time complexity of O(n).
        """
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

    def find(self, key):
        """
        Give a key (value), finds the value in the tree.
        Time Complexity: O(h), h is height of the tree.
        """
        root = self.root
        while root:
            if root.val == key:
                break
            elif root.val < key:
                root = root.left
            else:
                root = root.right
        return root

    def maximum(self, node=None):
        """
        Given a node, find the maximum value in the subtree of that node.
        If node is not provided, then returns the maximum value in the binary tree.
        Time complexity: O(h), h is the height of the tree.
        """
        if node:
            root = node
        else:
            root = self.root
        while root.right:
            root = root.right
        return root

    def minimum(self, node=None):
        """
        Given a node, finds the minimum value in the subtree of the node.
        If the node is not provided, then returns the minimum value of the binary tree.
        Time complexity:  O(h), h is the height of the tree.
        """
        if node:
            root = node
        else:
            root = self.root
        while root.left:
            root = root.left
        return root

    def successor(self, key):
        """
        Finds the node with the value equal to key.
        If right node exists, then find the left-most node in the right sub-tree.
        Else, find the nearest ancestor (parent) whose left child is also an
        ancestor of the node.
        Time complexity: O(h), h is the height of the tree.
        """

        node = self.find(key=key)

        if node.right:
            return self.minimum(node=node.right)
        parent = node.parent
        while parent and parent.right == node:
            node = parent
            parent = parent.parent
        return parent

    def predecessor(self, key):
        """
        Finds the node with the value equal to key.
        If left node exists, then find the right-most node in the left-subtree.
        Else, find the nearest ancestor (parent) whose right child is also an
        ancestor of the code.
        Time complexity: O(h), h is the height of the tree.
        """

        node = self.find(key=key)

        if node.left:
            return self.maximum(node=node.left)
        parent = node.parent
        while parent and parent.left == node:
            node = parent
            parent = parent.parent
        return parent
