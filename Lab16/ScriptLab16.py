import pandas as pd
from pandas import ExcelFile, ExcelWriter
import sqlalchemy


polution_tbl = pd.read_table
# adding own column names
states_columns = ['id', 'Name', 'Abbr', 'Country', 'Type', 'Region Name', 'Division Name']
states_tbl = pd.read_table('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/uspollution.csv',
                           sep=',', encoding='cp1252')

engine = sqlalchemy.create_engine('mysql://root:PASSWORD@localhost/Barget')
states_tbl.to_sql('states_tbl', engine, if_exists='replace')

dates_table = pd.read_excel('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/files/Date_dim.xlsx',
                            sheet_name='Sheet1')
dates_table.to_sql('dates', engine, if_exists='replace')

barget_columns = ['RowID',
                  'OrderID',
                  'OrderDate',
                  'OrderPriority',
                  'OrderQuantity',
                  'Sales',
                  'Discount',
                  'ShipMode',
                  'Profit',
                  'UnitPrice',
                  'ShippingCost',
                  'CustomerName',
                  'Province',
                  'Region',
                  'CustomerSegment',
                  'ProductCategory',
                  'ProductSub-Category',
                  'ProductName',
                  'ProductContainer',
                  'ProductBaseMargin',
                  'OrderDate1']
barget_order_table = pd.read_excel(
    '/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/files/Barget Store.xls',
    sheet_name='Orders', header=None, names=barget_columns)
# print(barget_order_table.head())
barget_order_table.to_sql('Orders', engine, if_exists='replace')

barget_returns = pd.read_excel(
    '/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/files/Barget Store.xls',
    sheet_name='Returns')
barget_returns.to_sql('Returns', engine, if_exists='replace')

barget_users = pd.read_excel(
    '/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/files/Barget Store.xls',
    sheet_name='Users')
barget_users.to_sql('Users', engine, if_exists='replace')
