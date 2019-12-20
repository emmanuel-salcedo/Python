import pandas

# 3.	Load the file into a Pandas dataframe and answer the following questions
data = pandas.read_csv('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/Consumer_Complaints.csv')
# print(data)

# 4.	Retrieve the 1st 5 rows of the dataset
header = data.head()
for cols in header:
    print(cols)

print("\nCount Rows:")
print(data.shape[0])
print("\nCount Columns:")
print(data.shape[1])

# 5.	Delete the following columns and then display the 1st 5 rows in the new dataset
#     a.	Consumer complaint narrative
del header['Consumer complaint narrative']
#     b.	Company public response
del header['Company public response']
#     c.	Consumer consent provided
del header['Consumer consent provided?']
#     d.	Consumer disputed?
del header['Consumer disputed?']
#     e.	Complaint ID
del header['Complaint ID']
#     f.	Tags
del header['Tags']
#     g.	Issue
del header['Issue']
print('Deleted Stuff')
print(header)
# 6.	How many rows and columns are in the dataset.
print("Rows and COls in Dataset:\nCount Rows:")
print(header.shape[0])
print("Count Columns:")
print(header.shape[1])

# 7.	Delete rows 0 – 1000.  (We did not cover this in the class.  You will need to use the Range function.  Go look at Script3.py for help)
newdata = data.drop([data.index[0], data.index[1000]])
# 8.	How many rows and columns are in the dataset.
print('\nDeleted first 1000 Rows:')
print("Count Rows:")
print(header.shape[0])
print("Count Columns:")
print(header.shape[1])
# 9.	Sort the dataframe by Date Received descending – Print Dataframe
sorteddata = newdata.sort_values(by=['Date received'], ascending=False)
print(sorteddata)
# 10.	Find the number of disputes by Company
disputesbycompany = data.groupby('Company').sum()
print('\nDisputes by Company')
print(disputesbycompany)
# 11.	Find the number of disputes by State
disputesbystate = data.groupby('State').sum()
print('\nDisputes by State')
print(disputesbystate)
# 12.	Find the number of disputes by DateReceived Year, Month descending
data['Date received'] = pandas.to_datetime(data['Date received'])
disputesbydate = data.groupby(data['Date received']).sum()
print('\nDisputes byDate')
print(disputesbydate)