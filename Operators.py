#Airthmetic operators 
a = 24 
b  = 55 
print(a+b)
print(a-b)
print(a*b)
print(a/b)



# Modulus operators
a1 = 23 % 5
print(a1)

b2 = 22**2 #(power of 22 )
print(b2)



#floor operators
#(bringing the value on lower side if output is 3.33 then it will show 3 ) (//)
print(4//3) 
print(10//3)
print(10/3)  # show the difference 



#Comparision operators     (compare to values )
a = 10 
b = 5
print(a == b )
print(a != b ) 
print(a < b )   
print(a > b )
print(a <= b )
print(a >= b )



#Logical operators

#and ( both should be true )
a3 = True 
b3 = False 
print ( a3 and b3 )

# or  ( any one should be true )
a4 = True 
b4 = False 
print (a4 or b4)

# not ( reverse )
a5 = True 
print ( not a5)


# Assignment operators   ( updating the value )
r = 22
s = r + 10 
print ( s )
s *= 2
print ( s )
s -= 11
print ( s )
s /= 2
print(s)



# Membership operators 

code = "pw skills "
c = "p" in code  # if exist then true if not then false
print(c)

a5 = [ " data " , "analytics" , " science "]
a2= " data " in a5
print(a2)

# Identity operators       ("compare the memory location of two object")

kriti = " data analyst " 
arun = " data scientist"
a = kriti is arun 
print (a)

a = c 
b = a 
g = b is a 
print(g)



# Bitwise operators      (bits of number integers )
e = 10 & 10 
print ( e )
r = 10 & 3 
print (r )

b = bin(10 )
print (b )

# negation 
a = ~10 
print ( a ) # it will give greater value 

#Bitwise xor >> return 1 when exactly one operand is 1
v = 7^3
print(v)

#Bitwise xor >> return 1 when exactly one operand is 1
c = 77 >> 4 
print ( c )


# parenthesis 
n = ( 3 + 7 )-4 
print ( n )