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

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,num):
        self.queue.append(num)
    
    def dequeue(self):
        if(self.isEmpty()):
            return False 
        removed = self.queue[0]
        self.queue.remove(removed)
        return removed

    def rear(self):
        return self.queue[-1]
    
    def front(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True 
        return False 
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

    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print("Size of queue:", myQueue.size())
    print("Front of queue:", myQueue.front())
    print("Rear of queue:", myQueue.rear())
    dequeuedItem = myQueue.dequeue()
    print('Dequeue item:', dequeuedItem)

main()