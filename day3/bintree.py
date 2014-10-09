#!/usr/bin/enf python

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_helper(self, val):
        if val < self.val:
            # insert in left subtree
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert_helper(val)
        elif val > self.val:
            # insert in right subtree
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert_helper(val)
        else:
            print 'Value {} already present'.format(val)
            return None

    def search(self, val):
        if self.val == val:
            return True
        if val < self.val:
            return self.left.search(val) if self.left else False
        else:
            return self.right.search(val) if self.right else False

    def inorder_helper(self):
        # Print left subtree
        if self.left:
            self.left.inorder_helper()
        # Print node value
        print self.val,
        if self.right:
            self.right.inorder_helper()

    def height(self):
        lh = self.left.height() if self.left else 0
        rh = self.right.height() if self.right else 0
        return 1 + max(lh, rh)

class BinTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert_helper(val)

    def search(self, val):
        if self.root is None:
            return False
        return self.root.search(val)

    def delete(val):
        pass

    def inorder(self):
        if self.root is None:
            return
        self.root.inorder_helper()

    def height(self):
        if self.root is None:
            return 0
        return self.root.height()

bt = BinTree()
for x in range(0, 30, 3):
    bt.insert(x)

