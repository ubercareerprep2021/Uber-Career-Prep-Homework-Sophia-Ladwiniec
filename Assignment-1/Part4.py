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
    
    def pop(self):
        if self.size > 0: 
            current = self.head 
            index = 0
            while(index != self.size):
                if(index == self.size - 2):
                    rv = current.next.data 
                    current.next = None 
                    self.size-=1 
                    return rv 
                current = current.next 
                index += 1

    def remove(self, index):
        if(index == 0):
            self.head = self.head.next
            self.size-=1
            return 
        if (index < self.size):
            current = self.head 
            count = 0 
            while(current != None):
                if (index-1 == count):
                    current.next = current.next.next 
                    return 
                current = current.next 
                count+=1 

    
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

    def elementAt(self, index):
        current = self.head 
        count = 0 
        while(current!= None):
            if(count == index):
                return current
            current = current.next 
            count+=1 
        return None
def main():
    n1 = Node(7) 
    n2 = Node(8)
    n3 = Node(9)
    n4 = Node(10)
    n5 = Node(5)

    l1 = LinkedList()
    print("INSERTING ELEMENT AT POSITION 0:")
    l1.insert(0,n1)
    print(l1.printList())
    print("INSERTING ELEMENT AT POSITION 1:")
    l1.insert(1,n2)
    print(l1.printList())
    print("INSERTING ELEMENT AT POSITION 2:")
    l1.insert(2, n3)
    print(l1.printList())
    print("INSERTING ELEMENT AT POSITION 2:")
    l1.insert(2, n4)
    print(l1.printList())
    print("INSERTING ELEMENT AT POSITION 0:")
    l1.insert(0, n5)
    print(l1.printList())
    print("CURRENT SIZE OF LIST: "+ str(l1.get_size()))
    print("POPPING ITEM FROM LINKEDLIST: " + str(l1.pop()))
    print("CURRENT SIZE OF LIST: " + str(l1.get_size()))
    print("REMOVE ITEM AT POSITION 0")
    l1.remove(0)
    print(l1.printList())
    print("REMOVE ITEM AT POSITION 1")
    l1.remove(1)
    print(l1.printList())
    print("REMOVE ITEM AT POSITION 5:")
    l1.remove(5)
    print(l1.printList())
    print("GET ELEMENT AT POSITION 0:")
    n7 = l1.elementAt(0)
    print("ELEMENT'S DATA: "+ str(n7.data))
    print("GET ELEMENT AT POSITION 4:")
    n7 = l1.elementAt(4)
    if(n7 != None):
        print("ELEMENT'S DATA: "+ str(n7.data))
    else:
        print(n7)


main()

                    
