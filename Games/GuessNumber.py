from random import randint

attempts = 0

print("Hello! What's your name?")
name = input()
print("Welcome " + name, "nice to meet you!")

number = randint(1, 20)
print("Well " + name, "I'm thinking in a number between 1 and 20")

while attempts < 5:
    print("Try to guess")
    guess = input()
    guess = int(guess) 
    
    attempts = attempts + 1

    if guess < number:
        print("Bad luck!. Try again")

    elif guess > number:
        print("Bad luck! Try again")

    else:
        break

if guess == number:
    attempts = str(attempts)
    print("Good job!. You guessed it in " + attempts, "attempts")

if guess != number:
    number = str(number)
    print("I'm sorry. The number was " + number)