#################################
# THEORY
###################################
'''

-> Type hints, introduced in Python 3.5(one of the new feature of the language) as a part of the standard library via PEP 484,
-> Allow you to specify the expected type of variable, function parameter, or return value
-> Type hints in Python involve a colon and a type declaration after the first invocation of a name in a namespace
-> Type hinting is a formal solution to statically indicate the type of a value within your Python code

Examples:

name: str = "Captain America"

def greet(name: str) -> str:
    return "Hello, " + name


In terms of style, PEP 8 recommends the following:

    1.Use normal rules for colons, that is, no space before and one space after a colon (text: str).
    2.Use spaces around the = sign when combining an argument annotation with a default value (align: bool = True).
    3.Use spaces around the -> arrow (def headline(...) -> str).


'''

# type hint or annotation with variables : example-1

name: str = "navateja"
age: int = 45
salary: float = 92000.0056
isEmployee: bool = True

print(name, age, salary, isEmployee)


# type hints or annotation with functions : example-2

def greet(name: str) -> str:
    return "Hello, " + name


print(greet('kumar'))

'''
The name: str syntax indicates the name argument should be of type str. 
The -> syntax indicates the greet() function will return a string.
'''


# example-3
def addition(num1: str | int, num2: str | int) -> int | str:
    return num1 + num2


print(addition("hello", "world"))
print(addition(10, 20))


# example-4

def someFunction(var: any) -> any:
    return var

print(someFunction(10))
print(someFunction([0, 20, 30]))


# example-5

def processList(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] + 2
    return nums
print(processList([10,20,30]))


# example -6

def processDictionary(person: dict) -> dict:
    print(person)
    person['age'] = 56
    return person

print(processDictionary({"name": 'navateja', 'age': '1'}))
