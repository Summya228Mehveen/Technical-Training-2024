class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def sum1(self):
        t=head
        s=0
        while(t!=None):
            s+=t.data
            t=t.next
        print(s)
    def lastnode(self,x):
        t=head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addbeg(self,x):
        if head==None:
            t=node(x)
            self.head=t
        else:
            t=node(x)
            t.next=self.head
            self.head=t
    def addevn(self):
        t=head
        while(t!=None):
            if(t.data%2==0):
                print(t.data)
            t=t.next
    def search(self,x):
        t =  head
        f=0
        while(t!=None):
            if(x==t.data):
                f=1
                break
            else:
                t = t.next
        if f==1:
            print("Yes")
                
        else:
            print("No")
    def midnode(self):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
    def length(self):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast!=None:
            print("Odd")
        else:
            print("even")
    def maxsubstr(self):
        temp = head
        c=1
        m=0
        while(temp.next.next!=None):
            if temp.data==temp.next.data-1:
                c=c+1
                temp=temp.next
                if c>m:
                    m=c   
            else:
                temp=temp.next
        print(m)
    def bubblesort(self):
        T = head
        p = None
        c=0
        while(T.next != None):
            f=0
            t=head
            while(t.next != p):
                if (t.data > t.next.data):
                    f = 1
                    t.data , t.next.data = t.next.data,t.data
                t = t.next
                c += 1
            if(f==0):
                break
            p=t
            T = T.next
            return c
                    
    def printpairs(self):
        t = head
        while(t.next!=None):
            t1=t.next
            while(t1.next!= None):
                print(t.data,t1.data)
                t1 = t1.next
            t = t.next
            
        
l=sll()
head=node(1)      
head.next=node(2)
l.lastnode(4)
l.lastnode(3)
l.lastnode(5)
l.lastnode(6)
l.lastnode(7)
l.display()
print()
l.search(3)
l.search(10)
l.midnode()
l.length()
l.maxsubstr()
#l.printpairs()
l.bubblesort()
b = l.bubblesort()
l.display()
print()
print(b)