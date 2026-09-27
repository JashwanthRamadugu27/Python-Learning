numbers = {1,2,3,4,5,6,7,8,9,10}
print(numbers)

numbers = {10, 20, 30, 20, 40, 10}
print(numbers)

fruits = ["apple", "banana", "apple", "mango", "banana"]
unique_fruits = set(fruits)
print(unique_fruits)

skills={"python","sql"}
skills.add("powerbi")
print(skills)

skills = {"Python", "SQL", "PowerBI", "ML"}
skills.remove("SQL")
print(skills)

skills = {"Python", "SQL", "PowerBI"}
skills.discard("Java")
print(skills)

skills = {"Python", "SQL", "PowerBI"}
skills.pop()
print(skills)

removed = skills.pop()
print(removed)
print(skills)

students = {"Jashu", "Siddu", "Vanam"}
print("Jashu" in students)
print("mars" not in students)

students = {"Jashu", "Siddu", "Vanam"}
print(len(students))

numbers = {10, 20, 30, 40, 50}
for number in numbers:
    print(number)

kgrcet ={"jashu","froz"}
jbrec={"siddu","vanam"}
result= kgrcet|jbrec
print(result)

kgrcet ={"jashu","froz","siddu"}
jbrec={"siddu","vanam"}
result= kgrcet&jbrec
print(result)

kgrcet ={"jashu","froz","siddu"}
jbrec={"siddu","vanam"}
print(kgrcet-jbrec)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a ^ b)

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a | b)
print(a & b)
print(a - b)

#practice probelms 

numbers = {10, 20, 30, 20, 40, 10, 50}
print(len(numbers))

skills = {"Python", "SQL", "PowerBI"}
skills.add("ML")
skills.remove("SQL")
print(skills)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
result=a|b
print(result)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
result = a&b
print(result)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a-b)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a^b)

students = {"Jashu", "Siddu", "Vanam", "Mars"}
print("Jashu" in students)
print("ravi" not in students)

numbers = {10, 20, 30, 40, 50}
for number in numbers:
    if number>25:
        print(number)

a = {10, 20, 30}
b = {30, 40, 50}
result = a|b
print(result)
print(a-b)
result=a&b
print(result)

skills = {"Python", "SQL", "Python", "ML", "SQL", "Excel"}
print(skills)