def madlib(): 
    while True:
        adjective1 = input("Adjective: ")
        noun1 = input("Food and Number: ").split()
        food = noun1[0]
        count = noun1[1]
        adjective2 = input("Adjective: ")
        item1 = input("Item and Number: ").split()
        thing1 = item1[0]
        count2 = item1[1]
        line1 = f"This morning, I walked into the {adjective1} coffee shop and ordered {count} {food}s."
        line2 = f"The barista, who was {adjective2} handed me my drink with {count2} {thing1}s."
        print(line1)
        print(line2)

        adjective1 = input("Adjective: ")
        noun1 = input("Noun: ")
        verb1 = input("Verb ending in 'ing': ")
        line3 = f"I sat down at a {adjective1} table next to a {noun1}."
        line4 = f"Suddenly, I heard someone {verb1} loudly from across the room."
        print(line3)
        print(line4)

        noun1 =input("Noun: ")
        verb1 = input("Verb: ")
        adjective1 = input("Emotional Adjective: ")
        line5 = f"I turned around and saw a {noun1} {verb1} right next to the counter."
        line6 = f"It was the most {adjective1} moment of my day!"



        print( line1 + " " + line2 + " " + line3 + " " + line4 + " " + line5 + " " + line6)
        play_again = input("Do you want to create another Mad Lib? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

madlib()