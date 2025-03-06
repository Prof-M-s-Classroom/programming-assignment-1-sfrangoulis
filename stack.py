class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None
        pass

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.top = None
        self.rear = None
        self.size = 0

        pass

    def push(self, temperature, humidity):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_node = Node((temperature, humidity))
        if self.size == 0:
            self.top = new_node
            self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            self.rear.next = self.top


        if self.size < self.MAX_SIZE:
            self.size+=1
        else:
            temp = self.top
            while temp.next != self.rear:
                temp = temp.next
            temp.next = self.top
            self.rear = temp

        pass

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.is_empty():
            raise Exception("Stack Undeflow")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.size -= 1

        return temp.data
        pass

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.top.data
        pass

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.is_empty():
            raise Exception("Stack Undeflow")
        temp = self.top
        for i in range(self.size):
            print(temp.data)
            temp = temp.next
        pass

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0
        pass

