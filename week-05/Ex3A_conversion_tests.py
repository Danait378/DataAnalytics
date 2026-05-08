# description: this script tests various numeric
#conversion techniques
# author: Sam Q. Newprogrammer

a = "101.1" 
b = "55"
c = "402 stevens"
d = " Number 5 "

# integer conversions
# a_int = int(a) # valueError
b_int = int(b)
# c_int = int(c) # valueError
# d_int = int(d) # valueError

# float conversions
a_float = float(a)
b_float = float (b)
# c_float = float(c) # valueError
# d_float = float(d) # valueError

# float to integer
a_float_int = int(float(a))

#slicing numeric portions
c_number = int(c[0:3])

d_number = d[-2]

# using strip()
print(a.strip())
print(d.strip())

# print values and types
print(a,type(a))
print(b_int, type(b_int))