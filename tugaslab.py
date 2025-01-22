secret_word = "ganteng"

user_input = input("Enter a single letter: ").strip()

if len(user_input) == 1 and user_input.isalpha():
    
    if user_input.lower() in secret_word.lower():
        print(f"Yes, the letter '{user_input}' is in the secret word!")
    else:
        print(f"No, the letter '{user_input}' is not in the secret word.")
else:
    print("Invalid input. Please enter a single letter.")
