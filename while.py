#while
a=0
while(a<10):
    a+=1
    print(a)
print('---------------')
b=11
while(b>0):
    b-=1
    print(b)
print('---------------')
odd=1
while(odd<=20):
    print(odd)
    odd+=2
print('---------------')

s=1
t=1
while(s<10):
    s+=1
    t+=s
print(t)
print('---------------')

m=7
x=0
while(x<10):
    x+=1
    print(x,'*', m,'=',m*x)
print('---------------')

c=1
f=1
while(c<=5):
    f*=c
    c+=1
print(f)
print('---------------')

d=int(input('enter the numbers'))
e=0
while(d>=1):
    d=d//10
    #print(d)
    if d>=0:
        e+=1
print(e)
print('---------------')
    
t=int(input("Enter the number:"))
r=1
while(t>0):
    r=t%10
    print(r, end='')
    t=t//10
print()    
print('---------------')





    

