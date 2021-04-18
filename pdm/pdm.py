from PdmCars import vehicles
from PdmCustomers import customers

# main file
def find_name(vehicle, name_perameter):
    return name_perameter.lower() in vehicle.alias.lower()

def find_price_in_range(vehicle, lower_price, upper_price):
    return vehicle.price >= lower_price and vehicle.price <= upper_price

def price_and_type(vehicle, lower_price, upper_price):
    return vehicle.price >= lower_price and vehicle.price <= upper_price and type.lower() in vehicle.alias.lower()

def matching_name(customer, name):
    return name.lower() in customer.last_name.lower() or name.lower() in customer.first_name.lower()

input_decision = int(input('Input 1 to search by name, 2 to search by price, or 3 to search by type and price: '))

if input_decision == 1:
    name_perameter = str(input('Enter keyword for vehicle: '))

elif input_decision == 2:
    lower_price = int(input('Enter lower bound for pricing: '))
    upper_price = int(input('Enter upper bound for pricing: '))

elif input_decision == 3:
    type = str(input('Enter vehicle type: '))
    lower_price = int(input('Enter lower bound for pricing: '))
    upper_price = int(input('Enter upper bound for pricing: '))
elif input_decision == 4:
    name = input("Enter customer's name: ")


if input_decision == 1:
    matching_perameters = [vehicle for vehicle in vehicles if find_name(vehicle, name_perameter)]
elif input_decision == 2:
    matching_perameters = [vehicle for vehicle in vehicles if find_price_in_range(vehicle, lower_price, upper_price)]
elif input_decision == 3:
    matching_perameters = [vehicle for vehicle in vehicles if price_and_type(vehicle, lower_price, upper_price)]
elif input_decision == 4:
    matching_perameters = [customer for customer in customers if matching_name(customer, name)]

if input_decision == 1 or input_decision == 2 or input_decision == 3:
    print('---------------------------------------------\n')
    for vehicle in matching_perameters:
        price =  "${:,.0f}". format(vehicle.price)

        print('Vehicle Name: ' + vehicle.name)
        print('Vehicle Class: ' + vehicle.classification)
        print('Vehicle Price: ' + str(price))
        print('Vehicle Notes: ' + vehicle.notes)
        print('\n---------------------------------------------\n')

if input_decision == 4:
    print('---------------------------------------------\n')
    for customer in matching_perameters:
        print('Customer Name: ' + customer.first_name + ' ' + customer.last_name)
        print('Customer Notes: ' + customer.notes)
        print('Customer Purchase(s): ' + customer.purchases)
        print('\n---------------------------------------------\n')



if len(matching_perameters) == 0:
    print('NO MATCHES FOUND, TRY DIFFERENT SEARCH TERMS')
    print('\n---------------------------------------------')
