class stack:
    def _init_(self):
        self.sack=[""]
    def push(self,data):
        self.sack.append(data)
    def pop(self):
        del self.sack[-1]
    def peek(self):
        return self.sack[-1]       
    def sizesack(self):
        return len(self.sack)
    
    
obj = stack()
obj.push(12)
obj.push(13)
obj.push(15)
obj.pop()
obj.peek()
print(obj.sack)