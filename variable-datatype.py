a = 200      # a is a integer

b = 71.22     # b is a floating point number

c = "sneha"    # c is a string

d = False     # d is boolean variable

e = None      # is a non type vairable


# 1) basic

a = 10

b = "sneha"

c = 3.9

print( a, b ,c)





# 2) Multiple Assignment

a, b, c = 10, "sneha", 3.9
print(a)
print(b)
print(c)






#3.1) checking data type

a = 10

b = "sneha"

c = 3.9

print(type(a))
print(type(b))
print(type(c))
  

# 2)

a, b, c = 10, "sneha", 3.9
print(type(a))
print(type(b))
print(type(c))
   




# 4) swaping

a = 10

b = 30

a, b = b, a
print(a , b)





# 5) Type Conversion
a = "100"

b = 50

c = 0.5
print(int(a) + b)
print(float(a) + c)
print(b + int(a))



# 6) Integer (int)

age = 100

print(age)
print(type(age))




# 7) Float (float)

rs = 99.99
print(rs)
print(type(rs))



# 8) string

name = "Sneha"

print(name)
print(type(name))



# 9) Boolean (bool)

is_student = True

print(is_student)
print(type(is_student))


# 10) List (list)


fruits = ["apple", "banana", "grapes", "orange"]
print(fruits)
print(type(fruits))


# 11) Tuple (tuple)
numbers= (1, 2, 3)                       
print(numbers)
print(type(numbers))


# 12) Dictionary (dict)

student =  {"name": "sneha" , "age": "21"}  
print(student)
print(type(student))


# 13) Set (set)

numbers = {1, 2, 3}
print(numbers)
print(type(numbers))



# 14) multiply

a = 3

b = 2

c = a * b

print(c)
print(type(c))


# 15) set trick

nu = [1, 2, 3, 2, 4, 4, 5]

nums = list(set(nu))                  #remove repeted numbers

print(nums)


# 16) (List Length)

fruits = ["apple", "banana", "mango", "grapes"]

length = len(fruits)                  #Find length of list

print(length)




# 17) Remove duplicates using set   and # Count unique values

numbers = [ 1, 1, 2, 2, 4, 4, 5]
nums = list(set(numbers))
print(len(nums))




# 18)Dictionary Access
data = { "name": "sneha", "age":21}
print(data["age"])











