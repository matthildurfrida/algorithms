vowels = "aeiou"

while True:
    word = input("Enter a word: ")
    first_letter = word[0]
    if word == ".":
        break
    else:
        if first_letter in vowels:

            pl_word = word + "yay"
            print(pl_word)
        else:
            for index, letter in enumerate(word):
                if letter in vowels:
                    pl_word = word[index:] + word[:index] + "ay"
                    print(pl_word)
                    break
            else:
                pl_word = word + "ay"
                print(pl_word)
                
        
            
        
                   
    
    