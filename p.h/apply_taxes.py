prices = [100,450,99,29]

def apply_taxes(price):
    vat = 0.15 * price
    duties = 0.20 * price
    return price + vat + duties

tax_inclusive = [apply_taxes(price) for price in prices]
print(tax_inclusive)