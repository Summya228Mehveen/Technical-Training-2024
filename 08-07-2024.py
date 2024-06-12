'''
def pairs(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                print(l[i],l[j],l[k])
l = [3,2,5,4,1,6,8]
pairs(l)
'''
'''
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
    fun([],0)
l= [3,2,5,4,1,6,8]
k = 5
combination(l,k)
'''
'''
def pairs(l,start,l1):
    if len(l1)==3:
        print(l1)
        return
    for i in range(start,len(l)):
        pairs(l,i+1,l1+[l[i]])
l = [3,2,5,4,1,6,8]
l1=[]
pairs(l,0,l1)
'''
'''
s="school"
res=""
l1=[]
q=3
l=2
s1=s[2:]+s[:2]
print(s1)
res+=s1[0]
r=3
s2=s[3:]+s[:3]
print(s2)
res+=s2[0]
s3=s[1:]+s[:1]
res+=s3[0]
print(res)
i,l=0,len(s)
while q<=len(s):
    l1.append(s[i:q])
    i+=1
    q+=1
print(l1)
count=0
flag=0
x=""
for i in range(len(l1)):
    x=l1[i]
    for i in x:
        if i in res :
             count+=1
    if count==3 :
         flag=1
         break
    else :
       x=""
       count=0
if flag==1:
    print("yes")
else :
    print("no")
'''
'''
a=input()
n=int(input())
str = ''
for i in range(n):
    b = input()
    if(b[0] == 'L'):
        str
        str+a[int(b[2])]
    else:
        str = str+a[-int(b[2])]
print(str)
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()
    b.append(t)
print(b)
for i in b:
    if i==str:
        print("Yes")
        break
else:
    print("No")

'''
'''
def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
a = int(input())
for i in range(1,((a//2)+1)): 
    if(isprime(i) and isprime(a-i)):
        print("Yes")
        break
else:
    print("No")
'''
'''
n = int(input())
while(n):
    a=input()
     c=input()
    s=''
    for i in a:
        if(i in c):
            s = s+(i*c.count(i))
    print(s)
    n-=1
'''
def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le = l[0]+fun(l[2:])
    ri = l[1]+fun(l[3:])
    return max(le,ri)
l = [13,9,4,10,5,7]
print(fun(l))