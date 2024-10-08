# 1) Queue implementation using a list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements:", queue)


# 2) Using collections.deque
from collections import deque

# Queue implementation using deque
queue = deque()

# Enqueue operation
queue.append(1)
queue.append(2)
queue.append(3)

print("\n\nQueue after enqueue operations:", queue)

# Dequeue operation
first_element = queue.popleft()
print("Dequeued element:", first_element)
print("Queue after dequeue operation:", queue)



# 3) Using queue.Queue
from queue import Queue

# Create a queue
queue = Queue()

# Enqueue operation
queue.put(1)
queue.put(2)
queue.put(3)

print("\n\nQueue size after enqueue operations:", queue.qsize())

# Dequeue operation
first_element = queue.get()
print("Dequeued element:", first_element)
print("Queue size after dequeue operation:", queue.qsize())

