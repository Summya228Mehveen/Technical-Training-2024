'''l=[2,3,1,3,4,3,2]
temp=[]
result=[]
i=0
while(i<len(l)):
    if l[i] not in temp:
        temp.append(l[i])
        i += 1
    else:
        result.append(temp)
        temp=[]
result.append(temp)
print(result)
'''

'''
a=[1,2,3,4,1,2,3,1,2]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c += 1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)'''
'''
a=[1,2,3,4,1,2,3,1,2]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i] = 1
    else:
        d[i]+=1
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i] = d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)
'''

'''s=input()
s1 = set(s)
if(len(s1)==27):
    print("true")
else:
    print("false")
'''
'''
a=input()
d={}
s=""
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s += a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i += 1
    i = d[a[i]]+1
print(m)
'''
'''
n=3
a=[[1,0,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]
def tree(i,j,a,n):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1 :
        return
    if a[i][j]==1 :
        a[i][j]=2
    tree(i,j-1,a,n)
    tree(i-1,j,a,n)
    tree(i+1,j,a,n)
    tree(i,j+1,a,n)
tree(1,1,a,len(a))
c=0
for i in a:
    for j in i:
        if j==2:
            c+=1
print(c)
'''
'''
def fun(i,j,a,n):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1 :
        return
    if a[i][j]==1 :
        a[i][j]=2
    fun(i,j-1,a,n)
    fun(i-1,j,a,n)
    fun(i+1,j,a,n)
    fun(i,j+1,a,n)
    
a=[]
n=int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
i=int(input())
j=int(input())
fun(i-1,j-1,a,len(a))
print(a)
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            c+=1
print(c)
'''
'''
ip: 4
tued
fwow
roer
drui
--->word
op:
yes 
'''
def fun(i,j,k,t):
    if (k==len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if(a[i][j] == s[k]):
        a[i][j] = 0
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j-1,k+1)
    t=fun(i,j+1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if(a[i][j] == s[0]):
            c=fun(i,j,1,0)
            if(c==1):
                print("yes")
if(c==0):
    print("No")