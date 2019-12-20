# 2.	Create a function called NonYaBusiness that accepts 0 parameters and returns the statement “None of your business”
def NonYaBusiness():
    """0 parameters and returns the statement “None of your business" """
    print('None Of Your Business')


# 3.	Create a List of Names and add 10 names to the list
ListOfNames = ['Lesly,'
               'James',
               'Jack',
               'Arthur',
               'Fallon',
               'Arya',
               'Spencer',
               '11',
               'Mike',
               'Jackson']


# a.	Create a function that accepts a name


def AddName1(name, list):
    """AddName1: this function requires a name and a list as parameters then adds the name to the list and displays the list"""
    list.append(name)
    print(list)


def AddName(name):
    """AddName: this function requires a name aas parameters then adds the name to ListOfNames and displays the ListofNames"""
    ListOfNames.append(name)
    print(ListOfNames)


AddName1('Avery', ListOfNames)
AddName('Nano')
AddName('J')
AddName('K')
AddName('L')
AddName('M')

print(AddName.__doc__)
print(AddName1.__doc__)

# b.	In the function, add the input parameter name to the Names list
# c.	Print the full list as the last step in the function
# d.	Add 5 more names to the list using the function
# e.	Document the function
# f.	Retrieve documentation from function
