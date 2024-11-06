def new_func():
    while True:
        myint = int(input("Number between 11-99:"))
        if myint < 11 or myint > 99:
            print("Input must be 11-99")
            
            new_func()
        
        for number in range(myint, 9, -1):
            print(number) 
            
            inta = number // 10
            intb = number % 10

            if inta == intb:
                print(f"Countdown stopped at: {number}")
                return

#new_func()


def lowestfunc():
    numList = []
    while True: 
        myint = int(input("Numbers:"))
        
        numList.append(myint)
        print(numList)

        if len(numList) >= 5:  # Stop after collecting 5 numbers (for example)
            smallest = min(numList)
            largest = max(numList)
            print(smallest)
            print(largest)
            break

lowestfunc()