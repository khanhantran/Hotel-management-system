from tabulate import tabulate
from datetime import datetime

bookings = {}
next_booking_id = 1

# 1. Add booking 

from datetime import datetime

def get_valid_date():
    while True:
        try:
            date_str = input('Enter date (YYYY-MM-DD):')
            datetime.strptime(date_str, "%Y-%m-%d")  
            return date_str
        except ValueError:
            print("Invalid format! Please enter the date in YYYY-MM-DD")


def add_booking():
    global next_booking_id 
    
    print('----- ADD BOOKING -----')
    customer_name = input("Enter customer's name: ").title()
    while True:
        try:
            room_number = int(input("Enter room number: "))
            break
        except ValueError:
            print('Invalid input.Please try again')
    
    check_in = get_valid_date()
    check_out = get_valid_date()
    


    new_booking = {
        "customer_name": customer_name,
        "room_number": room_number,
        "check_in": check_in,
        "check_out": check_out
    }

    bookings[next_booking_id] = new_booking

    print(f"Booking ID {next_booking_id} added successfully!")
    next_booking_id += 1  

# 2. Search booking
def search_booking():
    print('----- SEARCH BOOKING -----')
    search_choice = int(input('''How do you want to search for your booking?
    1. Booking ID 
    2. Customer's Name 
    3. Room Number
Please enter your option: '''))
    
    if search_choice == 1:
      try:
        booking_id = int(input('Enter Booking ID:'))
        if booking_id in bookings:
            print(f'Booking details: Booking ID:{booking_id} - {bookings[booking_id]}')
        else:
            print('Booking ID not found')
      except ValueError:
          print('Invalid input. Please try again.')
    
    if search_choice == 2:
        try:
            customer_name = input("Enter customer's name:").strip().title()
            for booking_id, booking_details in bookings.items():
                if booking_details['customer_name'] == customer_name:
                    print(f'Booking details: Booking ID:{booking_id} - {booking_details}')
                    break
                else:
                    print("Customer's name not found.")
        except ValueError:
            print('Invalid input.Please try again.')
                 
    if search_choice == 3:
        try:
            room_number = int(input("Enter room number:"))
            for booking_id, booking_details in bookings.items():
                if booking_details['room_number'] == room_number:
                    print(f'Booking details: Booking ID:{booking_id} - {booking_details}')
                    break
                else:
                    print('Room number not found.')
        except ValueError:
            print('Invalid data. Please try again.')
# 3. Delete booking
def del_booking():
    print('----- DELETE BOOKING -----')
    booking_id = int(input('Please enter the Booking ID you want to delete: '))
    
    if booking_id in bookings:
       del bookings[booking_id]
       print(f'Booking ID {booking_id} has been deleted successfully.')
    else:
        print('Booking ID not found.')

# 4. Update booking
def update_booking():
    print('----- UPDATE BOOKING -----')
    booking_id = int(input("Enter Booking ID: "))
    
    if booking_id in bookings:
        print('What would you like to update?')
        print("1. Customer's name")
        print("2. Room number")
        print("3. Check-in date")
        print("4. Check-out date")
        
        update_choice = int(input("Choose your option (1-4): "))

        if update_choice == 1:
            new_name = input("Enter new customer's name: ").strip().title()
            bookings[booking_id]['customer_name'] = new_name
            print(f"Customer name updated to {new_name}.")

        elif update_choice == 2:
            new_room = input("Enter new room number: ")
            bookings[booking_id]['room_number'] = new_room
            print(f"Room number updated to {new_room}.")

        elif update_choice == 3:
            new_check_in = input("Enter new check-in date (YYYY-MM-DD): ")
            bookings[booking_id]['check_in'] = new_check_in
            print(f"Check-in date updated to {new_check_in}.")

        elif update_choice == 4:
            new_check_out = input("Enter new check-out date (YYYY-MM-DD): ")
            bookings[booking_id]['check_out'] = new_check_out
            print(f"Check-out date updated to {new_check_out}.")
    else:
        print("Booking ID not found.")

#5 List of customers
def customers_tab():
    if not bookings:
        print('No bookings found.')
        input("\nPress Enter to return to the main menu...")  
        return
    
    customers = [['Booking ID', "Customer's name", 'Room number', 'Check-in date', 'Check-out date']]
    for booking_id, booking_details in bookings.items():
        customers.append([
            booking_id,
            booking_details['customer_name'],
            booking_details['room_number'],
            booking_details['check_in'],
            booking_details['check_out'],
        ])

    print(tabulate(customers, headers='firstrow', tablefmt='grid'))
    input("\nPress Enter to return to the main menu...")  

# 6. Main loop
def main():
    while True:
        print('''====== BOOKING MANAGEMENT SYSTEM ======
        1. Add booking
        2. Search booking
        3. Delete booking
        4. Update booking
        5. List of customers
        6. Exit
========================================''')
        try:
            choice = int(input('Please enter a number from 1 to 6: '))
            if choice == 1:
                add_booking()
            elif choice == 2:
                search_booking()
            elif choice == 3:
                del_booking()
            elif choice == 4:
                update_booking()
            elif choice == 5:
                customers_tab()
            elif choice == 6:
                print('Exiting system')
                break
            else:
               print("Invalid choice. Please select a number from 1 to 6.")
        except ValueError:
             print("Invalid input. Please enter a number from 1 to 6.")


main()
