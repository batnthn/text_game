from character_types import *


def main():
    print("Welcome to the Forgotten Meadows adventurer!")
    hero_type = input("First things first lets make a choice. Would you like to be a warrior or ranger?\n")

    if (hero_type == "warrior"):
        hero_type = Warrior
        print(f"As a warrior you have {hero_type.health} health")
    elif (hero_type == "ranger"):
        hero_type = Ranger
        print(f"As a ranger you have {hero_type.health} health")
    else:
        print("Incorrect input for hero type")



    


if __name__ == "__main__" :
    main()