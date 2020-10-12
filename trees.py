class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert Node - inserts left to right, top to bottom in data value order
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left == None:
                    # if no left node then create one
                    self.left = Node(data)
                else:
                    # if there is a left node, then recursive insert call
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    # if no right node then create one
                    self.right = Node(data)
                else:
                    # if there is a right node, then recursive insert call
                    self.right.insert(data)
            # apparently no duplicates in this tree. must be a binary search tree
        else:
            self.data = data

    def findval(self, value):
        if value < self.data:
            if self.left == None:
                return str(value) + " Not Found"
            return self.left.findval(value) # recursive
        elif value > self.data:
            if self.right == None:
                return str(value) + " Not Found"
            return self.right.findval(value) # recursive
        else:
            print(str(value) + " is found")

# Print Tree
    def printTree(self):

        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
# Calculate Height of the Tree
def height(root):
    if root == None:
        return -1

    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    return max(left_height, right_height)

# Print Level Order Tree Traversal
def levelOrder(root):

    if root == None:
        print("empty tree")
        return
    if root.left == None and root.right == None:
        print(root.info)
        return

    queue = []
    queue.append(root)
    
    while (len(queue)>0):
        curr = queue.pop(0)
        print(curr.data)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.insert(1)
# root.insert(10)
# root.insert(11)
# root.insert(8)
root = Node(1)
root.insert(2)
root.insert(5)
root.insert(3)
root.insert(6)
root.insert(4)

print(root.findval(7))
print(root.findval(14))
root.printTree()
print("height = " + str(height(root)))
print("level order:")
levelOrder(root)
