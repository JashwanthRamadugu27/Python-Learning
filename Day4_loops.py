# Day 04 — Loops

# 1. FOR LOOP
for i in range(1, 11):
    print(i)


# 2. RANGE WITH STEP — EVEN NUMBERS
for i in range(2, 21, 2):
    print(i)


# 3. COUNTDOWN
for i in range(10, 0, -1):
    print(i)


# 4. CONTINUE — SKIP 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 5. BREAK — STOP AT 8
for i in range(1, 21):
    if i == 8:
        break
    print(i)


# 6. SUM OF NUMBERS 1 TO 10
total = 0

for i in range(1, 11):
    total = total + i

print(total)


# 7. SUM OF EVEN NUMBERS 2 TO 20
total = 0

for i in range(2, 21, 2):
    total = total + i

print(total)


# 8. SKIP MULTIPLES OF 3 AND STOP AT 17
for i in range(1, 21):
    if i % 3 == 0:
        continue

    if i == 17:
        break

    print(i)


# 9. COUNT EVEN NUMBERS FROM 1 TO 20
count = 0

for i in range(1, 21):
    if i % 2 == 0:
        count = count + 1

print(count)


# 10. FIND THE LARGEST NUMBER
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)


# 11. COUNT MULTIPLES OF 4 FROM 1 TO 50
count = 0

for i in range(1, 51):
    if i % 4 == 0:
        count = count + 1

print(count)