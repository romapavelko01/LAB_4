"""
Module for the UML of logistic system.
"""
import random


class Location:
    """
    Class for location: city and post office.
    """

    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice

    def __repr__(self):
        return f"Location({self.city}, {self.postoffice})"


class Item:
    """
    Class for Item representation.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item {self.name} costs {self.price}"


class Vehicle:
    """
    Class for Vehicle representation.
    """

    def __init__(self, vehicleNo, isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order:
    """
    Class for Order representation.
    """

    def __init__(self, user_name, city, postoffice, items):
        self.orderld = random.choice(range(100000000, 1000000000))
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None
        print(f"Your order number is {self.orderld}.")

    def __str__(self):
        return f"Order {self.orderld} for {self.user_name} to " + \
               ", ".join([self.location.city, str(self.location.postoffice)])

    def calculateAmount(self):
        """
        Method for computing the total price.
        """
        return sum([item.price for item in self.items])

    def assignVehicle(self, vehicle):
        """
        Method for vehicle assignment.
        """
        self.vehicle = vehicle


class LogisticSystem:
    """
    Main class for Logistic System representation.
    """

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order):
        """
        (Order) -> (None)
        Method for placing an order if there is
        any available vehicle.
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                order.assignVehicle(vehicle)
                vehicle.isAvailable = False
                break
        check_lst = [veh for veh in self.vehicles if veh.isAvailable]
        if not check_lst:
            print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderld):
        """
        (int) -> (str)
        Based on the previous order information,
        returns either order delivery description or
        a warning that the order does not exist.
        """
        i = 0
        while i < len(self.orders):
            if self.orders[i].orderld == orderld:
                break
            i += 1
        if i < len(self.orders):
            our_ord = self.orders[i]
            ult_price = our_ord.calculateAmount()
            return f"Your order #{our_ord.orderld} is sent" + \
                   f" to {our_ord.location.city}" + \
                   f" Total price: {ult_price} UAH."
        else:
            return "No such order."
