#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    while True:
        phrase = input("Type a phrase (or 'quit' to exit the program): ")
        if phrase.lower() == "quit":
            print("Exiting program")
            break
        print("")
    
        letters_to_redact = input("Type a comma-seporated list of letters to redact: ")
        letters_to_redact = [letter.lower() for letter in letters_to_redact.split(",")] 

        redacted_phrase = ""
        redacted_count = 0 

        for char in phrase: 
            if char.lower() in letters_to_redact:
                redacted_phrase += "_"
                redacted_count += 1 
            else: 
                redacted_phrase += char 

        print(f"Number of letters readcted: {redacted_count}")
        print(f"Redacted Phrase: {redacted_phrase}\n")
        letters_to_redact = input("Type a comma-seporated list of letters to redact: ")
        letters_to_redact = [letter.lower() for letter in letters_to_redact.split(",")] 

    # YOUR CODE ENDS HERE

main()