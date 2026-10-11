
print('1. Odd or even number')
n=int(input('Enter the Number:'))
if n%2==0:
    print(n, "is Even number.")
else:
    print(n, 'is odd number.')
print("-------------------------")

print('2. Divisible 2&3')
n=int(input('Enter Number:'))
if n%2==0 and n%3==0:
    print('Divisible by Both')
else:
    print('Not Divisible by both')
print("-------------------------")

print("3. Multiple of 5")
a=int(input('Enter a number:'))
if a%5==0:
    print('Multiple of 5')
else:
    print('Not multiple of 5')
print("-------------------------")

print("4. Leap year")
year=int(input('Enter year:'))
if year%4==0:
    print(year, 'is leap year')
else:
    print(year, 'is not leap year')
print("-------------------------")

print("5. Student Grades")
mark=int(input('Enter the Mark out of 100:'))
if mark>=50 and mark<60:
    print('E Grade')
elif mark>60 and mark<=70:
    print('D Grade')
elif mark>70 and mark<=80:
    print('C Grade')
elif mark>80 and mark<=90:
    print('B Grade')
elif mark>90 and mark<=100:
    Print('A Grade')
else:
    print('Mark is Below 50')
print("-------------------------")

print("6. Number is +/-/0")
a=int(input('Enter a number:'))
if a==0:
    print(a, 'is Zero')
elif a<0:
    print(a, 'is Negative')
else:
    print(a,'is Positive')
print("-------------------------")

print("7. Party Entry")
t=str(input('Ticket(Yes/No):'))
age=int(input("Enter your age: "))

if t.upper()=="YES" and age>=18:
    print('Welcome to the Party')
else:
    print('You are not Eligible to attend the Party')
print("-------------------------")

print("8. Login System")
username=str(input('User name:'))
pwd=str(input('Password: '))
if username=='admin' and pwd=='admin':
    print('Login Successful')
else:
    print('Wrong Username and Password')
print("-------------------------")

print("9. Vowels or Consonant")
a=(input('Enter a Charecter:'))
if a in 'a, e, i, o, u':
    print('Vowels')
else:
    print('Consonant')
print("-------------------------")

print("10. Min & Max")
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if a>b and a>c:
    print('Maximum:', a)
elif a<b and b>c:
    print('Maximum:', b)
elif a<c and b<c:
    print('Maximum:', c)
    
if a<b and a<c:
    print('Minimum:', a)
elif a>b and b<c:
    print('Minimum:', b)
elif a>c and b>c:
    print('Minimum:', c)
print("-------------------------")

print("11. Age Category")
age=int(input('Enter your age:'))
if age>=0 and age<12:
    print('You are Child')
elif age>=12 and age<20:
    print('You are Teen')
elif age>=20 and age<=59:
    print('You are adult')
elif age>=60:
    print('You are Senior')
print("-------------------------")

print("12. Calculator")
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=str(input('Add/Sub/Multiple/Divide:'))

if c.upper()=="ADD":
    d=a+b
    print(d)
elif c.upper()=="SUB":
    d=a-b
    print(d)
elif c.upper()=="MULTIPLE":
    d=a*b
    print(d)
elif c.upper()=="DIVIDE":
    d=a/b
    print(d)
else:
    print("Try Again")
print("-------------------------")

print("13. Cube number is 100?")
a=int(input('Enter a number:'))
b=a**3
if b==100:
    print(a,'cube is',b,' ,equal to 100')
elif b<100:
    print(a,'cube is ',b,',below 100')
elif b>100:
    print(a,'cube is ',b,',above 100')
print("-------------------------")

print("14. Leap year")
year=int(input('Enter Year:'))
if year%4==0:
    print(year,'is leap year1')
elif year%100==0:
    print(year,'is leap year2')
elif year%400==0:
    print(year,'is leap year3')
else:
    print(year,'is not leap year')
print("-----------End--------------")
