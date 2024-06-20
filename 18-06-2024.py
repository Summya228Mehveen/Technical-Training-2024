'''
height = [4,3,4,5,6,1,0,6,7]
# height = [2,7,2,3,6,7,1,0,5,7] 
i=0
j=len(height)-1
res=0
left = height[i]
right = height[j]
while i<j:
    if left<right:
        i+=1
        left = max(left,height[i])
        res += left-height[i]
    else:
        j-=1
        right = max(right,height[j])
        res += right-height[j ]
print(res)
'''
'''
height = [2,7,2,3,6,7,1,0,5,7]
l=[0]*len(height)
r=[0]*len(height)
m=0
m1=0
for i in range(len(height)):
    if height[i]>m:
        m=height[i]
        l[i]=m
for i in range(len(height)-1,-1,-1):
    if height[i]>m1:
        m1=height[i]
        r[i]=m1
s=0
for i in range(len(height)):
    s = s+abs(min(l[i],r[i])-height[i])
print(s)
'''
'''
coin=list(map(int,input().split( )))
target= int(input())
l=[]
mat=[]
for i in range(len(coin)+1):
    l=[0]*(target+1)
    mat.append(l)
for j in range(target+1):
    mat[0][j] = 99999
    mat[0][0] = 0
for i in range(1,len(coin)+1):
    for j in range(target+1):
        if coin[i-1]>j:
            mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = min(mat[i-1][j] , 1+mat[i][j-coin[i-1]])
if mat[len(coin)][target] == 99999:
    print("-1")
else:
    print(mat[len(coin)][target])
'''
#Coin Change Problem - Solution II
'''
def fun(l,n):
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j] = min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    return (l1[-1])
l=list(map(int,input().split( )))
n=int(input())
print(fun(l,n))
'''
def fun(i,j,c):
    if(i<0 or i>=n or j>=m or j<0 ):# or(i == k and j == l):
        return c
    if (i==n-1 and j==m-1):
        c = c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c = fun(i-1,j,c)
    if((i+1,j) not in vi):
        c = fun(i+1,j,c)
    if((i,j-1) not in vi):
        c = fun(i,j-1,c)
    if((i,j+1) not in vi):
        c = fun(i,j+1,c)
    vi.pop()
    return c
n = int(input())
m = int(input())
#l = int(input())
#k = int(input())
vi=[]
print(fun(0,0,0))








