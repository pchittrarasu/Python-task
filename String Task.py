#String Task:

a=str(input('Enter the text: '))
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.capitalize())

print('-------')

b=str(input('Enter the text: '))
c=b.startswith('Python')
if c==True:
    print('text starts with Python')
else:
    print('text not starts with Python')
print('-------')

d=str(input('Enter the file name: '))
if d.endswith('py') is True:
    print('This file is Python file')
else:
    print('This file is not Python file')
print('-------')

e=str(input('Enter the Text with python:'))
f=e.replace('python','Java')
print(f)
print('-------')
g=' I put space befor and after . '
print(g)
print(g.strip())
print('-------')
h='Here we not allowed'
print(h.split('e'))
