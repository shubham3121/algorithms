class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return self.val

    def __repr__(self):
        return self.__str__()


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

    def maximum(self, node):
        """
        Given a node, find the maximum value in the subtree of that node.
        Time complexity: O(h), h is the height of the tree.
        """
        if not node:
            return node

        root = node
        while root.right:
            root = root.right
        return root

    def minimum(self, node):
        """
        Given a node, finds the minimum value in the subtree of the node.
        Time complexity:  O(h), h is the height of the tree.
        """
        if not node:
            return node

        root = node
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

    def _transplant(self, node, subnode):

        if not node.parent:
            self.root = subnode

        parent = node.parent
        if parent.left == node:
            parent.left = subnode
        else:
            parent.right = subnode
        if subnode and not subnode.parent:
            subnode.parent = parent

    def delete(self, node):
        """
        Given a node, deletes a node from the subtree.
        Time complexity: O(h), h is the height of the tree.
        """
        if not node.left and not node.right:
            self._transplant(node=node, subnode=None)
        elif not node.left:
            self._transplant(node=node, subnode=node.right)
        elif not node.right:
            self._transplant(node=node, subnode=node.left)
        else:
            subnode = self.minimum(node=node.right)
            if not subnode.parent == node:
                self._transplant(node=subnode, subnode=subnode.right)
                subnode.right = node.right
                subnode.right.parent = subnode

            self._transplant(node=node, subnode=subnode)
            subnode.left = node.left
            subnode.left.parent = subnode
