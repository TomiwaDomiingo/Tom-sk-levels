"""""
prices = [10,40,14,12,62,58,22]

halved = []
for price in prices:
    half_price = price/2
    halved.append(half_price)

print(halved)

halved = [price * 2 for price in halved]
print(halved)

answers = ['True','False','False']
opposite = []

for answer in answers:
    opposite.append(not answer)

    print(opposite)

print([not answer for answer in answers])


expiry_years = [2018,2022,2027,2030]

renewed = [year + 4 for year in expiry_years]
print(renewed)

ages = [17, 14, 13, 18, 22]

can_drive = [age >= 18 for age in ages]
print(can_drive)

results = [3.12, 2.1, 1.9,3.0]
corrected_results = [result + 0.1 for result in results]
print(corrected_results)
"""
users = ['jill','ahmed','rex']
users[-3] = 'Dom'
print(users)

active_users = ['jill','ahmed','rex','Dom','Abass']
del active_users[-1]
print(active_users)

user = ('joe', 'Dom', 27)
name = user[0]
age = user[-1]
messsage = f'{name}, {age}'
print(messsage)