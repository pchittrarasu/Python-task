
Uname=str(input('Enter the User Name:'))
Uname.strip()
Uname.capitalize()
if Uname.startswith('A') is True:
    print(Uname,'Correct format')
else:
    print('Incorrect format')
print('----------')

Fname=str(input('Enter the file name:'))

if Fname.endswith('.py') is True:
    print(Fname, 'is ends with .py')
if Fname.isalnum() is True:
    print(Fname, 'is Alpha and Digit')
if Fname.isascii() is True:
    print(Fname, 'is ASCII')
else:
    print('wrong')
print('----------')

Ph=input('Mobile Number')
if Ph.isdigit() is True:
    print(Ph.zfill(15))
else:
    print('Wrong')
print('----------')

d=input('Text')
print(d.upper())
print(d.replace(' ','-'))
l=d.split(' ')
c=len(l)
print(l)
i=0
while(i<c):
    print(l[i])
    i+=1




