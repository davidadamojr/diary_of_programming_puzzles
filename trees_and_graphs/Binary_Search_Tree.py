import Queue
class Node:
	def __init__(self,item,left,right):
		self.item=item
		self.left=left
		self.right=right
		self.count=1

class binTree:
		def __init__(self):
			self.root=None
		
		def createBST(self,listi,low,high):
			if low<=high:
				mid=(low+high)/2
				node = Node(listi[mid],None,None)
				node.left = self.createBST(listi,low,mid-1)
				node.right=self.createBST(listi,mid+1,high)
				return node
			else:
				return None

		


		def search(self,key):
			return self.rSearch(self.root,key)


		def rSearch(self,r,key):
			print "called"
			if r != None:
				if r.item==key:
					print "Found"
					return r.item
				else:
					if r.item > key:
						return self.rSearch(r.left,key)
					else:
						return self.rSearch(r.right,key)
			else:
				return None

		def inOrder(self,r):
			if r != None:
				self.inOrder(r.left)
				print r.item
				self.inOrder(r.right)

		def preOrder(self,r):
			if r != None:
				print r.item
				self.inOrder(r.left)
				self.inOrder(r.right)


		def postOrder(self,r):
			if r != None:
				self.inOrder(r.left)
				self.inOrder(r.right)
				print r.item

		def insert(self,item):
			self.rInsert(self.root,item)	



		def rInsert(self,r,item):
			if r == None:
				node = Node(item,None,None)
				r=node
			elif item==r.item:
				r.count+=1
			elif item<r.item:
				r.left=self.rInsert(r.left,item)
			else:
				r.right=self.rInsert(r.right,item)
			return r

		def removeNode(self,r):
		    toRemove = r
		    if r == None:  
		         return None
		    elif r.right == None:
		         r = r.left
		    elif r.left == None:
		          r = r.right
		    else: 
		          parent = r
		          toRemove = r.left
		          while toRemove.right !=  None:
		                parent = toRemove
		                toRemove = toRemove.right
		          r.item = toRemove.item
		          if parent == r:
		               parent.left = toRemove.left
		          else:
		               parent.right = toRemove.left
		    return r

		def remove(self,key):
			self.root = self.rRemove(self.root,key)
 
		def rRemove(self, r, key):
			if r == None or r.item == key:
				return self.removeNode(r)
			elif r.item > key:
				r.left = self.rRemove(r.left,key)
			else:
				r.right =  self.rRemove(r.right,key)
			return r




#bst=binTree()
#bst.root=bst.createBST([1,2,3,5,6,7,8],0,6)
#bst.inOrder(bst.root)
#bst.search(4)
#k=bst.remove(5)
#bst.inOrder(bst.root)



				
