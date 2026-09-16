# Day 3 - Conditions and Decision Making
# Python Learning Journey


# --------------------------------------------------
# 1. Comparison Operators
# --------------------------------------------------

age = 19

print(age > 18)
print(age < 18)
print(age == 19)
print(age != 19)


cgpa = 8.31

print(cgpa > 8)
print(cgpa < 8)
print(cgpa >= 8.31)
print(cgpa <= 8)
print(cgpa == 8.31)
print(cgpa != 8.31)


# --------------------------------------------------
# 2. if Statement
# --------------------------------------------------

age = 19

if age >= 18:
    print("You are an adult")


# --------------------------------------------------
# 3. if-else
# --------------------------------------------------

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# --------------------------------------------------
# 4. if-elif-else
# --------------------------------------------------

cgpa = 8.31

if cgpa >= 9:
    print("Excellent")
elif cgpa >= 8:
    print("Good")
elif cgpa >= 7:
    print("Average")
else:
    print("Need Improvement")


# --------------------------------------------------
# 5. Logical Operators - and
# --------------------------------------------------

age = 17
cgpa = 8.5

if age >= 18 and cgpa >= 8:
    print("Eligible")
else:
    print("Not Eligible")


# --------------------------------------------------
# 6. Logical Operator - or
# --------------------------------------------------

age = 17
cgpa = 8.5

if age >= 18 or cgpa >= 8:
    print("Eligible")
else:
    print("Not Eligible")


# --------------------------------------------------
# 7. Logical Operator - not
# --------------------------------------------------

is_raining = False

if not is_raining:
    print("Go outside")


# --------------------------------------------------
# 8. Nested if - Login System
# --------------------------------------------------

username = "jashwanth"
password = "python123"

if username == "jashwanth":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


# --------------------------------------------------
# 9. Nested if - ATM Withdrawal
# --------------------------------------------------

balance = 5000
withdraw_amount = 3000
pin_correct = True

if pin_correct == True:
    if withdraw_amount <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")


# --------------------------------------------------
# 10. Nested if - College Library
# --------------------------------------------------

student_id_valid = True
book_available = False

if student_id_valid == True:
    if book_available == True:
        print("Book issued successfully")
    else:
        print("Book is currently unavailable")
else:
    print("Invalid student ID")


# --------------------------------------------------
# 11. Scholarship Eligibility
# --------------------------------------------------

cgpa = 8.5
family_income = 250000

if cgpa >= 8.5 and family_income <= 300000:
    print("Scholarship Approved")
elif cgpa >= 7.5 and family_income <= 500000:
    print("Partial Scholarship")
else:
    print("Not Eligible")


# --------------------------------------------------
# 12. Number Analyzer
# --------------------------------------------------

number = -7

if number == 0:
    print("Zero")

elif number > 0 and number % 2 == 0:
    print("Positive Even")

elif number > 0:
    print("Positive Odd")

elif number < 0 and number % 2 == 0:
    print("Negative Even")

else:
    print("Negative Odd")


# --------------------------------------------------
# 13. College Exam Eligibility
# --------------------------------------------------

attendance = 82
cgpa = 7.8
medical_certificate = False

if attendance >= 75:
    if cgpa >= 7.0:
        print("Eligible for exam")
    else:
        print("CGPA too low")
elif attendance < 75:
    if medical_certificate == True:
        print("Eligible with medical exception")
    else:
        print("Not eligible")