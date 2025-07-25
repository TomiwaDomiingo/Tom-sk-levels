words = ["apple", "alligator","abracadabra", "avatar"]

def has_double_a (word) :
    count = word. count ("a")
    return count == 5
double_a = [has_double_a (word) for word in
words]
print(double_a)

websites = ['nytimes.com','waptrick.com','naija.org','x-train.org','economist.com']

commercial = [website for website in websites if website.count("com") > 0]
print(commercial)

ids = ['X12','M8','GLB','Z10']

ids_a = ['0' + value for value in ids]
print(ids_a)

ids_b = []
for value in ids_b:
    new_ids = "1" + value
    ids_b.append(new_ids)
    print(new_ids)


menu = ['vanilla latte','vanilla scone','russian creame']

menuRedo = [item.replace("vanilla", "matcha") for item in menu]
print(menu)
print(menuRedo)

passwords = ['CRY88P','GDK77','87HGW','123Ghd']
copy = [password for password in passwords]
print(copy)


numbers = ['+44 709821','+43 565326','+31 87432','+44 940477']

uk_numbers = [num for num in numbers if num.count("+44") == 1]
print(uk_numbers)