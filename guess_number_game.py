python
import random

secrete_number = random.randint(1,10)
guess = 0
count = 0
while guess != secrete_number and guess != "exit":
    guess = input("Enter a guess between 1 to 10: ")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1
    
    if count >  10:
      print("You took 10 times already!")
      break


    if guess < secrete_number:
        print("Too low")
    elif guess > secrete_number:
        print("Too high")
    else:
        print("Right!")
        print("You took only", count, "tries!")

