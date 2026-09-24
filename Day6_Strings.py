name="Jashwanth"
print(name)
print(len(name))
print(name[0])
print(name[-1])

word="programming"
print(word[-1])
print(word[-2])
print(word[-3])

word="pythonprogramming"
print(word[0:6])
print(word[6:17])
print(word[6:])

sentence = "Python is easy"
print(sentence)
print(len(sentence))

name = "Jashwanth"
print(name.upper())
print(name.lower())

name = "   Jashwanth   "
print(name.strip())

college = "KG Reddy College"
print(college.replace("College","University"))
college=college.replace("College","University")

skills = "Python SQL Excel PowerBI"
print(skills.split())

word = "Python"
for character in word:
    print(character)  

word = "Python"
print("y" in word)  
print("jash" not in word)

word = "Python"
print(word.startswith("Py"))
print(word.endswith("on"))

word = "banana"
count=0
for character in word:
    if character=="a":
        count+=1
print(count)


