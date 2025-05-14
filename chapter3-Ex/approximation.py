import math
def approximate_e(terms): 
    e_approx = 0  
    terms = 0
for number in range(terms):
    e_approx +=1 / math.factorial(number) 
    print({e_approx})

terms = int(input('Enta th3 numb3r of t3rms:'))

approx_e = approximate_e(terms) 

print(f" Approximate value of e: , {approx_e}")
print(f"Actual value of e: , {math.e}")