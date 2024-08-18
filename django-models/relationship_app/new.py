from datetime import datetime
def get_time_input():
    while True:
        time_input = input("Enter the time for the reminder (12-hour format HH:MM pm): ")
        try:
            reminder_time = datetime.strptime(time_input, "%I:%M %p").time()
            return reminder_time
        except ValueError:
            print("Invalid time format. Please enter time in 12-hour format.")
            
while True:
    user_input = input("Do you want to set a reminder? (yes/no): ").strip().lower()

    match user_input:
        case "yes":
            # get_time_input()
            break
        case "no":
            print("No reminder set. Exiting.")
            break
        case _:
            print("Invalid input. Please enter 'yes' or 'no'.")        
            