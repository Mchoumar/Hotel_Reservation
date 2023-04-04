import pandas as px

# reads csv file
df = px.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        pass

    # books a hotel
    def book(self):
        pass

    # checks if the hotel is available
    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)

# gets the id of the hotel from the user
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)

# if the hotel is available then we book a ticket, and print a reservation ticket
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is note free.")