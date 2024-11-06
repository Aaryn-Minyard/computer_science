months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

def input_dates():
    while True: 
        input_month = input("Type Month: ")
        input_day = int(input("Type Day: "))
        return input_month,input_day

input_month, input_day = input_dates()


if input_month not in months:
    print("Try again!")
else:
    month_index = months.index(input_month)
    
    
    if (month_index == 11 and input_day >= 21) or \
       (month_index == 0) or \
       (month_index == 1) or \
       (month_index == 2 and input_day <= 19):
        print("Winter")
    
    
    elif (month_index == 2 and input_day >= 20) or \
         (month_index == 3) or \
         (month_index == 4) or \
         (month_index == 5 and input_day <= 20):
        print("Spring")
    
    
    elif (month_index == 5 and input_day >= 21) or \
         (month_index == 6) or \
         (month_index == 7) or \
         (month_index == 8 and input_day <= 21):
        print("Summer")
    
    
    elif (month_index == 8 and input_day >= 22) or \
         (month_index == 9) or \
         (month_index == 10) or \
         (month_index == 11 and input_day <= 20):
        print("Fall")
    
    else:
        print("Try again!")
