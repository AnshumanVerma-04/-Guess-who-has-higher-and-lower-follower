from art import logo
from art import vs
from game_data import data
import random
# RANDOM
randA = random.choice(data)
randB = random.choice(data)
while randA == randB:
    randB = random.choice(data)

current_score = 0
game_over = False
while not game_over:

    print(logo)



    #MAKE THINGS IN PRINTABLE FORM
    namee = randA["name"]
    back =  randA["follower_count"]
    countryA= randA["country"]
    occupation = randA["description"]
    print(f"{"compareA:"} {namee}{","} {countryA}{","} {occupation}")
    print(vs)

    nameeB = randB["name"]
    backB = randB["follower_count"]
    countryB= randB["country"]
    occupationB= randB["description"]
    print(f"{"compareB:"} {nameeB}{","} {countryB}{","} {occupationB}")

    compare = input("Who has more followers? Type 'A' or 'B': ").lower()
    while compare != "a" and compare != "b":
        print("Please enter only A or B.")
        compare = input("who has more follower :TYPE 'A' OR 'B':").lower()

    if compare ==  "a":
        if back > backB:
            current_score+=1
            print(f"{"u are right"} {":"}{"your current score"}{"="}{current_score}")
            # winner stays
            randA = randB

            # New B
            randB = random.choice(data)

            while randA == randB:
                randB = random.choice(data)
        else:
            print(f"{"sorry"} {"thats wrong"} {"final_score:"}{current_score}")
            game_over = True

    elif compare == "b":
        if backB > back:
            current_score += 1
            print(f"{"u are right"} {":"}{"your current score"}{"="}{current_score}")

            randA = randB

            # New B
            randB = random.choice(data)

            while randA == randB:
                randB = random.choice(data)
        else:
            print(f"{"sorry"} {"thats wrong"} {"final_score:"}{current_score}")
            game_over = True






