from datetime import datetime as dt
import time
import random

TRAINS=[(12001, "AP Exp", "BHOPAL", "AMARAVATI"),(14701, "Vijay Exp", "BHOPAL", "AMARAVATI"),(13345, "Rajdhani Express", "BHOPAL", "VELLORE"),(12137, "Coromandel Express", "BHOPAL", "CHENNAI"),(12247, "Chennai Express", "BHOPAL", "CHENNAI"),(12860, "Gitanjali Exp", "CHENNAI", "AMARAVATI"),(15423, "Vellore Exp", "CHENNAI", "VELLORE"),(12839, "Raj Bhoj Exp", "CHENNAI", "BHOPAL"),(17689, "Shatabadi Express", "VELLORE", "BHOPAL"),(17689, "Tejas Express", "VELLORE", "BHOPAL"),(14167, "Garib Rath Express", "VELLORE", "AMARAVATI"),(12548, "Jan Shatabdi Express", "AMARAVATI", "CHENNAI"),(18453, "Duranto Express", "AMARAVATI", "BHOPAL"),(19638, "Godavari Express", "AMARAVATI", "VELLORE")]

BASE_FARES={("BHOPAL","AMARAVATI"): 1500,("BHOPAL", "VELLORE"): 2100,("BHOPAL","CHENNAI"): 2000,("CHENNAI", "AMARAVATI"): 1200,("CHENNAI","VELLORE"): 700,("CHENNAI", "BHOPAL"): 2050,("VELLORE","BHOPAL"): 2150,("VELLORE","AMARAVATI"): 1450,("AMARAVATI","CHENNAI"): 1250,("AMARAVATI","BHOPAL"): 1550,("AMARAVATI","VELLORE"): 1300}

def valid_city(x):
    while True:
        c=input(x).strip().upper()
        if c:  
            return c
        print("Input Cannot be empty. Please try again")

def valid_date():
    while True:
        try:
            d=input("Enter date of travel(DDMMYYYY): ")
            day=int(d[0:2])
            month=int(d[2:4])
            year=int(d[4:8])
            travel=dt(year, month, day) 
            if travel.date()>=dt.today().date(): 
                return travel
            else:
                print("Travel date must be today or in future.")
        except ValueError:
            print("Invalid date format(Use DDMMYYYY). Please Try Again")

def calculate_fare(source, dest, preferred_berth_code=None):
    route_key=(source, dest)
    base_price=BASE_FARES.get(route_key, 0)

    if base_price==0:
        return 0 

    GST=base_price*(0.05)
    final_fare=base_price+GST
    return round(final_fare)

def process_payment(fare):
    print("\n-----Payment Gateway-----")
    print(f"Total Amount Due: INR {fare}")
    
    while True:
        card=input("Enter 16-digit card number:")
        if len(card) == 16 and card.isdigit():
            break
        print("Invalid card number.")
        
    while True: 
        pin= input("Enter 4-digit PIN:")
        if len(pin) == 4 and pin.isdigit(): 
            break
        print("Invalid PIN:")
        
    print("\nProcessing payment...")
    time.sleep(3)
    print("Payment successful!")
    return True 

def booking_system():
    print("------Welcome to VITrails:Train Booking System------")

    source=valid_city("Enter Source City : [Ex- BHOPAL, AMARAVATI, VELLORE, CHENNAI]: ")
    dest=valid_city("Enter Destination City : [Ex- BHOPAL, AMARAVATI, VELLORE, CHENNAI]: ") 
    travel=valid_date()
    
    print(f"\n--- Searching for trains from {source} to {dest} ---")
    available_trains=[
        train for train in TRAINS 
        if train[2] == source and train[3] == dest]
    
    if not available_trains:
        print("No trains found for this route. Booking cancelled.")
        print("Available cities in VITrails : BHOPAL, AMARAVATI, VELLORE, CHENNAI.")
        return

    print("Found the following trains:")
    for i, train in enumerate(available_trains):
        print(f"{i+1}. Train No: {train[0]} | Name: {train[1]}")
        
    while True:
        try:
            choice=int(input("Enter the number of the train you want to book: "))
            if 1<=choice<=len(available_trains):
                selected_train=available_trains[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    BERTH_TYPES={'LB': 'Lower Berth', 'MB': 'Middle Berth', 'UB': 'Upper Berth', 'SL': 'Side Lower', 'SU': 'Side Upper'}
    print("\n-----Seat Preferences-----")
    print("Available Preferences: LB , MB , UB , SL ")
    
    while True:
        pref=input("Enter your preferred seat type (LB/MB/UB/SL): ").strip().upper()
        if pref in BERTH_TYPES:
            break
        print("Invalid preference. Please enter LB, MB, UB, SL")

    fare=calculate_fare(source, dest)
    if fare==0:
        print("\n*ERROR: Could not calculate fare for this route. Booking cancelled.*")
        return

    coach=random.choice(['B1','B2','B3','B4','B5'])
    seat_no=random.randint(1, 72)
    remainder=seat_no%8
    if remainder in [1, 4]:
        allotted_berth_code='LB'
    elif remainder in [2, 5]:
        allotted_berth_code='MB'
    elif remainder in [3, 6]:
        allotted_berth_code='UB'
    elif remainder == 7:
        allotted_berth_code='SL'
    else: 
        allotted_berth_code='SU'
    allotted_berth_name=BERTH_TYPES.get(allotted_berth_code, "Unknown Berth")

    if process_payment(fare): 
        print("\n  ------VITrails Ticket------  ")
        print("")
        print(f"Train No: {selected_train[0]} | Name: {selected_train[1]}")
        print(f"Route: {source} --> {dest}") 
        print(f"Travel Date: {travel.strftime('%d-%b-%Y')}") 
        print("-------------------------------------------------")
        print(f"Coach No.: {coach} | Seat No. {seat_no}")
        print(f"Alloted berth: {allotted_berth_name} ({allotted_berth_code})")
        print(f"Pref Type: {BERTH_TYPES.get(pref)}")
        print(f"Fee Paid including GST: INR {fare}")
        print("-------------------------------------------------")
        print("Wish you a pleasant journey and\n Travel again with VITrails! ")

if __name__=="__main__":
    booking_system()
