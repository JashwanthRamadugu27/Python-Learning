#practice problems of Day_9

car = {"brand": "toyota",
       "model":"fortuner", 
       "year":2024}
print(car)

movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "rating": 8.8
}
print(movie["title"])
print(movie["rating"])

phone = {
    "brand": "Samsung",
    "model": "S24",
    "price": 75000
}
phone["price"]=70000
print(phone)


laptop = {
    "brand": "Dell",
    "ram": "16GB",
    "storage": "512GB"
}
laptop["processor"]="i7"
print(laptop)

employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
}
employee.pop("salary")
print(employee)

book = {
    "title": "Python Basics",
    "author": "John",
    "pages": 250
}
print("author" in book)
print("price" not in book)


cricket = {
    "team": "India",
    "captain": "Rohit",
    "matches": 15,
    "wins": 11
}
for key in cricket:
    print(key)

cricket = {
    "team": "India",
    "captain": "Rohit",
    "matches": 15,
    "wins": 11
}
for value in cricket.values():
    print(value)

marks = {
    "Maths": 85,
    "Physics": 78,
    "Python": 92,
    "SQL": 88
}
for key,values in marks.items():
    print(key,value)

product = {
    "name": "Keyboard",
    "brand": "Logitech",
    "price": 2500
}
print(len(product))
print(product.keys())
print(product.values())
print(product.get("brand"))