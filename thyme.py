def thyme_converter():
    while True:
        thyme = input("Please choose, hours, minutes or seconds: ")
        if thyme.lower() == "minutes":
            minute_converter()
        elif thyme.lower() == "seconds":
            second_converter()
        elif thyme.lower() == "hours":
            hour_converter()
        
        else: 
            print("please enter 'hours', 'minutes', or 'seconds'")


def hour_converter():
    
    thyme = input("Please choose, minutes or seconds: ")
    if thyme.lower() == "minutes":
        hours = int(input("Number of minutes: "))
        print(str(hours // 60) + " hour(s)")
    elif thyme.lower() == "seconds":
        minutes = int(input("Number of seconds: "))
        print(str(minutes  // 3600) + " hour(s)")
    
    else: 
        print("please enter 'hours', 'minutes', or 'seconds'")
        
    
    thyme_converter()

def minute_converter():
    
    thyme = input("Please choose, hours or seconds: ")
    if thyme.lower() == "hours":
        hours = int(input("Number of Hours: "))
        print(str(hours * 60) + " minutes")
    elif thyme.lower() == "seconds":
        minutes = int(input("Number of seconds: "))
        print(str(minutes  // 60) + " minutes")
        
    else: 
        print("please enter 'hours', 'minutes', or 'seconds'")
        
    thyme_converter()


def second_converter():
    
    thyme = input("Please choose, hours or minutes: ")
    if thyme.lower() == "hours":
        hours = int(input("Number of Hours: "))
        print(str(hours * 3600) + " seconds")
    elif thyme.lower() == "minutes":
        minutes = int(input("Number of Minutes: "))
        print(str(minutes * 60) + " seconds")
    
    else: 
        print("please enter 'hours', 'minutes', or 'seconds'")
        
    thyme_converter()
            
thyme_converter()

def second_multiplier():
    seconds = int(input("Enter the number of seconds: "))
    minutes = int(input("Enter the number of minutes: "))
    hours = int(input("Enter the number of hours: "))

    # Convert time to total seconds
    total_seconds = seconds + (minutes * 60) + (hours * 3600)

    # Output the total time in seconds
    print(f"{total_seconds} seconds")

#second_multiplier()

def second_divider():
    total_seconds = int(input("Enter the total number of seconds: "))

    # Calculate hours, minutes, and remaining seconds
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Output the time in hours, minutes, and seconds
    print(f"Seconds: {seconds}")
    print(f"Minutes: {minutes}")
    print(f"Hours: {hours}")

#second_divider()
