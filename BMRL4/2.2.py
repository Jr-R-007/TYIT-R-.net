#Computation of greatest common divisor of
#1)(60,15)
#2)(35,12)
#3)(252,105)
#using Euclid's algorithm

def gcd_with_steps(a,b):
    step =1
    while b !=0:
        reminder =a%b
        print(f"Step{step}:{a}%{b} = {reminder} -> Next (a={b},b={reminder})")
        a,b=b,reminder
        step+=1
        print(f"GCD is:{a}\n")
        return a
    
gcd_with_steps(60,15)
gcd_with_steps(35,12)
gcd_with_steps(252,105)
