class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Traversing the doubly linked list:")
dll.traverse()
