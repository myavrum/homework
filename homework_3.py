# where you should see what items are in fridge, check is there electricity in the house.
# If there wouldn’t be electricity you should take all of the fruits from fridge.
# Also you need to check if you didn’t have just one fruit and go to the market to buy it. 

electricity = input ('Is there electricity in the house? ->')
take_from = 'Take all of the fruits from the fridge! '
print(take_from + str('no' in electricity))

items_in_fridge = input('What items are in the fridge? ->')
fruits_in_fridge = 'There is fruits in the fridge. '
print(fruits_in_fridge + str('fruits' in items_in_fridge))
value1 = str(False)
market = 'Go to the market to buy fruits! '
print(market + str(fruits_in_fridge == value1))
