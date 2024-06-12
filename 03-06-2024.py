'''n=input()
m = sum(list((map(int,list(n)))))
print(m)'''
'''def add(n):
    s=0
    while(n):
        s+=(n%10)
        n = n//10
    return s
def prime(x):
    if (n in ['2','3','5','7']):
        return m
    else:
        return m+1  
n = int(input())
m=n
if(n<10):
    print(n)
else:
    while(1):
        n = add(n)
        if(n<10):
            break '''
'''def fun(i,s1,s2):
    if (i==len(a)):
        return s1,s2
    if a[i]%2 == 0:
        s1 += a[i]
    if b[i]%2 !=0:
        s2 += b[i]
    return fun(i+1,s1,s2)
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
x,y = fun(0,0,0) 
print(x,y)'''
'''def fun(n):
    if n==0:
        return 0
    return n+fun(n-2)
n = int(input())
if(n%2==0):
    print(fun(n))
else:
    print(fun(n-1))'''
'''a = list(map(int,input().split(' ')))
n = len(a)
if a%2==0:
    print ("Yes")
else:
    print ("No
s = input()
cm=0
cf=0
for i in s:
    if i =='M':
        cm += 1
    if i =='F':
        cf += 1
if cm==cf:
    print("0")
elif cm>cf:
    print("M")
else:
    print("F")'''
'''s=input()
c=0
for i in s:
    if i=='M':
        c += 1
    else:
        c -= 1
if c==0:
    print("0")
elif c>0:
    print("M")
else:
    print("F")'''
s="leet**cod*e"
'''a=[]
for i in s:
    if (i!='*'):
        a.append(i)
    else:
        a.pop()
    res=''.join(a)
print(res)'''
s="is2 sentence4 This1 a3"
