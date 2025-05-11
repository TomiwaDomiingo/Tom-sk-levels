print('WELCOME TO BLACKWOOD FARM')

user_total = int(input('How much would you like to flex today: '))
discount = 0

if user_total >= 1000 and user_total < 10000:
    store_discount = user_total * 5 / 100    
    total_amount = user_total - store_discount
    print('Your total after the discount is', total_amount,)
  
elif user_total >= 10000 and user_total < 50000:
    store_discount = user_total * 10 / 100    
    total_amount = user_total - store_discount
    print('Your total after the discount is', total_amount,)
  
elif user_total > 50000:
    store_discount = user_total * 20 / 100
    total_amount = user_total - store_discount
    print('Your total after the discount is', total_amount,)