# 1) positive or negative number
"""
def check_num(num):
    if num > 0:
        print("positive number")
    elif num <0:
        print("negative number")
    else:
        print("zero")
i = int(input("Enter a number: "))
check_num(i)

# 2) even or odd number
def check_even_odd(num):
    if num %2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
check_even_odd(i) # take input from above, if we dont declare it like below by separately then it will take the input from above and check for even or odd number


# 3) checking number divisible by 5 or not
def check_divisible(num):
    if num % 5 == 0:
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is not divisible by 5")
i1 = int(input("enter a number : "))
check_divisible(i1)
"""
"""

# 4) find big from 2 numbers :
def fun(i,j):
    if i>j:
        print(f"{i} is the big number")
    else:
        print(f"{j} is the big number")
#big_num = map(float,input(f"enter 2 numbers : ").split())
i,j = map(float,input(f"enter 2 numbers : ").split(','))
fun(i,j)
"""
# Without a space, Python sees only one number and crashes because it needs two separate values.
#big_num = map(float,input(f"enter 2 numbers : ").split())
#Note : # What happens behind the scenes:
# map(float, ['10', '20'])  ---> Converts both to floats: 10.0 and 20.0
#x, y = map(float, input("Enter two numbers: ").split())
"""
# 5) find big from 3 numbers:
def fun(i,j,k):
    if i>j and i>k:
        print(f"{i} is bigger number: ")
    elif j>i and j>k:
        print(f"{j} is bigger number: ")
    else:
        print(f"{k} is bigger number: ")
i,j,k = map(float,input(f"enter 3 numbers").split(','))
fun(i,j,k)
"""
# 6) finding leap year :
"""
Note : Think of it like a security checkpoint with these steps:
1) Is the year divisible by 4? Yes. 
2) Is it a century year ending in 00? No? Then it is safely a Leap Year (e.g., 2024).
3) Is it a century year ending in 00? Yes? Then it is blocked unless it can also pass the ultimate 400 test (e.g., Year 2000 is a Leap Year, but Year 1900 is Not).

def find_leap_year(num):
    if num % 4==0 and num % 100!=0 or num % 400 ==0:
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")
year = int(input(f"enter a year: "))
find_leap_year(year)

# 7) print grade based on percentage :
def grade(percentage):
    if percentage >=90:
        print("grade A")
    elif percentage >=75:
        print("grade B")
    elif percentage >=60:
        print("grade C")
    elif percentage < 60:
        print("grade D")
    else:
        print("Fail")

score = float(input("enter percentage between 0 to 100 : "))

if 0<= score <= 100:
    grade(score)
else:
    print("enter valid number")

#Xponentium:-
TEST_RESULTS = ["PASS", "fail", " Pass ", "FAIL", "pass", "", "Skip", None, "PASS"]
d = {}
for i in TEST_RESULTS:
    if i is not None and i.strip()!="": # `strip()` → **Removes spaces (whitespace) from the beginning and end of a string.**
        clean_item = i.strip().upper()
        if clean_item not in d:
            d[clean_item] = len(clean_item)
print(d)
"""
TEST_RESULTS = ["PASS", "fail", " Pass ", "FAIL", "pass", "", "Skip", None, "PASS"]
d = {}
for i in TEST_RESULTS:
    if i is not None and i!="":
        clean_data = i.strip().upper()
        if clean_data not in d:
            d[clean_data] = len(clean_data)
print(d)

"""
# Dictionary — Remove Duplicates

### Logic

```text
1. Take value
2. Clean → strip().upper()
3. Check key exists?
4. NO → add key:value
5. YES → skip
```

### Key Syntax

```python
d = {}                         # empty dictionary

d[key] = value                 # add key-value
d[clean_data] = len(clean_data)
```

### Important Difference

```python
d = clean_data
```

❌ WRONG — `d` is the **whole dictionary**; this replaces it with a **string**.

```python
d[clean_data] = len(clean_data)
```

✅ CORRECT — adds data **inside** the dictionary.

```text
clean_data       → KEY
len(clean_data)  → VALUE
if               → decides whether to add
```

### Example

```text
" Pass "
   ↓ strip().upper()
"PASS"
   ↓
Already key?
   ↓
YES → Skip
NO  → Add "PASS": 4
```

### Remember

```text
d = something       → replace dictionary
d[key] = value      → store inside dictionary
```

**Final:** `{"PASS": 4, "FAIL": 4, "SKIP": 4}`
"""
