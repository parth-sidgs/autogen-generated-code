"""
Implementation of a stack data structure using a linked list.

This implementation provides the following functionalities:
- push(data): Adds an element to the top of the stack.
- pop(): Removes and returns the element at the top of the stack.
- peek(): Returns the element at the top of the stack without removing it.
- is_empty(): Checks if the stack is empty.
- size(): Returns the number of elements in the stack.

"""

class Node:
    """Represents a node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Represents a stack implemented using a linked list."""

    def __init__(self):
        self._head = None  # Top of the stack
        self._size = 0

    def push(self, data):
        """Adds an element to the top of the stack."""
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        """Removes and returns the element at the top of the stack."""
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack.")  # Explicit exception for clarity
        popped_data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return popped_data

    def peek(self):
        """Returns the element at the top of the stack without removing it."""
        if self.is_empty():
            raise Exception("Cannot peek into an empty stack.")  # Explicit exception for clarity
        return self._head.data

    def is_empty(self):
        """Checks if the stack is empty."""
        return self._head is None


    def size(self):
        """Returns the number of elements in the stack."""
        return self._size

    def __str__(self):  # Added for easy printing/debugging
        """String representation of the stack."""
        if self.is_empty():
            return "Stack is empty"
        nodes = []
        current = self._head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)


# Example Usage:

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)  # Output: 30 -> 20 -> 10
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
stack.pop()
stack.pop()
print(stack.is_empty()) # Output: True

