import collections

dq = collections.deque(['red','pink'])

# adding blue on left
dq.appendleft('blue')
print("Appending blue to the left: ", list(dq))

# adding green on right 
dq.append('green')
print("Appending green to the right: ", list(dq))

# adding two colors white and gray on right
dq.extend(['white', 'gray'])
print("Appending  white and gray to the right: ", list(dq))

# adding two colors black  and voilet on left:
dq.extendleft(['black','voilet'])
print("Appending black and voilet to the left: ", list(dq))

# Inserting golden at index 2
dq.insert(2,'golden')
print("Inserting golden at index 2: ", list(dq))

# To Pop colors from the right end:
dq.pop()
print("Removing colors from the right: ", list(dq))

# To Pop element from the left end:
dq.popleft()
print("Removing colors from the left: ", list(dq))

# Removing golden from the queue
dq.remove('golden')
print("Removing golden from the queue :", list(dq))
