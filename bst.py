class node1(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary(object):
    def __init__(self):
        self.root=None
    def ins(self,data):
        if not self.root:
            self.root=node1(data)
        else:
            self.insertN(data,self.root)
            
    def insertN(self,data,node):
        if data<node.data:
            if node.left:
                self.insertN(data,node.left)
            else:
                node.left=node1(data)
        else:
            if node.right:
                self.insertN(data,node.right)
            else:
                node.right=node1(data)

    def traverse(self):
        if self.root:
            self.trav(self.root)
        
    def trav(self,cnode):
        if cnode.left:
            self.trav(cnode.left)
        print(cnode.data)
        if cnode.right:
            self.trav(cnode.right)


b=Binary()
b.ins(12)
b.ins(10)
b.ins(11)
b.ins(9)
b.ins(14)
b.traverse()
            
    
            
        
