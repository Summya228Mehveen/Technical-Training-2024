'''s=input()
count = 1
maximum = 0
for i in range(len(s)-1):
    if(ord(s[i]) == ord(s[i+1])-1):
        count += 1
    else:
        if(count>maximum):
            maximum = count
        count = 1
if(count>maximum):
    maximum = count
print(maximum)'''

'''n = int(input())
l=[]
for i in range(n):
    l.append(list(map(str,input().split(" "))))
print(l)
s = input()
flag=0
for i in range(len(s)):
    if(s[i] not in l[i%n]):
        print("No")
        flag=1
        break
    else:
        l[i].remove(s[i])
if (flag==0):
    print("yes")'''
'''
print("*", str(i * 3 + 1) + str(i * 3 + 2) + str(i * 3 + 3), "*")
a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
a.append(78)
a.extend([2])
print(len(a))'''
'''a={5,1,'5',(5,2),1,(2,5),"hi",'hi',True,False}
print(len(a))'''
'''def rev(n,r):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)
n = int(input())
if(rev(n,0)==n):
    print("Palindrome")
else:
print("Not palindrome")'''
'''
* * * * *
* 1 2 3 *
* 4 5 6 *
* 7 8 9 *
* * * * *
'''
'''n = int(input())
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*",(i*3+1),(i*3+2),(i*3+3),"*")
'''
'''n = int(input())
k=1
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("* ",end=' ')
        else:
            print(k,end=' ')
            k+=1
    print()'''

'''
output : 
_ _ _ _ a _ _ _ _
_ _ _a b a _ _ _
_ _ a b c b a _ _
_ a b c d c b a _
'''

'''
#Input :- 4
Output:
1 1 1 1 1 1 1
1 2 2 2 2 2 1
1 2 3 3 3 2 1
1 2 3 4 3 2 1
1 2 3 3 3 2 1
1 2 2 2 2 2 1
1 1 1 1 1 1 1
'''
