class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root = node()
    def insert(self,s):
        t = self.root
        for i in s:
            if i not in t.d:
                t.d[i] = node()
            t = t.d[i]
            t.flag = 1
    def search(self,s):
        t = self.root
        for i in s:
            if i not in t.d:
                return False
            t = t.d[i]
        if t.flag == 1:
            return True
        else:
            return False
    def prefix(self,s):
        t = self.root
        for i in s:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def allwords_prefix(self,s1):
        def fun(t,s):
            if (t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)    
        t=self.root
        s=""
        for i in s1:
            if (i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def largest(self,l):
        #lexographically smallest prefix on longest string
        #largest string of a given prefix
        #count no of words
        #earasing words
t1=tries()
n = int(input())
for i in range(n):
    a,s = input().split()
    if a=='1':
        t1.insert(s)
    if a=='2':
        print(t1.search(s))
    if a=='3':
        print(t1.prefix(s))
    if a == '4':
        t1.allwords_prefix(s)
    if a == '5':
        print(t1.largest())







