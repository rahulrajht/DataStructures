class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,inItem):
        return self.items.append(inItem)

    def pop(self):
        try:
            return self.items.pop()     #self.items[len(self.items)-1]
        except:
            print('Stack is Empty')
            
    def peek(self):
        try:
            return self.items[len(self.items)-1]
        except:
            return 'Stack is Empty'

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print(s.peek())
s.pop()
s.pop()
s.pop()
