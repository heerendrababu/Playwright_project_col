# 1) print numbers 1 to 10:
# for i in range(2,102,2):
#     print(i, end=" ")
"""
By default, Python's print() ends with a hidden newline character (\n) 
that forces the next item to a new line. Changing end to a space [end=" "] or a comma[end=","] keeps everything on the same line.

# 2) print numbers 10 to 1 :
print("\n")
for i in range(10,0,-1):
    print(i,end=",")

# or
print("\n")
print(*range(10,0,-1),sep=",")

# or
print("\n")
print(*list(range(1,11))[::-1])

# 3) print even numbers from 1 to 20:
for i in range(1,21):
    if i%2==0:
        print(i, end=" ")

# or
print("\n")
def even_numbers(num):
    if i % 2 ==0:
        print(i,end=",")

for i in range(1,21):
    even_numbers(i)


l = [1,2,3,5,7]
for i in l:
    l.remove(i) #0[2,3,5,7] #3[5,7]
    if i>2:
        print(i)

# 4) odd number:
for i in range(1,20):
    if i%2!=0:
        print(i,end=",")

# 5) find sum of numbers:
sum =0
for i in range(1,5):
    sum = sum+i
print(sum)

# 6) product of numbers:
prod = 1
for i in range(1,5):
    prod = prod*i
print(prod)

# 7) factorial of a number:
# factorial of 5 : 5*4*3*2*1 = ?
fact = 1
# using slicing method:
for i in range(5,0,-1): # without slicing : range(1,6)
    fact = fact*i #1,2,6,24,120
print(fact)

# 8) print multiplication table of a number:
num = 9
res =0
# 9*1, 9*2, 9*3
for i in range(1,11):
    res = num*i # here we replace result everytime with new result because we are just using res as variable not included in calculation
    print(f"{num}*{i} = {res}") # 9,
    #res = 0
print(res)

# or
# multiplication of a number in different form
n = 2
mul = 1
for i in range(1, 11):
    res = n * mul
    print(res)
    mul = mul + 1

# 9) count the digits in a number:
num = 12332
count = 0
str_data = str(num)
print(type(str_data))
for i in str_data:
    count = count+1
print(count)

# or [without changing it to string]
num = 12332
count = 0
while num >0:
    num = num //10
    count = count + 1
print(count)

# 10) find the sum of digits in a number
num = 12344
sum1 = 0
while num >=1:
    last_digit = num%10
    #print(last_digit)
    sum1 = sum1+last_digit
    num  = num //10
print(sum1)
# or

# num = 123432
# str_data = str(num)
# sum = 0
# for i in str_data:
#     i = int(i)
#     print("first",sum)
#     sum = sum + i
#     print("after adding",sum)
# print(sum)

# or
num1 = 123432
sum = 0
while num1>=1:
    last_digit = num1 %10
    print(f"get the last digit after doing i.e.,{num1}%10 = {last_digit}")
    sum = sum + last_digit
    num1 = num1 //10
    print("removed last item",num1)
print(f"total sum : {sum}")

# loops - while:
# print numbers from 1 to n using while loop:

# 12)
l = [1,2,3,5,7]
for i in l:
    print(l)
    l.remove(i) #0[2,3,5,7] #3[5,7]
    if i>=2:
        print(i)

#13)
s = "Babu"
d ={}
for i in s.lower():
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i]+1
print(d)
d1 = {v:k for k,v in d.items()}
print(d1)
"""

# s = "babu"
# d =[]
# for i in s:
#     if s.count(i) >1 and i not in d:
#         d.append(i)
# print(d)

# --- PYTHON SLICING & RANGE() NOTE ---

# 1. The range() Limitation:
#    - CANNOT use slicing inside range() -> range(::-1) throws SyntaxError.
#    - range() only accepts: range(start, stop, step)
#    - Fix for countdown: range(10, 0, -1)

# 2. How List Slicing [::-1] Works:
#    - Syntax: my_list[start:stop:step]
#    - Step is -1: Moves BACKWARD through the sequence.
#    - Blank Start/Stop: Spans from the very end to the very start.
#    - Note: Creates a brand new copy of the list in memory.

# 3. Memory-Efficient Alternative:
#    - Use `reversed(sequence)` to loop backward without copying the list.

# --- QUICK TEMPLATES ---

"""
# 14) Countdown using range:
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8...

# 15 print numbers from 1 to n using while loop:
n = 1
print("print numbers from 1 to n using while loop:")
while n <=5:
    print(n)
    n = n+1

# 16 print numbers from n to 1 using while loop:
n = 10
print("print numbers from n to 1 using while loop",n)
while n >=1:
    print(n)
    n = n-1

#17) Find sum of digits in a number
digit = 12345
sum = 0
while digit : # or while digit != 0: --> explanation : while digit: itself is the condition so it automatically checks digit is non-zero or not
    digit1 = digit %10
    sum = sum + digit1
    digit = digit //10
print(sum)

# or 
num = 12345
sum = 0
while num>=1:
    num1 = num %10
    sum = sum + num1
    num = num //10
print(sum)

# 18) reverse a string :
# using slicing [Note: slicing will only works on sequence types like strings, lists, and tuples not integer.
d = "babu"
print("using slicing: ",d[::-1])
# or using for loop
res = ""
for i in d:
    res = i+res
print("using for loop: ",res)

# or using while:
d1 = "raju"
res = ""
i = len(d1)-1
while i>=0:
    res = res + d1[i]
    print(res)
    i = i-1
print("reverse string: ",res)

#19 ) reverse of a number:
num = 12345
d  = str(num)
res = ""
for i in d:
    res = i +res
print(res)

# or using while loop :
num1 = 123123
res1 = 0
while num1>0:
    last_digit = num1%10
    res1 = res1*10+last_digit
    num1 = num1 //10
print(res1)

# or using build-in way:
num2 = 843184
rev = "".join(reversed(str(num2)))
print(rev)

# 20) count digits of a number:
num = 9888928901
str_count = str(num)
count =0
for i in str_count:
    count = count +1
print(count)

# without changing to string using while:
num = 292929292
count = 0
while num>0:
    num = num //10
    count = count +1
print(count)

#21) factorial using while
fact = 1
num = 5
while num >0:
    fact = fact *num
    num = num-1
print(fact)
"""
num = 123
rev = 0
while num>0:
  ld=num%10
  rev = rev*10+ld
  num = num/10
print(rev)
