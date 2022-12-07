Gend=-1 #global end
import time
def time_dec(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res =  func(*args, **kwargs)
        end_time = time.time()
        result = end_time - start_time
        print('Execution time is %.3fs' %result)
        return res
    return inner
class Node:

    def __init__(self,isleaf):
        self.start=None
        self.end=None
        self.children={} #use a dic to store the tree structure
        self.isleaf=isleaf
        self.suffixlink=None
        self.suffixindex=None

    def __getattribute__(self, name):
        if name == 'end':
            if self.isleaf:
                return Gend
        return super(Node, self).__getattribute__(name)


class Suffixtree:

    def __init__(self, input):
        self.string=input
        self.activenode=None
        self.activeedge=-1
        self.activelength=0
        self.remainingcount=0
        self.rootend=None
        self.breakend=None #store the breaked internal node end
        self.size=-1
        self.root=None
        self.suffixlist=[]

    def edge_length(self,node):
        return node.end-node.start

    def walk_down(self, index):
        node = self.selectnode()
        length=self.edge_length(node)
        if(self.activelength>length):
            self.activelength-=length
            self.activeedge=node.children[self.string[index]].start
            self.activenode=node
        else:
            self.activelength+=1

    def creat_node(self, start, end, isleaf=False):
        node = Node(isleaf)
        node.suffixlink=self.root
        node.start=start
        node.end=end
        return node

    def selectnode(self):
        return self.activenode.children.get(self.string[self.activeedge])

    def getnextchar(self,pos):
        nextnode = self.selectnode()
        if (self.edge_length(nextnode)>=self.activelength):
            return self.string[nextnode.start+self.activelength]
        if (self.edge_length(nextnode)+1==self.activelength):
            if(nextnode.children[self.string[pos]] is not None):
                return self.string[pos]
        else:
            self.activenode=nextnode
            self.activelength=self.activelength-self.edge_length(nextnode)-1
            self.activeedge=self.activeedge+self.edge_length(nextnode)+1
            return self.getnextchar(pos)


    def startphase(self,pos):
        global Gend
        lastCreatedInternalNode=None
        Gend+=1
        self.remainingcount+=1
        while(self.remainingcount>0):
            if(self.activelength == 0):
                if(self.activenode.children.get(self.string[pos]) is not None):
                    self.activeedge = self.activenode.children.get(self.string[pos]).start
                    self.activelength+=1
                    break
                else:
                    self.activenode.children[self.string[pos]]=self.creat_node(pos, Gend, isleaf=True)
                    self.remainingcount-=1
            else:
                try:
                    nextchar = self.getnextchar(pos)
                    if (nextchar == self.string[pos]):
                        if (lastCreatedInternalNode is not None):
                            lastCreatedInternalNode.suffixlink = self.selectnode()
                        self.walk_down(pos)
                        break
                    else:
                        node = self.selectnode()
                        self.breakend = node.start + self.activelength - 1
                        new_internalnode = self.creat_node(node.start, self.breakend)
                        self.activenode.children[self.string[self.activeedge]] = new_internalnode
                        new_internalnode.children[self.string[pos]] = self.creat_node(pos, Gend,isleaf=True) #it is the string[pos]
                        node.start += self.activelength
                        new_internalnode.children[self.string[node.start]] = node
                        if (lastCreatedInternalNode is not None):
                            lastCreatedInternalNode.suffixlink = new_internalnode
                        lastCreatedInternalNode = new_internalnode
                        new_internalnode.suffixlink = self.root
                        if (self.activenode != self.root):
                            self.activenode = self.activenode.suffixlink
                        else:
                            self.activeedge += 1
                            self.activelength -= 1
                        self.remainingcount -= 1
                except:
                    node=self.selectnode()
                    node.children[self.string[pos]]=self.creat_node(pos,Gend,isleaf=True)
                    if (lastCreatedInternalNode is not None):
                        lastCreatedInternalNode.suffixlink=node
                    lastCreatedInternalNode = node
                    if(self.activenode!=self.root):
                        self.activenode=self.activenode.suffixlink
                    else:
                        self.activeedge += 1
                        self.activelength -= 1
                    self.remainingcount -= 1
    @time_dec
    def build_suffixtree(self):

        self.root=self.creat_node(-1,-1)
        self.activenode=self.root
        for i in range(len(self.string)):
            self.startphase(i)


    def walk_dfs(self, current,sub):
        if (len(current.children)==0):
            start, end = current.start, current.end
            sub +=self.string[start: end + 1]
            self.suffixlist.append(sub)
            print(sub)
        else:
            start, end = current.start, current.end
            sub +=self.string[start: end + 1]
            for key, node in current.children.items():
                self.walk_dfs(node,sub)


    def print_dfs(self):
        self.walk_dfs(self.root,"")
        return self.suffixlist
















