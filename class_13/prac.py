# / is for float division, it will give you a float result even if both numbers are integers
# // is for integer division, it will give you an integer result even if both numbers are floats

# For example:
print(5 // 2)  # Output: 2
print(5 / 2)   # Output: 2.5


# Complex number:
x = 4 + 3j
z = 3 + 7j

print(z - x)


# Round method: ka matlab hai ki aap kisi number ko kitne decimal places tak round karna chahte hain.

print(round(3.14159, 2))  # Output: 3.14

print(0.1 + 0.2)  # Output: 0.30000000000000004
print(round(0.1 + 0.2, 2))  # Output: 0.3



# # Strings are immutable, which means that you cannot change a string after it has been created. If you try to change a string, you will get an error.
my_message = "Hello, World!"
# str_chg = my_message[0] = "h"
# print(str_chg)

my_message = "don't worry, be happy"
print(my_message) # its created a new string and assigned it to the variable my_message, it did not change the original string "Hello, World!".



# # Bool:
print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool([]))  # Output: False
print(bool([1, 2, 3]))  # Output: True
print(bool(None))  # Output: False
print(bool(0.0))  # Output: False
print(bool({})) # Output: False
print("-=-=", bool(- 0.0))  # Output: False



a : None = None
b : None = None

print(a == b)  # Output: True
print(id(a))  # Output: 140736799863936 (example memory address)
print(id(b))  # Output: 140736799863936 (same memory address as a)
print(id(a) == id(b))  # Output: True (both a and b point to the same memory address)

x: int = 23

y: int = 23

y = 32 # y is now pointing to a different memory address where the value 32 is stored
# x is still pointing to the memory address where the value 23 is stored
# y = 23 # if we change y back to 23, it will point to the same memory address as x again


print(x == y)  # Output: True
print(id(x))  # Output: 140736799863936 (example memory address)
print(id(y))  # Output: 140736799863936 (same memory address as x)
print(id(x) == id(y))  # Output: True (both x and y point