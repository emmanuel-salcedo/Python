import pandas

a = pandas.read_table('https://bit.ly/chiporders')
print(a)

header = a.head()
print(header)

user_columns = ['userid', 'age', 'gender', 'occupation', 'zip_code']

c = pandas.read_table('https://bit.ly/movieusers', sep='|', header=None, names=user_columns)
cheader = c.head()
print(cheader)


users = c
users_age = c['age']
print(users_age)

print(type(users))
print(type(users_age))

users_gender = users.gender.head()
print(users_gender)

users['Occup-Gender'] = users['occupation'] + '-' + users['gender']
print(users)