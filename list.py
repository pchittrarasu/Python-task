#List:

Fname=[]
Lname=[]
name=[]
n=5
i=0
while(i<n):
    Fname.append(input())
    Lname.append(input())
    i+=1
print(Fname,end=',')
print()
print(Lname, end=',')
print(len(Fname))

fruit=['apple','orenge','lemon','berry','watermelon']
print(fruit)
fruit.append(input())
print('Updated:',fruit)
fruit.remove('lemon')
print('removed list:',fruit)

num=[12,45,78,89,23]
b=len(num)

def min(c,d):
    if c<d:
        #print(c,'<',d)
        return c
    else:
        #print(d,'<',c)
        return d
def max(c,d):
    if c>d:
        #print(c,'>',d)
        return c
    else:
        #print(d,'>',c)
        return d
    
c=num[0]    
for a in range(1,b):
    
    d=num[a]
    
    c=(min(c,d))
    a+=1
print('Min:',c)
    
d=num[0]       
for a in range(1,b):
    
    c=num[a]
    
    d=(max(c,d))
    a+=1
print('Max:',d)

a=[1,2,3,4,5,6,7,8]
odd=[]
even=[]
for i in range(len(a)):
    b=a[i]
    if b%2==0:
        even.append(b)
    else:
        odd.append(b)
    i+=1
print(odd)
print(even)

dup=[1,2,3,2,4,5,5,7,9]
u=[]
o=[]
a=len(dup)-1
for i in range(a):
    b=a-1
    j=1
    c=dup[i]
    print(c)
    for j in range(1,a):
        d=dup[j]
        print(d)
        bl=False
        if c!=d and bl==True:
            bl=bool(c!=d)
        j+=1
    if bl==True:
        u.append(c)
        
    print(u)
    i+=1

arr=[1,2,3,2,4,5,5,7,9,2]
#a=set(arr)
#print(type(a))
print(list(set(arr)))

p = [10, 20, 30, 20, 40, 10, 50, 10]
d=[]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arrm[j]:
            print(arr[i])
            break
    else:
        d.append(arr[i])
    print(d)
        


