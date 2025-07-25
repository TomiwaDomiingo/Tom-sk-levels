prices = [17, 14, 13, 18, 22]

def halve(num):
    return num/2

    no_tax = 0.85 * num
    return no_tax/2

halved = [halve(price) for price in prices]
print(halved)

