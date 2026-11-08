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

# THE LOST TEMPLE - INTERMEDIATE
rooms = {
    "entrance": {
        "description": "You are at the temple entrance.",
        "exits": {"north": "hall"},
        "item": None
    },
    "hall": {
        "description": "Torches flicker along a long hall.",
        "exits": {"south": "entrance", "east": "vault"},
        "item": "bronze key"
    },
    "vault": {
        "description": "A sealed chest stands in the vault.",
        "exits": {"west": "hall", "south": "spook maze"},
        "item": "treasure"
    },
    "spook maze": {
        "description": "This is the scarecrow maze.",
        "exits": {"west": "entrance", "north": "vault"},
        "item": "skeleton" 
    }
}

current_room = "entrance"
inventory = []
running = True

def show_room():
    room = rooms[current_room]
    print("\n" + room["description"])
    print("Exits:", ", ".join(room["exits"]))
    print("Item:", room["item"] or "none")

while running:
    show_room()
    command = input("\nMove (direction), take, bag or quit: ").lower().strip()

    if command == "quit":
        running = False

    elif command == "bag":
        if inventory == []:
            print("There are no items in the inventory. ")
        else:
            print("Inventory:", inventory)

    elif command == "take":
        # Check if the current room has an item.
        if not rooms[current_room]["item"] == None:
        # Add the item to inventory.
        # Set the room item to None.
            inventory.append(rooms[current_room]["item"])
            rooms[current_room]["item"] = None
        else:
            print("There are no items in this room. ")

        
        

    elif command in rooms[current_room]["exits"]:
        next_room = rooms[current_room]["exits"][command]
        # Require the bronze key before entering the vault.
        if next_room == "vault" and "bronze key" not in inventory:
            print("You need the bronze key to enter the vault. ")
        # Otherwise change current_room to next_room.
        else:
            current_room = rooms[current_room]["exits"][command]
        

    else:
        print("Unknown command.")

# Print a victory message if treasure was collected.
print("Well done!! Treasure was collected. ")


