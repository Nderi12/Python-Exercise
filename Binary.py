class node:
	def _init_(self,vaue=None):
		self.value=value
		self.left_child=None
		self.right_child=None

class binary_search_tree:
	def _init_(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=node(value)

			elif value>cur_node.value:
				if cur_node.right_child==None:
					cur_node.right_child=node(value)
				else:
					self._insert(value,cur_node.right_child)
                else:
                    print "Value already exists in tree!"
    
    def _print_tree(self,cur_node)
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree (self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print str(cur_node)
            self._print_tree(cur_node.right_child)

	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
	else:
		return 0

	def height(self, cur_elem, cur_height):
		if cur_node==None: return cur_height
			left_height=self._height(cur_node.left_child,cur_height+1)
			right_child=self._height(cur_node.right_child,cur_height+1)
			return max(left_height,right_height)

	def search(self,value):
		if self.root!=None:
			return self.__search(value,self.root)
		else:
			return False

	def __search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None
			return self.__search(value,cur_node.left_child)
		elif value<cur_node.value and cur_node.right_child!=None
			return self.__search(value,cur_node.right_child)

    def fill_tree(tree,num_elems=100,max_int=1000):
        from random import randint
        for _ in range(num_elems):
            cur_elem = randint(0,max_int)
            tree.insert(cur_elem)
        return tree

tree = binary_search_tree()

tree.insert(7)
tree.insert(15)
tree.insert(20)
tree.insert(25)
tree.insert(18)
tree.insert(2)
tree.insert(0)

tree._print_tree()

print "Tree height is: "+str(tree.height())

print tree.search(15)
print tree.search(13)