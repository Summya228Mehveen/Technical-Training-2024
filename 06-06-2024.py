class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def addback(self,x):
        if(self.head == None):
            self.head = node(x)
            return self.head
            self.tail = self.head
            
        else:
            self.tail.next = node(x)         #t = node(x)
            self.tail.next.prev = self.tail  #self.tail.next = t
            self.tail = self.tail.next       #t.prev = self.tail
                                           #self.tail = self.tail.next
    def addfront(self,x):
        if(self.head == None):
            self.head = node(x)
            self.tail = self.head
            
        else:
            newnode = node(x)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def display(self):
        t = self.head
        while(t!=None):
            print(t.data,end="->")
            t = t.next
        print()
    def revdisplay(self):
        t = self.tail
        while(t!=None):
            print(t.data,end="->")
            t = t.prev
        print()
    def linearsearch(self,x):
        t=self.head
        s=self.tail
        f = 0
        '''while(t.next!=None):
            if(x == t.data):
                f=1
                break
            else:
                t = t.next
        if f==1:
            print("Yes")
        else:
            print("No")'''
        while(t!=s and t!=s.next):
            if(x == t.data or x == s.data):
                f=1
                break
            else:
                t=t.next
                s=s.prev
        
        if f==1:
            print("Yes")
        else:
            print("No")
    def length(self):
        t=self.head
        s=self.tail
        f=0
        while(t!=s and t!=s.next):
            t = t.next
            s = s.prev
            if t==s:
                f=1
                break
        if f==1:
            print("odd")
        else:
            print("even")
    def palindrome(self):
        t=self.head
        s=self.tail
        f=0
        while(t!=s and t!=s.next):
            if(t.data == s.data):
                t = t.next
                s = s.prev
            else:
                f=1
                break
        if f==1:
            print("Not Palindrome")
        else:
            print("Palindrome")
    def shuffle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        q=slow
        while slow!=fast:
            print(slow.data,end='->')
            slow = slow.next
        t = self.head
        while t!=q:
            print(t.data,end='->')
            t = t.next
    def shift(self):
        slow = self.head
        fast = self.head
        while fast!=None:
            slow = slow.next
            fast = fast.next.next
        t=self.head
        t1 = slow
        while t!=t1 and t1!=None:
            t.data,t1.data = t1.data,t.data
            t = t.next
            t1 = t1.next
        print()
    def difference(self,head,s1,s2):
        if head==None:
            return abs(s1-s2)
        if head.data % 2 ==0:
            s1 += head.data
          
        else:
            s2 += head.data
        return self.difference(head.next,s1,s2)
    def prime(self,t,c):
        if t==None:
            return c
        def notprime(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return notprime(s+1,n)
        if(notprime(2,t.data)):
            c=c+1
        self.prime(t.next,c)
        
        
         
        
l1 = dll()
l1.addfront(3)
t=l1.addback(5)
print(t)
l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(10)
l1.addback(12)
l1.addback(15)
l1.display()
l1.revdisplay()
l1.linearsearch(10)
l1.linearsearch(50)
l1.linearsearch(100)
l1.linearsearch(60)
l1.length()
l1.palindrome()
l1.shuffle()
l1.shift()
l1.display()
a = l1.difference(l1.head,0,0)
print(a)