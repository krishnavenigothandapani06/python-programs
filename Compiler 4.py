#Length of a basestring
s = input()
print(len(s))
#Join the strings
s1 = input()
s2 = input()
print(s1 + " " + s2)
#Compare the Strings
s1 = input()
s2 = input()
if s1==s2:
  print("true")
else:
  print("false")
#First character of a basestring
s = input()
print(s[0])
#Last character of a basestring
s = input()
print(s[-1])
#Join first & last characters of a basestring
s=input()
print(s[0]+s[-1])
#Alphanumeric strings
s=input()
numcount=alphacount=False
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isdigit():
    numcount=True
if alphacount and numcount:
  print("true")
else:
  print("false")
#Uppercase check
s=input()
if s.isupper():
  print("true")
else:
  print("false")
#Lowercase check
s=input()
if s.islower():
  print("true")
else:
  print("false")
#String lengths equal or not
s1=input()
s2=input()
if (len(s1)==len(s2)):
  print("true")
else:
  print("false")
#Reverse a basestring
s=input()
print(s[::-1])
#Split strings by comma
s=input()
for i in s.split(","):
  print(i)
#Remove vowels
s=input()
vow="aeiouAEIOU"
for i in s:
  if i in vow:
    s=s.replace(i,"")
print(s)
#Reverse the character swapcase
s=input()
print(s.swapcase())
#Print ascii value
s=input()
print(ord(s))
#Remove occurrences of a char
s=input()
c=input()
print(s.replace(c,""))
#Search for a word
s=input()
word=input()
print("true" if word in s else "false")
#Count vowels and consonants
s=input()
vow=0
con=0
for i in s:
  if i in "aeiouAEIOU":
    vow=vow+1 
  else:
    con=con+1 
print(vow)
print(con)
#Anagram check
s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
if(len(s1)==len(s2)):
  print("true")
elif sorted(s1)==sorted(s2):
  print("true")
else:
  print("false")
#Palindrome check
s=input()
if s==s[::-1]:
  print("true")
else:
  print("false")
