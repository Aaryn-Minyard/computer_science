

while True:
    my_string = input("Say something:")
    if my_string != "done" and my_string != "Done" and my_string != "d":

        reversed_string = my_string[::-1]
        print(reversed_string)

    else:
        print("done")
        break