a={'name':'Arun','age':21,'mark':50}
print('Name:',a.get('name'))
print('Age:',a.get('age'))
print('Mark:',a.get('mark'))
a['age']=25
a.setdefault('city','Salem')
print(a)
print('---------')

mark={'Arun':85,'Bala':92,'Cathy':78,'Divya':95}
l=[]
for i in mark:
    l.append(mark[i])
print(l)
m=max(l)
print(m)

for i,j in mark.items():
    if j==m:
        print(i)
        
