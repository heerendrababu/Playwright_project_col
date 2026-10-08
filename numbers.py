#22) check whether a number is prime or not :
# prime : A prime number is a number greater than 1 that is divisible only by 1 and itself.
# Example: 2, 3, 5, 7, 11
"""
Map:
START
  ↓
Check all possible divisors
  ↓
Count how many divide the number
  ↓
Loop finished?
  ↓
YES
  ↓
Is count == 2?
  ↓
YES → Prime
NO  → Not Prime
"""
"""
num = 15
count =0
for i in range(1,num+1):
    if num%i==0:
        count = count+1

if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime")

#1) checking a number is prime or not:
"""
"""
num = int(input("Enter a number: "))
count =0
for i in range(1,num+1):
    if num%i==0:
        count = count+1
if count == 2:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


# 2)print numbers from 1 to 10:
l =[]
n = int(input("Enter a number: "))
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if i%j ==0:
            count = count +1
    if count ==2:
        l.append(i)
print(f"{l} are prime numbers")
"""
"""
Note: 
count = 0 must be inside the i loop because you need to reset the count for each new number.
if count == 2 must be inside the i loop because you need to check each number immediately after counting its divisors.

#3) find the largest of n numbers:
#n = list(input("Enter a list of numbers: "))
# or
n = list(map(int, input("Enter numbers separated by space: ").split()))
big = 0
for i in n:
    if i >big:
        big = i
print(big)
"""

"""
Note : 
`for i in n:` → `i` directly represents each **value** in the list.
`for i in range(len(n)):` → `i` represents the **index/position**, and `n[i]` gives the value at that index.
split()       → separates values
map(int, ...) → converts strings to numbers
list(...)      → makes the result a list

# 4) find the smallest of n numbers:
n = list(map(int,input("enter numbers wi.th space ").split()))
small = 0
for i in n:
    if i<small:
        small = i
print(small)

n = 153
original = n
str_data = str(n)
last_digit = 0
temp = 0
for i in str_data:
    last_digit = n%10
    temp = last_digit**3+temp
    n = n//10
if original == temp:
    print(f"{original} is armstrong")
else:
    print(f"{original} is not armstrong")
"""

"""
# 7) check whether a number is palindrome or not:
num = 12321
str_data = str(num)
original = num
temp = ""

for i in str_data:
    last_digit = num % 10
    num = num // 10
    temp = str(last_digit) + temp

print(temp)

if str(original) == temp:
    print(f"{original} is palindrome")
else:
    print(f"{original} is not palindrome")
"""
"""
#or using while:
num = 123320
original = num
rev = 0
while num >0:
    last_digit = num %10
    rev = rev*10+last_digit
    num = num//10

print(rev)
if rev == original:
    print("it is a palindrome")
else:
    print("not a palindrome")

# or using slicing
num = 123321
data = str(num)
if data == data[::-1]:
    print("it is palindrome")
else:
    print("not a palindrome")

#8) Fibonacci series:
x = 0
y = 1
print(x)
print(y)
n = 7
while n>2:
    res = x+y
    print(res)
    x = y
    y = res
    n = n-1

# or - without temp var:
x = 0
y = 1

for i in range(7):
    print(x)
    x, y = y, x + y
# or - using list:
fib = [0, 1]

for i in range(2, 7):
    fib.append(fib[-1] + fib[-2])

print(fib)

#9) Find the GCD of two numbers:
num1 = 12
l1 =[]
num2 = 18
l2=[]
for i in range(1,13):
    if num1%i ==0:
        l1.append(i)
print(l1)
for j in range(1,num2+1):
    if num2%j ==0:
        l2.append(j)
print(l2)
#l1 intersect l2
# common = [i for i in l1 if i in l2]
# print(max(common))
# or [without predefined]
common =[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)
gcd = 0 # or big = 0
for i in common:
    if i>gcd:
        gcd= i
print("gcd value or bigger value in common list: ",gcd)

# 10) Finding LCM of two numbers

num1 = 12
num2 = 18

l1 = []
l2 = []

for i in range(1, num2 + 1):
    l1.append(num1 * i)

print(l1)

for j in range(1, num1 + 1):
    l2.append(num2 * j)

print(l2)

for i in l1:
    if i in l2:
        print("LCM =", i)
        break
"""

