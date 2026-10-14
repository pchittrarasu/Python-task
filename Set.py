a={1,2,2,3,3,4,5}
print(a)
a.add(6)
a.remove(3)
print(a)
print('-----')

a={1,2,3}
b={3,4,5}
print('Unique no:',a.symmetric_difference(b))
print('Common no:',a.intersection(b))
print('------')

a={101,102,103,104}
b={103,104,105,106}
print('Belongs to A:',a.difference(b))
print('-------')

