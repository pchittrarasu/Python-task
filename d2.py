#for Loop
for a in range(1,11):
    print(a, end=" ")
print()

print('Even Numbers:')
for even in range(0,20,2):
    print(even, end=", ")
print()

print('Odd Numbers:')
for odd in range(1,20,2):
    print(odd, end=", ")
print()

for a in range(1,10,1):
    print(a,'* 5=', a*5)
    
c=0
for n in range(1,11,1):
    c+=n
print('sum of 1 to 10:',c)

txt='PYTHON'
for s in range(6):
    print(txt[s])

v='programming'
c=0
for z in range(11):
    #print(v[z])
    if v[z] in ['a','e','i','o','u']:
    #if v[z]=='a' or v[z]=='e' or v[z]=='i'  or v[z]=='o' or v[z]=='u':
        c+=1
          
print('Vowels count in',"'",v,"'",':',c)

for r in range(10,0,-1):
    print(r)

re=1
for fac in range(1,6):
    re=fac*re
print(re)


for i in range(1,7,1):
    for j in range(1,i):
        if j<=i:
            print(' ', end=" ")
    print("*")
    
   
for i in range(1,7,1):
    for j in range(1,i):
        print('*', end=" ")
    print()

v=str(input('Name:'))
c=0
for z in range(len(v)):
    
    if v[z]=='a' or v[z]=='e' or v[z]=='i'  or v[z]=='o' or v[z]=='u':
        c+=1
          
print('Vowels count in',"'",v,"'",':',c)
