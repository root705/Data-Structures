class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Stack is empty

    def size(self):
        return len(self.items)

# Example usage of the Stack class
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Size:", stack.size())
print("Top element:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Stack after popping:", stack.items)
print("Is the stack empty?", stack.is_empty())
