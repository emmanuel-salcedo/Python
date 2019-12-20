import datetime

# today = datetime.date.now()®
from ScriptLab6 import Cars

today = datetime.datetime.now()

# print (Today)
print(today)

# value = Zero
value = 0

# value = value + 5 * value
value = value + 5 * value

# Print ('My new Value is',value)
print('My new Value is', value)

# Food = {'Meat' : 'Chicken', 'Veggie': 'Beats", 'starch':'Potatoes'}
Food = {'Meat': 'Chicken', 'Veggie': 'Beats', 'starch': 'Potatoes'}

# for key,value in Cars.items(:
#     PRINT "I would love to have a ", key, valu

for key, value in Cars.items():
    print("I would love to have a ", key, value)
