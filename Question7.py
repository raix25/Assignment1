print (">>>>> Tossing the pyramid...")

#importing random for customizing random exercise
import random
exercise = ["plank", "squat", "sit-up","push-up"]

#using while loop for the assigning exercise
while True:
    print(f"You should do: {random.choice(exercise)} ")
    ans= input("Do you want to toss again? (yes/no): ")

    if ans == "no":# to break the loop
        print ("Goodluck!")
        break
