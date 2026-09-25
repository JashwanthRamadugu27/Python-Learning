skills = ("python","sql","excel","powerbi")
print(skills)
print(skills[1])
print(skills[3])
print(skills[-2])

numbers=(10,20,30)
numbers[1]=50

marks=(10,20,30)
print(len(marks))

skills = ("python","sql","excel","powerbi")
for skill in skills:
    print(skill)

roommates = "jashu","siddu","vanam"
print(roommates)

data=("python","sql","powerbi")

python,sql,powerbi = data
print(python)
print(sql)  
print(powerbi)

marks= (10,20,30)
print(marks.count(20))

skills = ("Python", "SQL", "Excel", "Python", "PowerBI")
print(skills.index("Python"))

room_members = ("jashu","siddu","vanam")
print("jashu" in room_members) 

room_members = ("jashu","siddu","vanam")
print("siddu"not in room_members) 

class_members = (("Jashu",19),("Mars",19))
print(class_members[0][0])
print(class_members[1][0])

student = ("Jashwanth", 19, "AI&ML", 8.31)
print(student[0])
print(student[1])
print(student[-1])
print(len(student))


marks = (85, 92, 78, 90, 88)
for mark in marks:
    print(mark)

numbers = (10, 20, 10, 30, 10, 40, 20)
print(numbers.count(10))

skills = ("Python", "SQL", "Excel", "PowerBI", "SQL")
print(skills.index("SQL"))

skills = ("Python", "SQL", "Excel", "PowerBI")
print("Python" in skills)
print("java" not in skills)

student = ("Jashwanth", 19, "AI&ML")
Jashwanth , age , branch = student
print(Jashwanth)
print(age)
print(branch)   

students = (
    ("Jashu", 19),
    ("Siddu", 20),
    ("Vanam", 21),
)
print(students[0][1])
print(students[2][1])

student="jashu",19,"single"
print(student)

skills="Python", "SQL", "ML"
print(skills)

skill1,skill2,skill3 = skills
print(skill1)
print(skill2)   
print(skill3)

data = (
    ("Python", 90),
    ("SQL", 85),
    ("ML", 95)
)
count =0 
print(data[0][1])
print(len(data))
print(data.count("Python"))

for item in data :
    if "Python" in item:
        count+=1
print(count)