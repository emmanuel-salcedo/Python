import mysql.connector

# 2.	Connect to your MySQL Server / adventureworks database
mydb = mysql.connector.connect(
    user='root',
    passwd='PASSWORD',
    host='Localhost',
    database='adventureworks'
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("Show tables")
print(mycursor.fetchall())

# 3.	Find total Sales by Credit Card Type
print("\nFind total Sales by Credit Card Type\n")
mycursor.execute(
    "select 		CreditCard.CardType, round(Sum(SalesOrderHeader.SubTotal),2)as TotalSales \
	FROM 		SalesOrderHeader \
	inner JOIN 	CreditCard ON  SalesOrderHeader.CreditCardID = CreditCard.CreditCardID \
    group by 	CreditCard.CardType \
    order by 	CreditCard.CardType desc")
print(mycursor.fetchall())

# 4.	Find total Sales by Product
print("\nFind total Sales by Product\n")
mycursor.execute(
    "SELECT 			Product.Name as Product, \
					round(Sum(Sales.LineTotal),2) as TotalSales \
	FROM 			salesorderdetail as Sales \
    INNER JOIN 		Product \
    ON 				Sales.ProductID = Product.ProductId \
    INNER JOIN		ProductSubCategory as SubCat \
    ON 				Product.ProductSubCategoryID = SubCat.ProductSubCategoryID \
    GROUP BY 		Product.name \
    ORDER BY 		Product.name ASC")
print(mycursor.fetchall())

# 5.	Find total Sales by Ship State
print("\nFind total Sales by Ship State\n")
mycursor.execute(
    "Select 	State.Name as ShipState, \
				round(Sum(Sales.LineTotal),2) as TotalSales \
	From 		salesorderdetail as Sales \
    INNER JOIN 	salesorderheader as header \
    on 			Sales.SalesOrderID =Header.SalesOrderId \
	INNER JOIN	SalesTerritory as Territory \
    on 			header.territoryid = Territory.TerritoryID \
    INNER JOIN 	StateProvince as State \
    on 			Territory.TerritoryID = State.TerritoryID \
	group by 	State.name \
    Order by 	State.Name ASC")
print(mycursor.fetchall())

# 6.    Find total Sales by Territory Group
print("\nFind total Sales by Territory Group\n")
mycursor.execute(
    "Select 		Territory.Group as TerritoryGroup, \
					round(Sum(Sales.LineTotal),2) as TotalSales \
	From 			salesorderdetail as Sales \
    INNER JOIN 		salesorderheader as header \
    on 				Sales.SalesOrderID = Header.SalesOrderId \
	INNER JOIN		SalesTerritory as Territory \
    on 				header.territoryid = Territory.TerritoryID \
	group by 		Territory.group \
    Order by 		Territory.group ASC")
print(mycursor.fetchall())

# 7.	Find Total Sales by Ship Method
print("\nFind Total Sales by Ship Method\n")
mycursor.execute(
    "Select 		Ship.Name as 'Ship Method', \
					round(Sum(Sales.LineTotal),2) as TotalSales \
	From 			salesorderdetail as Sales \
    INNER JOIN 		salesorderheader as header \
    on 				Sales.SalesOrderID =Header.SalesOrderId \
	INNER JOIN		ShipMethod as ship \
    on 				header.ShipMethodID = Ship.ShipMethodID \
    group by 		Ship.name \
    Order By		Ship.name desc")
print(mycursor.fetchall())

# 8.	Find Total Sales by Product Subcategory.

print("\nFind Total Sales by Product Subcategory\n")
mycursor.execute(
    "Select 			Sub.Name as Product_SubCategory,round(Sum(Sales.LineTotal),2) as TotalSales \
	From 			salesorderdetail as Sales \
    INNER JOIN 		Product \
    on 				Sales.ProductID = Product.ProductId \
    INNER JOIN		ProductSubCategory as Sub \
    on 				Product.ProductSubCategoryID = Sub.ProductSubCategoryID \
    group by 		sub.name \
    order by 		sub.name ASC")
print(mycursor.fetchall())
