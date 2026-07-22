#q1     Write a Python program implements and deonstrate the fundamental algebric properties of modular  congrurences.
def is_congruent(a, b, m):
    """Check if a= b (modulo m)"""
    return (a % m) == (b % m)

#Setup variables for demonstration
m=7
a,b= 15,1
c,d=22,1
print (f" is 15= 1 (mod 7)? {is_congruent(a,b,m)}") #True(15%7==1%7)
print (f" is 22= 1 (mod 7)? {is_congruent(c,d,m)}") #True(22%7==1%7)

#1.Reflexive property: a = a (mod m)
print(f"\n Reflexive property: {is_congruent(b,a,m)}")

#2.Symmetric property:  if a = b then b=a(mod m)
print(f"\n Symmetric property: {is_congruent(b,a,m)}")

#3.Transitive property:  if a = b and b = c then a = c (mod m)
#Since 15=1 and 1=22(mod7) then 15=22(mod7)
print(f"\n Transitive property: {is_congruent(a,c,m)}")

#4.Addition property: if a + c  = b + d (mod m) 
print(f"\n Addition property: {is_congruent(a+c,b+d,m)}")

#5.Subtraction property: if a - c  = b - d (mod m)
print(f"\n Subtraction property: {is_congruent(a-c,b-d,m)}")    

#6.Multiplication property: if a * c  = b * d (mod m)
print(f"\n Multiplication property: {is_congruent(a*c,b*d,m)}")

#7.Power property: if a^k  = b^k (mod m)
k=3
print(f"\n Power property: {is_congruent(a**k,b**k,m)}")
    