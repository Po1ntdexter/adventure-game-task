# THE LOST TEMPLE - BEGINNER
print("=== THE LOST TEMPLE ===")
name = input("What is your name, explorer? ")
print(f"Welcome, {name}! You stand at the temple entrance.")

print("\n1. Enter the dark corridor")
print("2. Explore the courtyard")
choice = input("Choose 1 or 2: ").strip()

if choice == "1":
    print("You enter the dark corridor.")
    #  Ask whether to open the stone door (yes/no).
    stone_door = input("Do you want to open the stone door? (yes/no): \n").strip()
    #  Display a different outcome for each answer.
    if stone_door == ("yes" or "y"):
        print("You are entering the dark corridor.\n")
    else:
        print("You are not entering the dark corridor.\n")

elif choice == "2":
    print("You find an overgrown courtyard.\n")
    # Ask whether to climb the tower (yes/no).
    climb_tower = input("Do you want to climb tower? (yes/no): \n").strip()

    #  Display a different outcome for each answer.
    if climb_tower == ("yes" or "y"):
        print("You are climbing the tower.\n")
    else:
        print("You are not climbing the tower.\n")

else:
    print("That is not a valid route.\n")

# Print a closing message for the player.
print(f"Thank you {name} for visiting the lost jungle. \nHope to see you again! \n\nRemember...More objects are waiting to be discovered.")
print("=== THE LOST TEMPLE ===\n")
