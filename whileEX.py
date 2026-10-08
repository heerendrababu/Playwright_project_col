n =10
i = 0
while i<n:
    i = i+1
    print(i,end=",")
print()
#2)
print("reverse of a loop using while:")
n1=0
i = 10
while i>n1:
    i = i-1
    print(i,end=",")
print()
#3)
i = 0
n =20
while i<=n:
    if i%2==0:
        print(i,end=",")
    i = i+1
print()
#4)
print("odd numbers: ")
i = 0
n4 =10
while i<=n4:
    if i%2!=0:
        print(i,end=",")
    i = i+1
print()
# 5 ) print each character of string
s = "python"
i=0
while i<len(s):
    print(s[i])
    i = i+1
print()
#6) Reverse a string:
s = "python1"
s1 = ""
i = len(s)-1
while i>=0:
    s1 = s1+s[i]
    i = i-1
print(s1)
# 7) count the number of characters:
s = "babu"
count = 0
i = 0
while i<len(s):
    count = count +1
    i = i+1
print(count)
#8)