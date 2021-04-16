class Stack: 
    def __init__(self):
        self.stack = []
    
    def push(self, num):
        self.stack.append(num)
    
    def pop(self):
        if(self.isEmpty()):
            return False
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True 
        return False 
    
    def size(self):
        return len(self.stack)

def main():
    myStack = Stack()
    myStack.push(42)
    print("Top of the stack:", myStack.top())
    print("Size of stack:", myStack.size())
    popped_value = myStack.pop()
    print("Popped value:", popped_value)
    print("Size of stack:", myStack.size())
    popped_value = myStack.pop()
    print("Popped value:", popped_value)

main()