from my_core.my_airtravel import Flight, AirCraft
from pprint import pprint as pp

# f = Flight()
# print(f, type(f), f.number())  # print object location, its type <class 'my_airtravel.Flight'>
# print(Flight.number(f))  # result is same as f.number()

# f = Flight("AF213")
# print(f.number())
# print(f._number)  # this also returns the flight number. However it is not recommended for prod use
# everything in python is public. there are no such access specifiers

# a = AirCraft("IN-09", "Airbus A320", num_rows=22, num_seats_per_row=6)
#
# print(a.registration(), a.model())
# print(a.seating_plan())

f = Flight("AF212", AirCraft("IN-09", "Airbus A320", num_rows=22, num_seats_per_row=6))
print(f.num_avail_seats())
f.allocate_seat("12C", "Hussain")
f.allocate_seat("11A", "John")
pp(f._seating)
print(f.num_avail_seats())
# f.allocate_seat("11A", "Mary")  # Result in exception that seat is already occupied
f.relocate_passanger("11A", "12B")
pp(f._seating)
