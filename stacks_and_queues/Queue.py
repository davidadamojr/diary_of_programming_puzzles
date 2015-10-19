#Authored By:- Nishant Shreshth


class Queue:
	#Initializing Queue
	def __init__(self):
		self.items = []

	#Checking whether Queue is empty or Not returns Boolean
	def is_empty(self):
		return self.items == []

	#Adds an element to the queue.
	def enqueue(self, item):
		self.items.insert(0,item)

	#Removes the first element from the Queue.	
	def dequeue(self):
		return self.items.pop()

	#Determines The Size Of Queue
	def size(self):
		return len(self.items)
