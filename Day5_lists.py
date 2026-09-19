# Day 5 - Lists & List Operations


# 1. Creating Lists

fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40, 50]
data = ["Jashwanth", 19, 8.5, True]

print(fruits)
print(numbers)
print(data)


# 2. Positive Indexing

marks = [69, 70, 99, 100, 35]

print(marks[2])


# 3. Negative Indexing

print(marks[-1])
print(marks[-2])


# 4. Changing List Items

marks[4] = 50

print(marks)


# 5. append()

fruits.append("orange")

print(fruits)


# 6. insert()

fruits.insert(2, "grapes")

print(fruits)


# 7. remove()

fruits.remove("mango")

print(fruits)


# 8. pop()

fruits = ["apple", "banana", "mango", "orange"]

fruits.pop(1)

print(fruits)


# 9. len()

print(len(marks))


# 10. Looping Through a List

for mark in marks:
    print(mark)


# 11. Practice - Access Third Item

numbers = [10, 20, 30, 40, 50]

print(numbers[2])


# 12. Practice - Change 30 to 100

numbers = [10, 20, 30, 40, 50]

numbers[2] = 100

print(numbers)


# 13. Practice - append()

numbers = [10, 20, 30, 40, 50]

numbers.append(60)

print(numbers)


# 14. Practice - insert()

numbers = [10, 20, 30, 40, 50]

numbers.insert(1, 15)

print(numbers)


# 15. Practice - remove()

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)

print(numbers)


# 16. Practice - pop()

numbers = [10, 20, 30, 40, 50]

numbers.pop(3)

print(numbers)


# 17. Practice - len()

numbers = [10, 20, 30, 40, 50]

print(len(numbers))


# 18. Practice - Numbers Greater Than 25

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number > 25:
        print(number)


# 19. Practice - Find Largest Number

numbers = [10, 45, 23, 89, 12, 67]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)