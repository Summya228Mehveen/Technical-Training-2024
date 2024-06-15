class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root == None:
            return Node(x)
        else:
            if root.data > x:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root!=None:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root!=None:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
    def allsum(self,root):
        if root == None:
            return 0
        return root.data + self.allsum(root.left) + self.allsum(root.right)
    def branchsum(self,root):
        if root == None:
            return 0
        return root.data + self.branchsum(root.left) + self.branchsum(root.right)
    def evensum(self,root):
        if root ==None:
            return 0
        even_sum = 0
        if root.data % 2 == 0:
            even_sum += root.data
        even_sum += self.evensum(root.left)
        even_sum += self.evensum(root.right)
        return even_sum
    def oddsum(self,root):
        if root ==None:
            return 0
        odd_sum = 0
        if root.data % 2 == 1:
            odd_sum += root.data
        odd_sum += self.oddsum(root.left)
        odd_sum += self.oddsum(root.right)
        return odd_sum
    def absdiff(self,root):
        if root == None:
            return 0
        s = 0
        if(root.data %2 == 0):
            s += root.data
        else:
            s -= root.data
        s += self.absdiff(root.left)
        s += self.absdiff(root.right)
        return s
    def abd(self,root):
        if root == None:
            return 0
        if root.data%2==0:
            return root.data+self.abd(root.right)+self.abd(root.left)
        return self.abd(root.left)+self.abd(root.right)-root.data
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leafnodes(self,root):
        if root == None:
            return 
        if self.leafnodes(root.left)==None and self.leafnodes(root.right) == None:
            return 1
        return self.leafnodes(root.left)+ self.leafnodes(root.right)
    def sumleaf(self,root):
        if root == None:
            return 
        if self.sumleaf(root.left)==None and self.sumleaf(root.right) == None:
            return root.data
        return self.sumleaf(root.left)+ self.sumleaf(root.right)
    def search(self,root,x):
        if root == None:
            return False
        if x==root.data:
            return True
        elif root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    def depth(self,root,y,c):
        if root == None:
            return -1
        if root.data==y:
            return c
        if(root.data>y):
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
            
    def left(self,root,c,l):
        if root==None:
            return
        if c not in l :
            l.append(c)
            print(root.data,end=" ")
        self.left(root.left,c+1,l)
        self.left(root.right,c+1,l)
    def right(self,root,c,l):
        if root==None:
            return
        if c not in l :
            l.append(c)
            print(root.data,end=" ")
        self.right(root.right,c+1,l)
        self.right(root.left,c+1,l)
    def top(self,root):
        if root == None:
            return
        d = {}
        q = [(root, 0)]
        while q:
            root, level = q.pop(0)
            if level not in d:
                d[level] = root.data
            if root.left != None:
                q.append((root.left, level - 1))
            if root.right != None:
                q.append((root.right, level + 1))
        for i in sorted(d):
            print(d[i], end=" ")
    def bottom(self,root):
        if root == None:
            return
        d = {}
        q = [(root, 0)]
        while q:
            root, level = q.pop(0)
            d[level] = root.data
            if root.left != None:
                q.append((root.left, level - 1))
            if root.right != None:
                q.append((root.right, level + 1))
        for i in sorted(d):
            print(d[i], end=" ")
        
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 3)
t1.root = t1.create(t1.root, 8)
t1.root = t1.create(t1.root, 30)
t1.root = t1.create(t1.root, 15)
print("Inorder traversal:")
t1.inorder(t1.root)
print("\nPreorder traversal:")
t1.preorder(t1.root)
print("\nPostorder traversal:")
t1.postorder(t1.root)
print()
print(t1.allsum(t1.root))
print(t1.branchsum(t1.root.left))
print(t1.branchsum(t1.root.right))
print(abs(t1.branchsum(t1.root.left)-t1.branchsum(t1.root.right)))
print(t1.evensum(t1.root))
print(t1.oddsum(t1.root))
print(abs(t1.evensum(t1.root) - t1.oddsum(t1.root)))
print(abs(t1.absdiff(t1.root)))
print(t1.height(t1.root))
print(abs(t1.abd(t1.root)))
print(t1.height(t1.root.left))
print(t1.height(t1.root.right))
print(t1.balance(t1.root))
print(t1.leafnodes(t1.root))
print(t1.sumleaf(t1.root))
print(t1.search(t1.root,15))
print(t1.search(t1.root,25))
print(t1.depth(t1.root,15,0))
print(t1.depth(t1.root,10,0))
print(t1.depth(t1.root,100,0))
t1.left(t1.root,0,[])
print()
t1.right(t1.root,0,[])
print()
t1.top(t1.root)
print()
t1.bottom(t1.root)
