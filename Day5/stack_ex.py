class StackExample:
    def __init__(self):#unparameterized constructor
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
        
    def is_empty(self):
        return self.stack==[]

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print('stack underflow')


    def display(self):
        if not self.is_empty():
            for top in range(len(self.stack)-1,-1,-1):
                print(self.stack[top])
        else:
                print('stack is empty')
    
    def peek(self):
        if not self.is_empty():
            print('the peek value:',self.stack[-1])
        else:
            print('stack is empty')



obj=StackExample()
obj.push(10)
obj.push(20)
obj.push('niha')
obj.push(40)
obj.peek()
obj.display()


