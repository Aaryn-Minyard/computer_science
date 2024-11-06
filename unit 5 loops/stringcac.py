def replace_ones_with_exclamation(word):
   
    result = ""
    
    while True:
        for char in word:
            
            if char.lower() == "i":
                result += "!"
            elif char.lower() == "a":
                result += "@"
            elif char.lower() == "m":
                result += "M"
            elif char.lower() == "b":
                result += "!"
            elif char.lower() == "B":
                result += "!"
            elif char.lower() == "s":
                result += "$"
            else:
                result += char  
        
        return result


user_input = input("Enter a word: ")


output = replace_ones_with_exclamation(user_input)
print("Modified word:", output)