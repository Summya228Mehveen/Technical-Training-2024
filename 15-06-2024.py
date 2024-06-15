'''
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
l=[]
i=0
s=0
while i < len(l1):
    if l1[i]%2 == 0:
        j=0
        while j< len(l2):
            if l2[j] % 2 == 1:
                s = l1[i]+l2[j]
                l.append(s)
            j += 1
    i += 1
print(l)
'''

'''
l1=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
l2=[5,6,5,4,11,2]
l=l2.copy()
i=1
while i<len(l1):
    j=0
    while j<i:
        if l1[j][1]<=l1[i][0]:
            if l[j]+l2[i]>l[i]:
                l[i] = l[j]+l2[i]
        j+=1
    i+=1
print(l)
print(max(l))
'''
#length of largest subsequence
'''
s1=input()
s2=input()
n=len(s1)
m=len(s2)
mat=[]
l=[]
s=""
for i in range(n+1):
    l=[0]*(m+1)
    mat.append(l)
for i in range(1,n+1):
    for j in range(1,m+1):
        if(s1[i-1] == s2[j-1]):
            mat[i][j] = mat[i-1][j-1] +1
        else:
            mat[i][j] = max(mat[i][j-1],mat[i-1][j])
print(mat[n][m])
while(n!=0 and m!=0):#print(s[::-1])
    if(s1[n-1] == s2[m-1]):
        s += s1[n-1]
        n = n-1
        m = m-1
    else:
        if(mat[n][m] == mat[n][m-1]):
            m -= 1
        else:
             n -= 1
'''
''' else:
        if(mat[n][m] == mat[n-1][m]):
            n -= 1
        else:
            m -= 1
'''
'''
'''

'''

#input : 5
'''
'''
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
1 0 0 0 0
1 0 0 0 1
'''
'''
n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split( ))))
count = 0
def fun(l,i,j,n):
    if l[i][j] == 0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if j>0:
        fun(l,i,j-1,n)
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            count += 1
            fun(l,i,j,n)
print(count)
'''
'''
def area(l,n):
    m = 0
    def fun(i,j):
        if i < 0 or i >= n or j < 0 or j >= n or l[i][j] == 0:
            return 0
        if l[i][j] == 1:
            l[i][j] = 0
        area = 1
        area +=fun(i+1,j)
        area +=fun(i-1,j)
        area +=fun(i,j+1)
        area += fun(i,j-1)
        return area
    for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                c = fun(i,j)
                m = max(m,c)
    return m
    
n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split( ))))
print(area(l,n))
'''
#n = 7262 sec and output : 2h:1m:2s
'''
n = int(input())
m = n//3600
k = n%3600
s = k//60
l = k%60
print(m,"hours:",s,"minutes:",l,"seconds")
'''
