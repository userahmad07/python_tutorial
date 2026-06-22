import random

word_to_guess = random.choice(["python", "java", "tcript", "Jango"])

attempt = 10

while attempt > 0:
    print('Current word:' + ' '.join('_' * len(word_to_guess)))
    word = input("Guess word:").lower

    if word in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == word:
                print("Congrats! Now next one...")
            else:
                attempt -= 1
                print(f"{attempt}Attempts left")
                print("Try again")