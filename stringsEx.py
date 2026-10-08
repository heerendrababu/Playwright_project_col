#1) Take a string as input and print it
"""
s =  input("enter data: ")
print(s)

#2) find the length of the string
s = "babu"
print(len(s))
# without predefined method len():
count = 0
s1="babu @1"
print(dir(s1))
# for i in s1:
#     if i.isalnum():
#         count = count +1
# print("count of chars: ",count)

# or [without predefined methods]:
for i in s1:
    if ('a' <= i <='z') or ('A' <= i <='Z') or ('0'<=i<='9'):
        count = count+1
print("count of chars: ",count)

#3) Reverse a string :
s = "babu"
s1=""
for i in s:
    s1 = i+s1
print(s1)

#4) check whether a string is palindrome or not ?
s = "babu"
s1=""
for i in s:
    s1 = i+s1
print(s1)
if s == s1:
    print("palindrom")
else:
    print("not palindrom")

#5) count the no. of vowels in a string ?
s = "maruthi"
s1 = s.lower()
vowel_count = 0
for i in s1:
    if i in s1 and i in ('a','e','i','o','u'):
        vowel_count = vowel_count+1
print(f"vowel count of {s1} is {vowel_count}")

# or
s = "babU"
s2 = "aeiouAEIOU"
vowel_count = 0
for i in s:
    if i in s2:
        vowel_count = vowel_count+1
print(f"vowel count of {s2} is {vowel_count}")

# 6) count the no. of consonants in a string ?
s = "baU"
s2 = "aeiouAEIOU"
consonant_count = 0
for i in s:
    if i not in s2:
        consonant_count = consonant_count+1
print(f"consonant count of {s2} is {consonant_count}")

from selenium.webdriver.common.print_page_options import PrintOptions

#7) convert uppercase string to lowercase:
# s = "babu"
# print(s.upper())
# s1 = "BABU"
# print(s1.lower())
s = "ABU"
s2 = ""
for i in s:
    if 'A'<=i<='Z':
        s2 = ord(i)
        print(s2)
        l= chr(i)

# ascii
# A = 65
# + 32
# a = 97

# 8) Remove spaces from a string ?
s = "babu 01"
s1 = ""
print(s.replace(" ",""))
# or [without predefined method] :
for i in s:
    if i!=" ":
        s1 = s1+i
print(s1)

# 9) check whether a string is anagram or not ? ex : (listen and silent)
s1 = "listen"
s2 = "silent"

count_s1 = {}
count_s2 = {}

if len(s1) != len(s2):
    print("not an anagram because length doesn't match for both strings:")
else:
    for i in s1:
        if i in count_s1:
            count_s1[i] = count_s1[i]+1  # count_s1[i]+1 -> This means: Take the existing count of character i and increase it by 1.
                                         # #i is the key, and count_s1[i] means: Access the value stored for key i.
        else:
            count_s1[i] = 1

    print("count_s1 : ",count_s1)
    for i in s2:
        if i in count_s2:
            count_s2[i] = count_s2[i]+1
        else:
            count_s2[i] = 1
    print("count_s2: ",count_s2)
    if count_s1 == count_s2:
        print("it is anagram")
    else:
        print("not an anagram")
"""
# or
def check_anagram(s1, s2):

    if len(s1) != len(s2):
        print("not an anagram")
        return

    count_s1 = {}
    count_s2 = {}

    for i in s1:
        if i in count_s1:
            count_s1[i] = count_s1[i] + 1
        else:
            count_s1[i] = 1

    for i in s2:
        if i in count_s2:
            count_s2[i] = count_s2[i] + 1
        else:
            count_s2[i] = 1

    if count_s1 == count_s2:
        print("it is anagram")
    else:
        print("not an anagram")


check_anagram("listen", "silent")







