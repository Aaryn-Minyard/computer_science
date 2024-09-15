def convert_to_time(hour):
    return f"{hour}:00"


open = int(input("Open at: "))
open_format = convert_to_time(open)
close = int(input("Closes at: "))
close_format = convert_to_time(close)
print("  NO PARKING")
print(open_format + " - " + close_format + " " + "a.m.")