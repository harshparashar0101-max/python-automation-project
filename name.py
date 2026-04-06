name = "harsh"
age = 30
is_strudent = True
price = 9.99

print("hello my name is" + name)
print("your age" ,age)
print("are you a student?" , is_strudent)
print("the price is" , price)

x, y , z = 10, 20, 30
print(x)
print(y)

x ,y = y, x
print(x)
print(y)

if age>20:
    print("you are an childern")
if age>30:
    print("you are a young citizen")
if age>40:
    print("you are a adult citizen")

if age>20 and age<30:
    print("you are an childern")

for i in range(1, 6):
        print(i) 

for i in range(1, 11):
     print(f"5 x {i} = {5*i}")

def greet(name):
    print("hello" + name)

greet("harsh")

def add(a, b):
    return a + b

add(5, 10)

def greet_with_message(name, mess="hello"):
    print(mess + name)  

greet_with_message("harsh")

def multiple_ret():
    age1 = 88
    name = "harsh"
    return age1, name

age1, name = multiple_ret()
print(age1, name)

def min_max(number):
     return min(number), max(number)

numbers = [3, 5, 1, 8, 2]
min_value, max_value = min_max(numbers)
print(min_value, max_value)

def calculate_area(num1, num2):
    return num1 * num2

area=calculate_area(5, 10)
print(area)

def fun(is_even):

    if is_even % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

fun(4)
fun(7)


number = [10 , 20 , 30 , 40 , 50]
string = ["hello" , "world" , "python"]
mixed= [10 , "hello" , 20.5 , "world" , True]

print(number[0])
print(string[1])
print(mixed[2])

mixed.append("new item")
print(mixed)

mixed.insert(2, "inserted item")
print(mixed)

print(f"Length of all arrays: {len(number)}, {len(string)}, {len(mixed)}")

person ={

    "name": "harsh",
    "age": 30,
    "city": "new york"
}

print(person["name"]);
print(person["age"]);

person["name"]="gourav"

print(person["name"]);

for key , value in person.items():
    print(f"{key}: {value}")

if "name" in person:
    print("name is present in the dictionary")

test={

"name" : "Harsh",
"age" : 28,
"city" : "Indore",
"hobby" : "coding",
"favourite_food" : "biryani"
}



for key , value in test.items():
    print(f"{key}: {value}")

print(len(test))

print(test.keys())

