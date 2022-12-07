Gend=-1 #global end

class Node:

    def __init__(self, flag):
        self.start=None
        self.end=None
        self.children={} #use a dic to store the tree structure
        self.suffixlink=None
        self.isleaf=flag
        self.suffixindex=None


