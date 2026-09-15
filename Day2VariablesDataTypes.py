# DAY 02 - VARIABLES, DATA TYPES & TYPE CONVERSION


# Variables

name = "Jashwanth"
age = 19
goal = "ML Engineer"

print(name)
print(age)
print(goal)

age = 19
print(age)

age = 20
print(age)


# Variable Practice

Jashwanth_CGPA = 8.29
print(Jashwanth_CGPA)

Jashwanth_CGPA = 8.31
print(Jashwanth_CGPA)


# int

Age_Details = "Family members"

Nagendra_prasad_Ramadugu = 50
Swapna_Ramadugu = 45
Jashwanth_Ramadugu = 19
Rakshith_Ramadugu = 15
Srilakshmi = 80

print(type(Jashwanth_Ramadugu))
print(type(Rakshith_Ramadugu))


# float

SGPA = "my_classmates"

jashwanth = 8.54
Rajesh = 8.29
Burdak = 7.5
Charan = 7.0
Pandey = 7.5
Mariya = 9.91
Naazima = 9.54
Sushma = 9.35

print(type(jashwanth))


# str

content = "profile"
Name = "Jashwanth Ramadugu"
Specialization = "AI&ML"
Skills = "python , sql , excel , powerbi"
Goal = "to become ML Engineer/Data Analyst"

print(type(Name))
print(type(Goal))


# bool

identifying_toppers_in_class = "True or false"

jashwanth = False
Rajesh = True
Rahul = True
Pandey = True
Charan = True
Manikanta = False

print(type(jashwanth))
print(type(Manikanta))


# type()

age = 19
CGPA = 8.31
Name = "Jashwanth"
Is_topper = False

print(type(age))
print(type(Name))
print(type(Is_topper))
print(type(CGPA))


# Type Conversion - int()

age = "69"

print(type(age))

age = int(age)

print(type(age))


# Type Conversion - float()

Sgpa = "8.31"

print(type(Sgpa))

Sgpa = float(Sgpa)

print(type(Sgpa))


# Type Conversion - str()

cgpa = 8.31

print(type(cgpa))

cgpa = str(cgpa)

print(type(cgpa))


# Type Conversion - bool()

cgpa = 8.31

print(type(cgpa))

cgpa = bool(cgpa)

print(type(cgpa))
print(cgpa)


# Final Challenge

name = "jashwanth"

age = "19"

cgpa = "8.31"

topper = False

age = int(age)

print(type(age))

cgpa = float(cgpa)

print(type(cgpa))

topper = str(topper)

print(type(topper))

age = age + 1

print(age)