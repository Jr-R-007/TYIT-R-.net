#
def gcd_euclidean(a,b):
    while b != 0:
        a,b=b,a%b
        return a
num1=48
num2=18
result=gcd_euclidean(num1,num2)
print(f"The GCD OF {num1} AND {num2} is:{result}")
