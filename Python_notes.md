# 🐍 Python Complete Notes 

---

# Day 1 — Python Basics

## 1. Python

### Definition

Python is a **high-level, easy-to-read programming language** used to build software, websites, automation, data analysis, AI, ML, and more.

### Example

```python
print("Hello Python")
```

---

## 2. `print()`

### Definition

`print()` is a **built-in function used to display something on the screen**.

### Syntax

```python
print(value)
```

### Example

```python
print("Hello World")
print(10)
```

### Output

```text
Hello World
10
```

---

## 3. Strings

### Definition

A string is **text written inside single quotes or double quotes**.

### Syntax

```python
" text "
' text '
```

### Example

```python
name = "Jashwanth"
college = 'KGRCET'
```

Both are valid:

```python
"Hello"
'Hello'
```

---

## 4. Comments

### Definition

Comments are **notes written inside the code for humans to understand**. Python does not execute them.

### Syntax

```python
# comment
```

### Example

```python
# This prints my name
print("Jashwanth")
```

---

## 5. Case Sensitivity

### Definition

Python is **case-sensitive**, meaning uppercase and lowercase letters are treated differently.

### Example

```python
name = "Jashwanth"
Name = "Ramadugu"
```

`name` and `Name` are different variables.

---

## 6. Functions

### Definition

A function is a **reusable block of code that performs a specific task**.

### Example

```python
print("Hello")
```

Here, `print()` is a built-in function.

---

## 7. Python Interpreter

### Definition

The Python interpreter **reads and executes Python code**.

Example:

```python
print("Hello")
print("Python")
```

The interpreter executes the code and produces the output.

---

# Day 2 — Variables & Data Types

## 1. Variable

### Definition

A variable is a **name used to store a value**.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Jashwanth"
age = 19
cgpa = 8.31
```

---

## 2. Reassigning a Variable

### Definition

A variable's value can be **changed by assigning a new value to it**.

### Example

```python
age = 19
age = 20

print(age)
```

### Output

```text
20
```

---

# Data Types

## 3. Integer — `int`

### Definition

An integer is a **whole number without a decimal point**.

### Example

```python
age = 19
marks = 95
```

---

## 4. Float — `float`

### Definition

A float is a **number containing a decimal point**.

### Example

```python
cgpa = 8.31
price = 99.50
```

---

## 5. String — `str`

### Definition

A string is **text enclosed inside quotes**.

### Example

```python
name = "Jashwanth"
college = "KGRCET"
```

---

## 6. Boolean — `bool`

### Definition

Boolean represents one of two values:

* `True`
* `False`

### Example

```python
is_student = True
is_working = False
```

---

## 7. `type()`

### Definition

`type()` is used to **find the data type of a value or variable**.

### Syntax

```python
type(value)
```

### Example

```python
age = 19
print(type(age))
```

### Output

```text
<class 'int'>
```

---

# Type Conversion

## 8. Type Conversion

### Definition

Type conversion means **changing one data type into another data type**.

---

## `int()`

### Definition

Converts a value into an integer.

### Example

```python
age = "19"
age = int(age)

print(age)
```

---

## `float()`

### Definition

Converts a value into a float.

### Example

```python
number = "10"
number = float(number)

print(number)
```

---

## `str()`

### Definition

Converts a value into a string.

### Example

```python
age = 19
age = str(age)

print(age)
```

---

## `bool()`

### Definition

Converts a value into a Boolean value.

### Example

```python
value = 1
print(bool(value))
```

### Output

```text
True
```

---

# Day 3 — Conditions

## 1. Condition

### Definition

A condition is used to **make a decision in a program based on whether something is True or False**.

---

## 2. Comparison Operators

### Definition

Comparison operators are used to **compare two values**.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 19

print(age >= 18)
```

### Output

```text
True
```

---

# 3. `if`

### Definition

`if` executes a block of code **when a condition is True**.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 19

if age >= 18:
    print("Eligible")
```

---

# 4. `if-else`

### Definition

`if-else` is used when there are **two possible situations**.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 17

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# 5. `if-elif-else`

### Definition

It is used when we need to **check multiple conditions**.

### Syntax

```python
if condition:
    statement
elif condition:
    statement
else:
    statement
```

### Example

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

---

# 6. Logical Operators

### Definition

Logical operators are used to **combine multiple conditions**.

### `and`

Both conditions must be True.

```python
age = 19
cgpa = 8.31

if age >= 18 and cgpa >= 7:
    print("Eligible")
```

---

### `or`

At least one condition must be True.

```python
age = 17

if age >= 18 or age == 17:
    print("Condition satisfied")
```

---

### `not`

Reverses the result.

```python
is_student = True

if not is_student:
    print("Not a student")
```

---

# 7. Nested `if`

### Definition

An `if` statement written **inside another `if` statement** is called a nested `if`.

### Example

```python
age = 19
cgpa = 8.31

if age >= 18:
    if cgpa >= 7:
        print("Eligible")
```

---

# Day 4 — Loops

## 1. Loop

### Definition

A loop is used to **repeat a block of code multiple times**.

Python has two loops that you learned:

* `for`
* `while`

---

# 2. `for` Loop

### Definition

A `for` loop is used to **repeat code for each item in a sequence or range**.

### Syntax

```python
for variable in sequence:
    statement
```

### Example

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

---

# 3. `range()`

### Definition

`range()` generates a **sequence of numbers**.

### Syntax

```python
range(start, stop, step)
```

The `stop` value is **not included**.

### Example

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## `range(start, stop)`

```python
range(1, 6)
```

Generates:

```text
1 2 3 4 5
```

---

## `range(start, stop, step)`

```python
range(2, 11, 2)
```

Generates:

```text
2 4 6 8 10
```

---

## Negative Step

Used for counting backwards.

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
...
1
```

---

# 4. `while` Loop

### Definition

A `while` loop **keeps running as long as its condition is True**.

### Syntax

```python
while condition:
    statement
```

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 5. `break`

### Definition

`break` is used to **immediately stop a loop**.

### Example

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

# 6. `continue`

### Definition

`continue` **skips the current iteration and moves to the next iteration**.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

---

# 7. Modulo Operator `%`

### Definition

`%` gives the **remainder after division**.

### Example

```python
10 % 3
```

Output:

```text
1
```

### Common use

Checking even numbers:

```python
if number % 2 == 0:
    print("Even")
```

Checking multiples of 4:

```python
if number % 4 == 0:
    print("Multiple of 4")
```

---

# 8. Accumulator

### Definition

An accumulator is a variable used to **keep adding or collecting values while a loop runs**.

### Example

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```text
15
```

---

# 9. Finding the Largest Number

### Example

```python
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output:

```text
89
```

---

# Day 5 — Lists

## 1. List

### Definition

A list is used to **store multiple values in a single variable**.

Lists can contain different types of data.

### Syntax

```python
list_name = [item1, item2, item3]
```

### Example

```python
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
```

---

# 2. List Indexing

### Definition

Indexing is used to **access individual items from a list**.

Python indexing starts from **0**.

### Example

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

# 3. Negative Indexing

### Definition

Negative indexing is used to **access items from the end of a list**.

```text
-1 → last item
-2 → second last item
```

### Example

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

---

# 4. Changing List Items

### Definition

Lists are **mutable**, meaning their items can be changed after the list is created.

### Syntax

```python
list[index] = new_value
```

### Example

```python
marks = [80, 90, 70]

marks[2] = 100

print(marks)
```

Output:

```text
[80, 90, 100]
```

---

# 5. `append()`

### Definition

`append()` adds an item **to the end of a list**.

### Syntax

```python
list.append(value)
```

### Example

```python
fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

---

# 6. `insert()`

### Definition

`insert()` adds an item **at a specific index**.

### Syntax

```python
list.insert(index, value)
```

### Example

```python
fruits = ["apple", "banana"]

fruits.insert(1, "mango")

print(fruits)
```

Output:

```text
['apple', 'mango', 'banana']
```

---

# 7. `remove()`

### Definition

`remove()` removes an item **using its value**.

### Syntax

```python
list.remove(value)
```

### Example

```python
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)
```

Output:

```text
['apple', 'mango']
```

---

# 8. `pop()`

### Definition

`pop()` removes an item **using its index**.

### Syntax

```python
list.pop(index)
```

### Example

```python
numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)
```

Output:

```text
[10, 30, 40]
```

### Without an index

```python
numbers.pop()
```

removes the **last item**.

---

# 9. `len()`

### Definition

`len()` returns the **number of items in a list**.

### Syntax

```python
len(list)
```

### Example

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

---

# 10. Looping Through a List

### Definition

A loop can be used to **access each item in a list one by one**.

### Example

```python
marks = [80, 90, 70]

for mark in marks:
    print(mark)
```

Output:

```text
80
90
70
```

---

# Day 6 — Strings

## 1. String

### Definition

A string is **a sequence of characters enclosed inside single or double quotes**.

### Example

```python
name = "Jashwanth"
college = "KGRCET"
```

---

# 2. String Indexing

### Definition

String indexing is used to **access individual characters from a string**.

Indexing starts from `0`.

### Example

```python
name = "Jashwanth"

print(name[4])
```

Output:

```text
w
```

---

# 3. Negative Indexing in Strings

### Definition

Negative indexing is used to **access characters from the end of a string**.

### Example

```python
name = "Jashwanth"

print(name[-1])
print(name[-2])
```

Output:

```text
h
t
```

---

# 4. String Slicing

### Definition

Slicing is used to **extract a part of a string**.

### Syntax

```python
string[start:end]
```

The `end` index is **not included**.

### Example

```python
name = "Jashwanth"

print(name[0:4])
```

Output:

```text
Jash
```

---

## Other Slicing Forms

### From an index to the end

```python
print(name[4:])
```

Output:

```text
wanth
```

### From the beginning to an index

```python
print(name[:4])
```

Output:

```text
Jash
```

---

# 5. `len()` with Strings

### Definition

`len()` returns the **number of characters in a string**.

### Example

```python
college = "kgrcet"

print(len(college))
```

Output:

```text
6
```

---

# 6. `upper()`

### Definition

`upper()` converts all letters in a string to **uppercase**.

### Syntax

```python
string.upper()
```

### Example

```python
college = "kgrcet"

print(college.upper())
```

Output:

```text
KGRCET
```

---

# 7. `lower()`

### Definition

`lower()` converts all letters in a string to **lowercase**.

### Syntax

```python
string.lower()
```

### Example

```python
name = "JASHWANTH"

print(name.lower())
```

Output:

```text
jashwanth
```

---

# 8. `strip()`

### Definition

`strip()` removes **spaces from the beginning and end of a string**.

It does not remove spaces between words.

### Syntax

```python
string.strip()
```

### Example

```python
name = "   Jashwanth   "

print(name.strip())
```

Output:

```text
Jashwanth
```

---

# 9. `replace()`

### Definition

`replace()` is used to **replace one part of a string with another**.

### Syntax

```python
string.replace(old, new)
```

### Example

```python
college = "KG Reddy College"

print(college.replace("College", "University"))
```

Output:

```text
KG Reddy University
```

### Important

`replace()` returns a **new string**. It does not change the original string unless you assign it back.

```python
college = college.replace("College", "University")
```

---

# 10. `split()`

### Definition

`split()` breaks a string into **multiple parts and returns them as a list**.

### Syntax

```python
string.split()
```

### Example

```python
skills = "Python SQL Excel PowerBI"

print(skills.split())
```

Output:

```text
['Python', 'SQL', 'Excel', 'PowerBI']
```

---

# 11. Looping Through a String

### Definition

A loop can be used to **access each character in a string one by one**.

### Example

```python
word = "Python"

for character in word:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

---

# 12. `in`

### Definition

`in` checks whether a **value or character exists inside a string or collection**.

### Example

```python
word = "Python"

print("y" in word)
```

Output:

```text
True
```

---

# 13. `not in`

### Definition

`not in` checks whether a **value or character does not exist**.

### Example

```python
word = "Python"

print("z" not in word)
```

Output:

```text
True
```

---

# 14. `startswith()`

### Definition

`startswith()` checks whether a string **starts with a specific value**.

### Syntax

```python
string.startswith(value)
```

### Example

```python
word = "Python"

print(word.startswith("Py"))
```

Output:

```text
True
```

---

# 15. `endswith()`

### Definition

`endswith()` checks whether a string **ends with a specific value**.

### Syntax

```python
string.endswith(value)
```

### Example

```python
word = "Python"

print(word.endswith("on"))
```

Output:

```text
True
```

---

# 16. String Case Sensitivity

### Definition

Python strings are **case-sensitive**, so uppercase and lowercase characters are different.

### Example

```python
word = "Python"

print(word.startswith("Py"))
print(word.startswith("py"))
```

Output:

```text
True
False
```

---

# 17. Counting a Character

### Definition

We can use a loop and a counter to **count how many times a particular character appears**.

### Example

```python
word = "banana"

count = 0

for character in word:
    if character == "a":
        count += 1

print(count)
```

### Output

```text
3
```

### Important pattern

```python
count = 0

for character in word:
    if character == "a":
        count += 1
```

This pattern is useful for many counting problems.

# Day 7 — Tuples

## 1. Tuple

### Definition

A tuple is an ordered collection of multiple values.

Tuples are **immutable**, meaning their values cannot be changed after creation.

### Syntax

```python
tuple_name = (item1, item2, item3)
```

### Example

```python
skills = ("Python", "SQL", "ML")

print(skills)
```

### Output

```text
('Python', 'SQL', 'ML')
```

---

# 2. Tuple Indexing

### Definition

Indexing is used to access individual items from a tuple.

Python indexing starts from `0`.

### Example

```python
skills = ("Python", "SQL", "ML")

print(skills[0])
print(skills[1])
```

### Output

```text
Python
SQL
```

---

# 3. Negative Indexing

### Definition

Negative indexing is used to access items from the end of a tuple.

```text
-1 → last item
-2 → second last item
```

### Example

```python
skills = ("Python", "SQL", "ML")

print(skills[-1])
print(skills[-2])
```

### Output

```text
ML
SQL
```

---

# 4. Tuple Immutability

### Definition

Tuples are immutable, meaning their values cannot be changed after creation.

### Example

```python
numbers = (10, 20, 30)

numbers[1] = 50
```

### Output

```text
TypeError
```

A tuple does not support changing individual items.

---

# 5. `len()` with Tuples

### Definition

`len()` returns the total number of items in a tuple.

### Syntax

```python
len(tuple)
```

### Example

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

### Output

```text
4
```

---

# 6. Looping Through a Tuple

### Definition

A loop can be used to access each item in a tuple one by one.

### Example

```python
skills = ("Python", "SQL", "ML")

for skill in skills:
    print(skill)
```

### Output

```text
Python
SQL
ML
```

---

# 7. Tuple Packing

### Definition

Putting multiple values together into a tuple is called tuple packing.

### Example

```python
student = "Jashwanth", 19, 8.31

print(student)
```

### Output

```text
('Jashwanth', 19, 8.31)
```

Parentheses are optional when creating a tuple through packing.

---

# 8. Single-Item Tuple

### Definition

A comma is required to create a tuple containing only one item.

### Example

```python
data = ("Python",)

print(type(data))
```

### Output

```text
<class 'tuple'>
```

Without the comma:

```python
data = ("Python")
```

This is a string, not a tuple.

---

# 9. Tuple Unpacking

### Definition

Taking values from a tuple and assigning them to separate variables is called tuple unpacking.

### Example

```python
data = ("Python", "SQL", "ML")

python, sql, ml = data

print(python)
print(sql)
print(ml)
```

### Output

```text
Python
SQL
ML
```

The position of each value determines which variable receives it.

---

# 10. `count()`

### Definition

`count()` returns how many times a specific value appears in a tuple.

### Syntax

```python
tuple.count(value)
```

### Example

```python
marks = (90, 85, 90, 95)

print(marks.count(90))
```

### Output

```text
2
```

---

# 11. `index()`

### Definition

`index()` returns the index of the first occurrence of a value.

### Syntax

```python
tuple.index(value)
```

### Example

```python
skills = ("Python", "SQL", "ML")

print(skills.index("SQL"))
```

### Output

```text
1
```

---

# 12. `in`

### Definition

`in` checks whether a value exists inside a tuple.

### Example

```python
skills = ("Python", "SQL", "ML")

print("Python" in skills)
```

### Output

```text
True
```

---

# 13. `not in`

### Definition

`not in` checks whether a value does not exist inside a tuple.

### Example

```python
skills = ("Python", "SQL", "ML")

print("Java" not in skills)
```

### Output

```text
True
```

---

# 14. Nested Tuples

### Definition

A tuple containing other tuples is called a nested tuple.

### Example

```python
students = (
    ("Jashu", 19),
    ("Siddu", 20),
    ("Vanam", 21)
)
```

### Accessing Nested Values

```python
print(students[0][0])
print(students[0][1])
```

### Output

```text
Jashu
19
```

---

# 15. Searching Inside Nested Tuples

### Definition

A loop can be used to search for a value inside nested tuples.

### Example

```python
data = (
    ("Python", 90),
    ("SQL", 85),
    ("ML", 95)
)

count = 0

for item in data:
    if "Python" in item:
        count += 1

print(count)
```

### Output

```text
1
```

Here, `item` represents each inner tuple.

---

# 16. List vs Tuple

| List                     | Tuple               |
| ------------------------ | ------------------- |
| `[]`                     | `()`                |
| Mutable                  | Immutable           |
| Can be changed           | Cannot be changed   |
| More flexible            | More fixed          |
| Used for changeable data | Used for fixed data |

# Day 8 — Sets

## 1. What is a Set?

### Definition

A **set** is a collection of values that:

* Does not allow duplicate values.
* Is unordered.
* Can be changed after creation.

### Syntax

```python
skills = {"Python", "SQL", "ML"}
```

### Example

```python
numbers = {10, 20, 30, 20, 10}
print(numbers)
```

### Output

```text
{10, 20, 30}
```

Duplicate values are automatically removed.

---

## 2. Set vs List vs Tuple

| Type  | Brackets | Ordered             | Duplicates  | Mutable |
| ----- | -------- | ------------------- | ----------- | ------- |
| List  | `[]`     | Yes                 | Allowed     | Yes     |
| Tuple | `()`     | Yes                 | Allowed     | No      |
| Set   | `{}`     | No guaranteed order | Not allowed | Yes     |

---

## 3. Creating a Set

### Directly

```python
fruits = {"apple", "banana", "mango"}
```

### From a List

```python
fruits = ["apple", "banana", "apple"]
fruits = set(fruits)
print(fruits)
```

### Output

```text
{'apple', 'banana'}
```

---

## 4. Adding Items

Use `add()`.

```python
skills = {"Python", "SQL"}

skills.add("PowerBI")

print(skills)
```

The new item is added to the set.

---

## 5. Removing Items

### `remove()`

```python
skills = {"Python", "SQL", "ML"}

skills.remove("SQL")
print(skills)
```

Removes the specified item.

If the item does not exist, `remove()` gives an error.

### `discard()`

```python
skills.discard("Java")
```

Removes the item if it exists. If it doesn't exist, no error occurs.

### `pop()`

```python
skills = {"Python", "SQL", "ML"}

skills.pop()
```

Removes and returns an arbitrary item because sets are unordered.

---

## 6. `in` / `not in`

```python
skills = {"Python", "SQL", "ML"}

print("Python" in skills)
print("Java" not in skills)
```

### Output

```text
True
True
```

---

## 7. `len()` with Sets

```python
numbers = {10, 20, 30, 20, 40, 10}

print(len(numbers))
```

### Output

```text
4
```

`len()` counts the unique items in the set.

---

## 8. Looping Through a Set

```python
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
```

The order of output is not guaranteed.

---

## 9. Union `|`

### Definition

Union combines values from both sets and removes duplicates.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

## 10. Intersection `&`

### Definition

Intersection gives the values that are common in both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
```

### Output

```text
{3}
```

---

## 11. Difference `-`

### Definition

Difference gives the values that are in the first set but not in the second set.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
```

### Output

```text
{1, 2}
```

`b - a` would give `{4, 5}`.

---

## 12. Symmetric Difference `^`

### Definition

Gives values that are present in **only one** of the two sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
```

### Output

```text
{1, 2, 4, 5}
```

### Quick Revision

```text
|  → Union → Everything from both
&  → Intersection → Common values
-  → Difference → First set only
^  → Symmetric difference → Only one side
```

# Day 9 — Dictionaries

## 1. What is a Dictionary?

### Definition

A **dictionary** stores data in **key-value pairs**.

```text
Key → Value
```

### Syntax

```python
student = {
    "name": "Jashwanth",
    "age": 19
}
```

Here:

* `"name"` → key
* `"Jashwanth"` → value
* `"age"` → key
* `19` → value

---

## 2. Creating a Dictionary

### Using `{}`

```python
student = {
    "name": "Jashwanth",
    "age": 19
}
```

### Empty Dictionary

```python
student = {}
```

### Using `dict()`

```python
student = dict(name="Jashwanth", age=19)
```

---

## 3. Key-Value Pairs

Each dictionary item follows:

```python
key : value
```

Example:

```python
student = {
    "name": "Jashwanth",
    "age": 19,
    "cgpa": 8.31
}
```

Keys should normally be unique.

---

## 4. Accessing Values Using Keys

Unlike lists and tuples, dictionaries use **keys instead of indexes**.

```python
student = {
    "name": "Jashwanth",
    "age": 19
}

print(student["name"])
print(student["age"])
```

### Output

```text
Jashwanth
19
```

---

## 5. Adding Items

If the key does not exist, a new item is added.

```python
student = {
    "name": "Jashwanth",
    "age": 19
}

student["cgpa"] = 8.31

print(student)
```

---

## 6. Updating Values

If the key already exists, its value is updated.

```python
student["age"] = 20
```

The old value is replaced.

### Important

```python
dictionary["key"] = value
```

* Existing key → update
* New key → add

---

## 7. Removing Items

### `pop()`

```python
student.pop("age")
```

Removes the item with the specified key.

### `del`

```python
del student["cgpa"]
```

Deletes the specified item.

### `clear()`

```python
student.clear()
```

Removes all items.

The dictionary becomes:

```text
{}
```

---

## 8. `in` / `not in`

In dictionaries, `in` and `not in` check **keys** by default.

```python
student = {
    "name": "Jashwanth",
    "age": 19
}

print("name" in student)
print("phone" not in student)
```

### Output

```text
True
True
```

It checks keys, not values.

---

## 9. Looping Through Dictionary Keys

```python
student = {
    "name": "Jashwanth",
    "age": 19,
    "cgpa": 8.31
}

for key in student:
    print(key)
```

This prints all the keys.

---

## 10. Looping Through Dictionary Values

Use `values()`.

```python
for value in student.values():
    print(value)
```

This prints all the values.

---

## 11. Looping Through Keys and Values

Use `items()`.

```python
for key, value in student.items():
    print(key, value)
```

This prints both the key and its value.

---

## 12. `len()`

`len()` counts the number of **key-value pairs**.

```python
student = {
    "name": "Jashwanth",
    "age": 19,
    "cgpa": 8.31
}

print(len(student))
```

### Output

```text
3
```

---

## 13. `keys()`

Returns all the keys.

```python
print(student.keys())
```

---

## 14. `values()`

Returns all the values.

```python
print(student.values())
```

---

## 15. `items()`

Returns both keys and values.

```python
print(student.items())
```

It is commonly used with loops:

```python
for key, value in student.items():
    print(key, value)
```

---

## 16. `get()`

Used to safely access a value using a key.

```python
print(student.get("name"))
```


Day 10 — Functions
1. What is a Function?
Definition

A function is a reusable block of code used to perform a specific task.

Syntax
def function_name():
    # code
Example
def greet():
    print("Hello")

greet()
2. Creating and Calling a Function

A function is created using def and called using its name.

def welcome():
    print("Welcome to Python")

welcome()
Output
Welcome to Python
3. Parameters

A parameter is a variable written inside the function definition.

Syntax
def function_name(parameter):
    # code
Example
def greet(name):
    print("Hello", name)

greet("Jashwanth")

Here, name is the parameter.

4. Arguments

An argument is the actual value passed to a function.

def greet(name):
    print("Hello", name)

greet("Jashwanth")

Here:

name → parameter
"Jashwanth" → argument
5. Multiple Parameters

A function can have multiple parameters.

Syntax
def function_name(parameter1, parameter2):
    # code
Example
def add(a, b):
    print(a + b)

add(10, 20)
Output
30
6. return

return sends a value back from the function.

Syntax
def function_name():
    return value
Example
def add(a, b):
    return a + b

answer = add(10, 20)
print(answer)
Output
30
7. print() vs return
print()

Displays the result.

def add(a, b):
    print(a + b)
return

Sends the result back so we can store or use it.

def add(a, b):
    return a + b

result = add(10, 20)
8. Default Parameters

A default parameter has a value that is used when no argument is given.

Syntax
def function_name(parameter="default"):
    # code
Example
def greet(name="Jashwanth"):
    print("Hello", name)

greet()
Output
Hello Jashwanth

If we give an argument, it replaces the default value.

greet("Rahul")
Output
Hello Rahul
Quick Revision
def        → creates a function
call       → runs the function
parameter  → variable inside the function
argument   → value passed to the function
return     → sends a value back
default    → value used when no argument is given



