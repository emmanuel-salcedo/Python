# 2.	Create 2 Dictionaries
#   1.	Cars – Add 5 entries.  Intentionally spell one of your Car Model’s incorrectly.
#       a.	Key = Make
#       b.	Value = Model
#   2.	Trucks – Add 5 entries
#       a.	Key = Make
#       b.	Value = Model
#   3.	Cars and Trucks (Empty)

Cars = {
    "Subaru": "STR",
    "Tesla": "Roadst3r",
    "Audi": "A4",
    "Lexus": "RX300",
    "Toyota": "Supra",
    "Mercedes": "S Class"
}

Trucks = {
    "Ford": "F150",
    "Ram": "1500",
    "Tesla1": "CyberTruck",
    "Honda": "Enclave",
    "Chevy": "Silverado"
}
CarsAndTrucks = {}

print(Cars)
print(Trucks)
print(CarsAndTrucks)

# 3.	Copy the Cars and Trucks dictionaries into the “Cars and Trucks” dictionary.
CarsAndTrucks.update(Cars)
print(CarsAndTrucks)

CarsAndTrucks.update(Trucks)
print(CarsAndTrucks)

# 4.	Do a search on a Make you know is not in the Cars dictionary.  (Display the FALSE results)
print("Roadster" in CarsAndTrucks)

# 5.	Delete 3 entries from the Cars and 2 entrée from the Trucks dictionary
del Cars["Subaru"]
del Cars["Lexus"]
del Cars["Audi"]
print(Cars)

del Trucks["Honda"]
del Trucks["Chevy"]
print(Trucks)

# 6.	Create a For Loop to display all of the Cars and Trucks from the 2 dictionaries.
# a.	For Every Car or Truck, you will display “I like this car/truck:  <<Car/Truck>>
for make, model in CarsAndTrucks.items():
    print("I like this Car/Truck %s, %s" % (make, model))
