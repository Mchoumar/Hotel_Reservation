from hotel import Hotel, print_df
from ticket import ReservationTicket, SpaTicket
from card import SecureCreditCard

print_df()

# gets the id of the hotel from the user
hotel_Id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_Id)

# if the hotel is available then we book a ticket, and print a reservation ticket
if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26", holder='JOHN SMITH', cvc='123'):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package? ")
            if spa == "yes":
                spa_reservation = SpaTicket(name, hotel)
                print(spa_reservation.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not free.")
