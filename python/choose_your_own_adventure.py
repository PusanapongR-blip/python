name = input("Enter your name: ")
print(f"Welcome, {name}, to the Choose Your Own Adventure game!")

answer = input("You find yourself at a crossroads. Do you want to go left or right? (left/right): ").lower()

if answer == "left":
  print("You encounter a monster and lose the game!")
elif answer == "right":
  answer = input("You find a hidden treasure chest. Do you want to open it? (yes/no): ").lower()
  if answer == "yes":
    print("It was a mimic! You were eaten alive! You lose the game!")
  elif answer == "no":
    answer = input("You safely walk away and find a peaceful village. Do you want to stay there? (yes/no): ").lower()
    if answer == "yes":
      print("You live happily ever after in the village. You win the game!")
    elif answer == "no":
      print("You venture back into the wild and get lost. You lose the game!")
    else:
      print("You have the true heart of an adventurer to seek for your own path. You win the game!")
  else:
    print("You have the true heart of an adventurer to seek for your own path. You win the game!")
else:
  print("You have the true heart of an adventurer to seek for your own path. You win the game!")

print("Thanks for playing Choose Your Own Adventure Demo! You can save it as a Wishlist in Steam for later. Estimated release date is 32 December 5555. Buy now for an exclusive discount of 0%! Only $5555555.55! Buy now! Buy please!")