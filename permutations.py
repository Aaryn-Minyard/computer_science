from itertools import permutations

if __name__ == "__main__":
    """
    This script generates all permutations of words in a given string and prints them.
    """
    
    while True:
        try:
            input_string = input("Enter a sentence: ")
            words = input_string.split() 
            if len(words) > 6:
                print("Too many words! Please enter no more than 6.")
                continue
            
        except EOFError:
            print("Input interrupted. Please enter a valid sentence.")
            continue

    # Split the sentence into words
     # Split on whitespace

    # Generate all permutations of the words
        perm = permutations(words)

    # Print each permutation as a space-joined sentence
        for p in perm:
            print(' '.join(p))
        # Uncomment the next line to limit the output to the first 10 permutations
        # if i >= 10: break
        