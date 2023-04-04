import pandas as px

# reads csv file
df = px.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"

        # Edits the available column without adding a new column
        df.to_csv("hotel.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        """Generates reservation ticket"""
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """

        return content


print(df)

# gets the id of the hotel from the user
hotel_Id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_Id)

# if the hotel is available then we book a ticket, and print a reservation ticket
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is note free.")