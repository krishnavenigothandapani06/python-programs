#Identify the Nature of a Number
a=int(input())
if a>=2:
  print("POSITIVE")
elif a<=-1:
  print("NEGATIVE")
else:
  print("ZERO")
#Explore Math Functions
import math
a=float(input())
b=int(input())
c=int(input())
d=int(input())
print(math.floor(a))
print(math.ceil(a))
print(round(a))
print(int(math.sqrt(b)))
print(int(math.pow(c,d)))
#Smallest of Four Numbers
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(a,b,c,d))
#Truncate to Two Decimal Places
import math
a=float(input())
print(f"{math.trunc(a * 100) / 100}")
#Find Second Maximum Number
a=int(input())
b=int(input())
c=int(input())

if a == b == c:
    print("No second max")
elif a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
else:
    if a >= c:
        print(a)
    elif b >= c:
        print(c)
    else:
        print(b)
#denote the angles of a triangle.
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("VALID")
    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")
#Number to Word
a=int(input())
match a:
  case 0:
    print("zero")
  case 1:
    print("one")
  case 2:
    print("two")
  case 3:
    print("three")
  case 4:
    print("four")
  case 5:
    print("five")
  case 6:
    print("six")
  case 7:
    print("seven")
  case 8:
    print("eight")
  case 9:
    print("nine")
  case _:
    print("invalid")
#Vowel or consonant
ch=(input())
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U': 
  print("vowel")
else:
  print("consonant")
#Leap Year Checker
a =int(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
  print("yes")
else:
  print("no")
#Fun Grade Calculator
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=a+b+c+d+e
average=total/5
if average >= 90:
  print("Excellent!")
elif average >= 80 and average < 90:
  print("Great Job!")
elif average >= 70 and average < 80:
  print("Good Effort!")
elif average >= 50 and average < 70:
  print("Keep Trying!")
else:
  print("Better Luck Next Time!")
#Train Berth Type Finder
seat=int(input())
no=seat%8
match no:
  case 1:
    print("LB")
  case 2:
    print("MB")
  case 3:
    print("UB")
  case 4:
    print("LB")
  case 5:
    print("MB")
  case 6:
    print("UB")
  case 7:
    print("SL")
  case 0:
    print("SU")
#Electricity Bill Calculator
units=float(input())
amount=0.0
if units>=0 and units<=50:
  amount=units*1 
elif units>=51 and units<=150:
  amount=50+(units-50)*2 
elif units>=151 and units<=250:
  amount=50+200+(units-150)*3
else:
  amount=50+200+300+(units-250)*4 
if amount>150:
  print(int(amount*0.2+amount))
else:
  print(int(amount))
#Thala vs Thalapathy Game
n=int(input())
if n%3==0 and n%5==0:
  print("ThalaThalapathy")
elif n%3==0:
  print("Thala")
elif n%5==0:
  print("Thalapathy")
else:
  print(n)
#Train Fare Calculator
age = int(input())
distance = int(input())
fare = distance * 5
if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75
print(int(fare) if fare.is_integer() else fare)
#Average Marks Calculator
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=(a+b+c+d+e)
average=total/5
if average==int(average):
  print(int(average))
else:
  print(f"{average:.2f}")
#Fun Character Case Converter
ch=(input())
if ch.islower():
  print(ch.upper())
elif ch.isupper():
  print(ch.lower())
else:
  print("abcd theriyatha?")
  
    
