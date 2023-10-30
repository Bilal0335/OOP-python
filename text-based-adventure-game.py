print(f"*****************************************")
print("Welcome to the Text-Based Adventure Game!")
print(f"*****************************************\n")
#Introduction
print("You find yourself in front of a mysterious cave entrance.")
print("Do you dare to enter? (yes/no)")
choice = input().lower()

if choice == "yes":
               
               print("You gather your courage and step inside the cave.")
               print("You enter a adark tunnel. It's getting colder.")

               #Cave Exploration
               print(f"You see two passages. Which one do you choose? (left/right)")
               choice=input().lower()

               if choice == "left":
                       print("You venture deeper into the cave.")
                       print(f"You find a hidden treature chest. You're rich!")
               elif choice=="right":
                        print("You hear growling and see glowing eyes in the darkness.")
                        print("A wild beast attacks you. \n Game Over!")
               else:
                       print("Invalid choice. You're paralyzed with fear.\n Game Over!")

else:
    print("You turn and run away from the cave, never to return.\n")

print("Thanks for playing!")
                    