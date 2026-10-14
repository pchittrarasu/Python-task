a=('green','red','blue','black','white')
print(a)
print("Second color:",a[1])
print("Fifth color:",a[4])
print('----------')

t=(10,20,30,40,50)
print(len(t))
print('First Value:',t[0],'\nlast Value:',t[len(t)-1])
print('----------')

tt=(1,2,3,2,4,2,5)
print(tt.count(2),tt.index(2))
print('------------')

s=('Raj',21,'salem')
a,b,c=s
print('Name:',a,'\nAge:',b,'\nCity',c)
print('------------')

w=(10,20,30)
z=list(w)
print(type(z))
z.append(40)
print(z)
w=tuple(z)
print(type(w))
print(w)

