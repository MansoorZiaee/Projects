#!/bin/python3

class Menu:
	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items = items
		self.start_time = start_time
		self.end_time = end_time

	def __str__(self):
		return f"{self.name} menu available from {self.start_time} to {self.end_time}"

	def calculate_bill(self, purchased_items):
		total_price = sum(self.items[item] for item in purchased_items if item in self.items)
		return total_price
print("==== Menus ====")

brunch = Menu("brunch", { 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50 }, '11am', '4pm' )
print(brunch)

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }, '3pm', '6pm')
print(early_bird)

dinner = Menu("dinner", { 'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }, '5pm','11pm' )
print(dinner)

kids = Menu("kids", { 'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00 }, '11am', '9pm' )
print(kids)

brunch_order = ['pancakes', 'home fries', 'coffee']
print(f"The total cost for brunch order: ${brunch.calculate_bill(brunch_order)}")

early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print(f"The total cost for early-bird order: ${early_bird.calculate_bill(early_bird_order)}")

class franchise:
	def __init__(self, address, menus):
		self.address = address
		self.menus = menus
	def __str__(self):
		return f"Address: {self.address}"
	def available_menus(self, time):
		available_menus = [menu for menu in self.menus if time >= menu.start_time and time <= menu.end_time]
		return available_menus


flagship_menus = [brunch, early_bird, dinner, kids]
new_installment_menus = [brunch, early_bird, dinner, kids]

("==== Franchises ====")

flagship_store = franchise("1232 West End Road", flagship_menus)
print(flagship_store)

new_installment = franchise("12 East Mulberry Street", new_installment_menus)
print(new_installment)

print("The available menus at 12 noon:")
for menu in flagship_store.available_menus("12pm"):
    print(menu.name)

print("These are the available menus at 5pm:")
for menu in flagship_store.available_menus("5pm"):
    print(menu.name)
#####


class business:
	def __init__(self, name, franchises):
        	self.name = name
        	self.franchises = franchises

arepas_menu = Menu("arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50 }, "10am", "8pm")

arepas_place = franchise("189 Fitzgerald Avenue", [arepas_menu])

take_a_arepa = business("Take a' Arepa", [arepas_place])

print("==== Business ====")
print(take_a_arepa.name)
print(take_a_arepa.franchises[0])
