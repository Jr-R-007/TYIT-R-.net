def gcd_euclidean(a,b):
    
    while b !=0:
        a,b=b,a%b
    return abs(a)
    
    
#Q3 Computation of greatest common divisor of A =35 and B =12
#Variable a=35,b=12
#iteration 1: 35% 12 = 11 -> a=12,b=11
#iteration 2: 12% 11 = 1 -> a=11,b=1
#iteration 3: 11% 1 = 0 -> a=1,b=0
print(gcd_euclidean(35,12))


#Q4 Computation of least common multiple of A =20 and B =100
#Variable a=20,b=100
#iteration 1: 20%100= 20 -> a=100,b=20
#iteration 2: 100% 20 = 0 -> a=20,b=0
print(gcd_euclidean(20,100))
