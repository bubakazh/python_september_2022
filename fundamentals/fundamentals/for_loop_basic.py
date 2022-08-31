# BASIC
for i in range(151):
    print(i)

# MULTIPLES OF 5
for i in range(1001):
    if i % 5 == 0:
        print(i)

# COUNTING, DOJO WAY
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Dojo")
    else:
        print(i)

# WHOA. YUUUGE
sum = 0
for i in range(500000):
    if i % 2 != 0:
        sum = sum + i
print(sum)

# COUNTDOWN BY FOURS
for i in range(2018,0,-4):
    print(i)

# FLEXIBLE COUNTER
loNum = 0
hiNum = 1933
mult = 7
for num in range(loNum,hiNum):
    if num % 7 == 0:
        print(num)
