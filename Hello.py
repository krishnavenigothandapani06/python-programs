#Count the number of digits
n=int(input())
if n==0:
  print("1")
else:
  count=0
  while n>0:
    n=n//10
    count += 1
  print(count)
#Sum of Even Digits
n=int(input())
evensum=0
while n>0:
  last=n%10
  if last%2==0:
    evensum+=last
  n=n//10
print(evensum)
#Product of Digits
n=int(input())
product=1
while n>0:
  last=n%10
  product*=last
  n=n//10
print(product)
#Reverse a Number
n=int(input())
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
print(rev)
#Palindrome Number
n=int(input())
temp=n 
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
if rev==temp:
  print("Palindrome")
else:
  print("Not Palindrome")
#First Digit of a Number
n=int(input())
while n>9:
  n=n//10
print(n)
#Count Zeros in a Number
n=int(input())
count=0
if n==0:
  count=1 
else:
  n=abs(n)
while n>0:
  last=n%10
  if last==0:
    count += 1 
  n=n//10
print(count)
#Armstrong Number
n=int(input())
temp=n 
digit=0 
while n>0:
  n=n//10
  digit+=1 
n=temp
sum=0 
while n>0:
  last=n%10
  sum=sum+last**digit
  n=n//10
if sum==temp:
  print("Armstrong")
else:
  print("Not Armstrong")
#Strong Number
n = int(input())
temp = n
sum = 0
while n > 0:
    last = n % 10
    fact = 1
    i = 1
    while i <= last:
        fact = fact * i
        i += 1
    sum = sum + fact
    n = n // 10
if sum == temp:
    print("Strong")
else:
    print("Not Strong")
#Check Perfect Number
n=int(input())
sum=0
for i in range(1,(n//2)+1):
  if n%i==0:
    sum+=i 
if sum==n:
  print("Perfect")
else:
  print("Not Perfect")
  
    
