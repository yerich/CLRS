import sys

class Stack:
	data = []
	length = 0
	
	def __len__(self):
		return len(self.data)
	
	def push(self, v):
		if(len(self.data) < self.length +1):
			self.data.append(0)
		self.data[self.length] = v
		self.length += 1
	
	def pop(self, v):
		if(self.length == 0):
			print >> sys.stderr, "Error: stack underflow"
			return
		self.length -= 1
		return self.data[self.length-1]