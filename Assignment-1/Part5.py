class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    

class LinkedList: 
    def __init__(self):
        self.head = None 
        self.size = 0 
    
    def get_size(self):
        return str(self.size)
    
    def reverse(self):
        prev = None 
        current = self.head
        while(current != None):
            next_node = current.next 
            current.next = prev
            prev = current 
            current = next_node 
        self.head = prev 

    def insert(self, index, node):
        if(index == 0):
            current = self.head 
            self.head = node 
            node.next = current
            self.size += 1
            return 

        if(index <= self.size):
            # wants to add at the head
            current = self.head 
            count = 0
            while(current != None):
                if(count == index -1):
                    node2 = current.next 
                    current.next = node 
                    node.next = node2 
                    self.size+=1 
                    return 
                current = current.next
                count+=1 
    
    def printList(self):
        return_string = ""
        current = self.head 
        while(current != None):
            return_string += str(current.data) + " -> "
            current = current.next
        return return_string

def main():
    n1 = Node(7) 
    n2 = Node(8)
    n3 = Node(9)
    n4 = Node(10)
    n5 = Node(5)

    l1 = LinkedList()
    l1.insert(0,n1)
    l1.insert(1,n2)
    l1.insert(2, n3)
    l1.insert(2, n4)
    l1.insert(0, n5)
    print("BEFORE REVERSING")
    print(l1.printList())
    l1.reverse()
    print("AFTER REVERSING")
    print(l1.printList())
    


main()
