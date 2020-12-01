# This program is to calculate and display the amount of discount and purchase.

# Author: Linhan Cai

# Collect data from the user.
quantity  = float(input('Please enter the number of packages you ordered: '))

# Calculate the price.
price = quantity * 100

# Calculate the discount and print out the result.
if quantity >= 0 and quantity <= 9:
    discount = 0
    print('The total cost of your purchase was $' + format(price * (1 - discount), '.2f'), 'with a discount of $' + format(discount * price, '.2f') + '.')
elif quantity >= 10 and quantity <= 19:
    discount = 0.1
    print('The total cost of your purchase was $' + format(price * (1 - discount), '.2f'), 'with a discount of $' + format(discount * price, '.2f') + '.')
elif quantity >= 20 and quantity <= 49:
    discount = 0.2
    print('The total cost of your purchase was $' + format(price * (1 - discount), '.2f'), 'with a discount of $' + format(discount * price, '.2f') + '.')
elif quantity >= 50 and quantity <= 99:
    discount = 0.3
    print('The total cost of your purchase was $' + format(price * (1 - discount), '.2f'), 'with a discount of $' + format(discount * price, '.2f') + '.')
else:
    discount = 0.4
    print('The total cost of your purchase was $' + format(price * (1 - discount), '.2f'), 'with a discount of $' + format(discount * price, '.2f') + '.')
