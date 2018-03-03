class Node:
    def __init__(self, data, parent=None):
        '''
        nodeType indicates if it is a 2 node, a 3 node, or a 4 node
        d1, d2, d3 are the data from left to right
        c1, c2, c3, c4 are the children, from left to right
        '''
        # make sure that if c2 is None, so is c3 and c4. And if c3 is None, so is c4. We shall follow this convention for uniformity
        self.nodeType = 2
        self.d1, self.d2, self.d3 = data, None, None
        self.c1, self.c2, self.c3, self.c4 = None, None, None, None
        self.parent = parent
    def push(self, data):
        '''
        this function adds the new data (and rearranges the inner arrangement of the node)
        '''
        if self.nodeType == 2:
            self.nodeType = 3
            self.d1, self.d2 = sorted([self.d1, data])
        elif self.nodeType == 3:
            self.nodeType = 4
            self.d1, self.d2, self.d3 = sorted([self.d1, self.d2, data])
    def split(self):
        '''
        Calling this function on a 4-node splits up the 4-node appropriately
        It also should split up 4-nodes in the path from this node upwards to the parent in case any were created
        '''
        # Case O, if there is nothing to do
        if self.nodeType < 4:
            ...
        # Case I, splitting when there is no parent
        if self.parent == None:
            ...
        # Case II, when parent is a 2-node
        elif self.parent.nodeType == 2:
            # subcase a: when the current node is the left child of the parent node
            if self == self.parent.c1:
                ...
            # subcase b: when the current node is the right child of the parent node
            elif self == self.parent.c2:
                ...
        # Case III, when parent is a 3-node
        elif self.parent.nodeType == 3:
            # subcase a: when the current node is the left child of the parent node
            if self == self.parent.c1:
                ...
            # subcase b: when the current node is the middle child of the parent node
            elif self == self.parent.c2:
                ...
            # subcase c: when the current node is the right node of the parent node
            elif self == self.parent.c3:
                ...
            # now recursively split the parent
            self.parent.split()
    def insert(self, data):
        '''
        insert a given data in the subtree rooted at this node
        '''
        # if this node is a leaf
        if self.c1 == None:
            # call self.push(data)
            # and then self.split()
            ...
        # if this node is not a leaf, and a 2-node
        elif self.nodeType == 2:
            if data < self.d1:
                # call this function recursively on the left subtree
                ...
            else:
                # call this function recursively on the right subtree
                ...
        # if this node is a 3-node
        elif self.nodeType == 3:
            if data < self.d1:
                # call this function recursively on the left subtree
                ...
            elif data > self.d2:
                # call this function recursively on the right subtree
                ...
            else:
                # call this function recursively on the middle subtree
                ...
    def search(self, data):
        '''
        find out if a given data in the subtree is in the tree rooted at this node
        returns True or False
        '''
        # if the current node contains the data
        if data in [self.d1, self.d2]:
            ...
        # if this node is a leaf
        elif self.c1 == None:
            ...
        # if this node is not a leaf, and a 2-node
        elif self.nodeType == 2:
            if data < self.d1:
                ...
            else:
                ...
        # if this node is a 3-node
        elif self.nodeType == 3:
            if data < self.d1:
                ...
            elif data > self.d2:
                ...
            else:
                ...

class TwoThreeTree:
    def __init__(self):
        self.isEmpty = True
        self.root = None
    def insert(self, data):
        if self.isEmpty:
            self.isEmpty = False
            self.root = Node(data)
        else:
            self.root.insert(data)
    def search(self, data):
        if self.isEmpty:
            return False
        else:
            self.root.search(data)
