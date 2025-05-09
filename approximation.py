def approximate_e(terms):
    e_approx = 1 
    factorial = 1 
    
    for n in range(1, terms):
    factorial *= n  
    e_approx += 1 / factorial  
    return e_approx
result = approximate_e(10)
print("Approximation of e:", result)