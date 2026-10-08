"""
split() → breaks a string into multiple parts based on a separator and returns a list.
Example: "10 20 30".split() → ['10', '20', '30']
# if you didn't give space in input it will take entire input as one character in single quotes.
Alternative: partition() can split into 2 parts, but for creating a list from multiple values, split() is the usual/simple choice.
"""

"""
# Note : 💡 end="," is used with print(), not with list().

# 1) create a list and print it ?
l = input("enter data with spaces: ").split() # you can enter characters also
l1 = list(map(int,input("enter list of numbers with spaces").split()))
print(l)
print(l1)

# 2) Find the length of a list ?
print(len(l))
print(len(l1))
# without predefined:
len_count = 0
for i in l:
    len_count = len_count+1
print("length of list without using predefined len() method: ",len_count)

# 3) Find the largest number in a list ?
big = 0
for i in l1:
    if i >big:
        big = i
print("big number from the list: ",big)

# 4) Find the smallest number in a list ?
small = 0
for i in l1:
    if i <small:
        small = i
print("smallest number from the list: ",small)

# 5) Find the sum of all elements in a list ?
# Note : instead of 'sum' use 'total' because sum is Python built-in function. so it may throw warning not error.
total = 0
for i in l1:
    total = total+i
print(f"sum of all elements in list: {total}")

# 6) Find the avg of all elements in a list ?
avg = total/len(l1)
print(f"avg of all elements in list: {avg}")

demo_list = list(map(int,input("enter numbers in demo_list : ").split()))
even_count = 0
odd_count = 0
for i in demo_list:
    if i %2 ==0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(f"even count of demo_list ",even_count)
print(f"odd count of demo_list ",odd_count)
"""
#8.reverse of a list
# mj=[5, 6, 8, -12, 4, 22, 10]
# reverse_mj = []
# for i in mj:
#     reverse_mj.insert(0,i)
#     reverse_mj = reverse_mj[:: -1]
# print(reverse_mj)
# #print(mj[:: -1])
# mj[3] =5 # to replace in a list is : List[index] = new value to replace
# print(mj)
'''
#alternative method
mj = [5, 6, 8, -12, 4, 22, 10]
reverse_mj = []

for i in range(len(mj) - 1,-1,-1):
    reverse_mj.append(mj[i])

print(reverse_mj)
'''
"""
#9.check whether the given number is existed or not

mj = [5, 6, 8, -12, 4, 22, 10]
n =4
found = False
for i in mj:
    if n==i:
        found = True
        break

if found:
    print(f"{n} is present in the list")
else:
    print(f"{n} is not present in the list")



#List Advanced

#1.remove duplicates from the list
ml = [5, 6, 8, -12, 4, 22, 10, 22, 4]
#ml_set = set(ml)
#print(ml_set)

#using for loo

unique = []
for i in ml:
    if i not in unique:
        unique.append(i)
print(unique)

#using dictionary
ml = [5, 6, 8, -12, 4, 22, 10, 22, 4]

unique = list(dict.fromkeys(ml))

print(unique)
"""

"""
# 2) Find the second largest in the list ?
# l = [10, 5, 20, 8, 15,18]
# big =0
# sbig = 0
# for i in l:
#     if i > big:
#         big = i
#     for j in l:
#         if j > sbig and j<big:
#             sbig = j
# print(big)
# print(sbig)

# or
l = [10, 5, 100, 8, 15,99]
big=0
second_big=0
for i in l:
    if i>big:
        big = i
    if i>second_big and i<big:
        second_big = i
print(big)
print(second_big)
# or 
l = [10, 5, 100, 8, 15, 99]

big = 0
second_big = 0

for i in l:
    if i > big:
        second_big = big
        big = i
    elif i > second_big:
        second_big = i

print(big)
print(second_big)
"""

"""
import json
data = json.dumps({"name": "John"})
print(data)
print(type(data))
j  = json.loads(data)
print(j)
print(type(j))
"""

# l = [2,7,3,4,5]
# target = 9
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] + l[j] == target:
#             print(i,j)
#             print(l[i])
#             print(l[j])

# for i in l
#        ↓
#    i = VALUE
#
# for i in range(len(l))
#        ↓
#    i = INDEX

# 10 adding first and two and substract next value :
l = [2,7,3,4,5]
res = l[0] +l[1]
print(res)
for i in range(2,len(l)):
    if i %2==0:
        res = res-l[i]
        print(res)
    else:
        res = res+l[i]
        print(res)
print("last value stored in result: ",res)

# 11)reverse of words
demo = "hello world"
demo1 = ""
for i in demo:
    demo1 = i+demo1
print(demo1)
"""
split() is a string method that automatically converts a string into a list of words based on the separator (space by default).

"hello world".split()  →  ['hello', 'world']

list() converts each individual character into a list element:

list("hello")  →  ['h', 'e', 'l', 'l', 'o']
"""

#12 Reverse Each Word Without Changing Word Position:
d = "Hello world"
w = d.split()
print(w)
w1 = ""
for i in w:
    if i not in w1:
        w1 = i+" "+w1
print(w1)

# or
w2 = " ".join(d.split()[::-1])
print("using join and slicing: ",w2)

#13 Reverse letters without changing the word position
d = "Hello world"
d1 = d.split()
d2 = ""
for i in d1:
    d2 = d2+i[::-1]+" "
print(d2)

# or
res = " ".join(word[::-1]for word in d.split())
print("using join and slicing : ",res)

#14 reverse of a list :
l =[1,2,3,4,5]
l1 =[]
for i in l:
    l1.insert(0,i)
print(l1)
"""
Important Point: append() / insert()

append() and insert() modify the existing list directly and return None, so don't assign their result back to the list.

l1.append(i)       # ✅
l1.insert(0, i)    # ✅

l1 = l1.append(i)  # ❌
l1 = l1.insert(0,i) # ❌
"""
# 14) Remove duplicates in a list :
l = [123,12,12,3]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

# 15) Find the second largest in a list :
l = [1,2,3,4,5]
big = 0
sbig = 0
for i in l:
    sbig = big
    if i >big:
        big = i
    if i>sbig and i<big:
        sbig = i
print(big)
print(sbig)

# 16) Rotate a list to left by k positions.
"""
Left rotation → First k → move to end.
Right rotation → Last k → move to beginning.
"""
# NOTE : Remember: Left rotation = front elements move to the back.
# Ex : List: [1, 2, 3, 4, 5] if  k = 2 -> [3, 4, 5, 1, 2]
# if k = 3 -> Move:  [1, 2, 3] → end
# Move:      [1, 2, 3] → end
# Result:    [4, 5, 1, 2, 3]
l = [1,2,3,4,5]
k = 2
# VVIMP : - l[k] is not slicing. It means access the element at index k.
l1 = l[k:]
print(l1)
l2 = l[:k]
print(l2)
l3 = l1 + l2
print(l3)
"""
l[k] → accesses the element at index k
l[k:] → slicing from index k to the end
l[:k] → slicing from beginning up to index k (excluding k)
"""
"""
#17) Rotate a list to right by k positions.
data1 = [1,2,3,4,5]
k = 2
position = len(data1)-k

new_list = data1[position:]
print(new_list)
new_list2 = data1[:position]
print(new_list2)
new_list3 = new_list + new_list2
print(new_list3)

#18) merging two lists :
n = [1,2,3]
n1 = [4,5]
print("Merging two lists: ")
#append(), insert(), and extend() modify the existing list and return None. Don't assign their result to another variable.
n.extend(n1) #changes n directly
print(n)

# 19) sort a list in ascending order :
k = [12,14,-1,0,3]
# k.sort()
# print(k)
temp = 0
for i in range(len(k)):
    for j in range(len(k)-1):
        if k[j] >k[j+1]:
            temp = k[j]
            k[j] = k[j+1]
            k[j+1]=temp
print(k)

s = "uday"
print(s)
s1 = ""
i = 0
while i < len(s):
    s1 = s[i]+s1
    i = i+1
print(s1)

l = [1,2,3,4,5,6,7,8,10]
for i in range(1,len(l)+1):
    if i not in l:
        print(i)

# or
l = [1,2,3,4,5,6,7,8,10]
l1 = []

# max(l) + 1 ensures we check all the way up to 10
for i in range(1, max(l) + 1):
    if i not in l:
        l1.append(i)

print(l1)  # Output: [9]
"""

"""
Given a string s, find the length of the longest substring without repeating characters.

• Example 1: s = "abcabcbb" → Output: 3 (The substring is "abc")

• Example 2: s = "bbbbb" → Output: 1 (The substring is "b")

• Example 3: s = "pwwkew" → Output: 3 (The substring is "wke")
"""

