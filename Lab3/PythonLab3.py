# 1.	Create a new script called Script3Lab.py
# 2.	Create and print a list of 10 of your favorite foods (FoodList)
FoodList = ['Pizza',
            'Tacos',
            'Burrito',
            'Burgers',
            'Pasta',
            'Panda Express',
            'In N Out',
            'Pozole',
            'Birria',
            'Tamales']

# 3.	Create and print a list of 10 of your favorite cars (CarList)
CarList = ['Supra',
           'Model 3',
           'Model X',
           'CyberTruck',
           'Model Y',
           'Roadster',
           'Prorche',
           'GTR',
           'Raptor',
           'Civic']

# 4.	Add 3 entries to both list
FoodList.append('Flauts')
FoodList.append('Dumplins')
FoodList.append('Pho')

CarList.append('A4')
CarList.append('A3')
CarList.append('STR')

# 5.	Create a For Loop that loops through the FoodList and prints “I love eating <<Food>>” for each member in your list.
for food in FoodList:
    print("I love eating %s" % food)

# 6.	Create a For Loop that loops through the CarList and prints “I love driving <<Car>>” for each member in your list.
for car in CarList:
    print('I love Driving %s' % car)

# 7.	Create a variable and set it equal to a range of integers starting at 150 and goes to 200 by 5
NumRange = range(150, 200, 5)


# 8.	Create a For Loop for the same range created in #7.  “Just Added: <<Number>> to the list”
for x in NumRange:
    print('Just added %d to the list' % x)

# 9.	Create a WHILE Loop that loops through every value in your CarList
    car = 0
while len(CarList) > 0:
    print("I can't afford a %s just yet" % CarList[car])
    CarList.remove(CarList[car])


print(CarList)

#   a.	Print “I can’t afford a <<Car>> just yet”
#   b.	Delete that car from the list after the print statement
#   c.	Once the While Loop completes, all the cars should be deleted from the list.
