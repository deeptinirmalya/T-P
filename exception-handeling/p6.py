flights = {
    "F101": {"destination": "Delhi", "seats": 5},
    "F102": {"destination": "Mumbai", "seats": 3},
    "F103": {"destination": "Chennai", "seats": 4}
}

bookings = []

def view_flights():
    print("\nAvailable Flights:")
    for f in flights:
        print("Flight:", f, "| Destination:", flights[f]["destination"], "| Seats:", flights[f]["seats"])


def book_ticket():
    try:
        name = input("Enter passenger name: ")
        if name == "":
            print("Invalid passenger details!")
            return

        flight_id = input("Enter flight number: ")

        if flight_id not in flights:
            print("Invalid flight number!")
            return

        if flights[flight_id]["seats"] <= 0:
            print("Seat not available!")
            return

        payment = input("Enter payment method (Card/UPI): ")
        if payment not in ["Card", "UPI"]:
            print("Payment failure! Invalid payment method.")
            return

        flights[flight_id]["seats"] -= 1
        bookings.append((name, flight_id))

        print("Ticket booked successfully!")

    except Exception:
        print("Something went wrong!")


def cancel_ticket():
    try:
        name = input("Enter passenger name to cancel ticket: ")
        flight_id = input("Enter flight number: ")

        if (name, flight_id) in bookings:
            bookings.remove((name, flight_id))
            flights[flight_id]["seats"] += 1
            print("Ticket cancelled successfully!")
        else:
            print("Booking not found!")

    except Exception:
        print("Error while cancelling ticket!")


while True:
    print("\n--- Flight Booking System ---")
    print("1. View Flights")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_flights()
        elif choice == 2:
            book_ticket()
        elif choice == 3:
            cancel_ticket()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")