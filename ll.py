class node(object):
    def __init__(self,data):
        self.data=data;
        self.nextN=None;
    
class LinkList(object):
    
    def __init__(self):
        self.head=None;
        self.size=0;
        
    def insertStart(self,data):
        self.size=self.size+1;
        newN=node(data);
        
        if not self.head:
            self.head=newN;
            
        else:
            newN.nextN=self.head;
            self.head=newN;
            
    def traverse(self):
        cNode=self.head;
        while cNode is not None:
            print(cNode)
            cNode=cNode.nextN;
    def size1(self):
        return self.size;
        


ll=LinkList()
ll.insertStart(14)
ll.insertStart(141)
ll.traverse()
ll.size1()
