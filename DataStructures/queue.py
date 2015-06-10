# Standard lists do not perform very well for queueing operations (shifting items)

from collections import deque

queue = deque([1, 2, 3, 4, 5])
print queue

queue.append(6)
queue.append(7)
print queue

i1 = queue.popleft()
i2 = queue.popleft()
print queue, i1, i2
