cart = int(input('Enter your total purchase: '))
if cart <= 10:
    discount = 10 * cart / 100
    discount_str = str(discount)
    total_sum = cart - discount
    total_sum_str = str(total_sum)
    print('Your discount is 10% ' + 'it\'s ' + discount_str
          + '$ total cart is ' + total_sum_str
          + '$, thank you for your purchase')
elif cart >= 20:
    discount = 20 * cart / 100
    discount_str = str(discount)
    total_sum = cart - discount
    total_sum_str = str(total_sum)
    print('Your discount is 20% ' + 'it\'s ' + discount_str
          + '$ total cart is ' + total_sum_str
          + '$, thank you for your purchace')
else:
    print('Sorry, try to buy next purchase lower 10$ or greater 20$ than our store give you a discount,'
          + 'thank you for your purchase')
