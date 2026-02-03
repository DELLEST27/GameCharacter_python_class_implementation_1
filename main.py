# main.py
import random  
from module import GameCharacter
# TASK:
# Make a prototype game using the GameCharacter class.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# -----------------------------------------
# TODO 1:
# Print a message that welcomes the user to this game.# 

print("Hello travler welcom to the game")

# TODO 2:
# Ask the user to name their character and store it in a variable.
Characters_name = ("what is your name?", input )


# TODO 3:
# Assign a power and a toughness value to the character.
# (Use any integers you like between 1 and 20.)
power= 13
toughness= 17
    

# TODO 4:
# Create a new GameCharacter object for the player.
player= (GameCharacter, power, toughness) 

# TODO 5:
# Create a new GameCharacter object for an enemy.
# The enemy's name can be something like "Goblin" or "Dragon".
# Give the enemy its own power and toughness values.
enemy = (power, toughness)
enemy_health = 4
# TODO 6:
# Print both characters' statuses.


# TODO 7:
# Print the player's attack message.
# Then make the enemy take damage equal to the player's power.
print ("you attacked the enemy for 4 damage")
player_damage = (int(enemy_health - 4))

# TODO 8:
# Print the enemy's updated status.
if player_damage true:
    print(enemy_health)

# TODO 9:
# Print the enemy's attack message.
# Then make the player take damage equal to the enemy's power.
enemy_damage = (int(player_health - 2))

# TODO 10:
# Update the player's name property to be "Lord " + the original name

# TODO 11: 
# Heal the player by 100 hitpoints


# TODO 11:
# Print the player's updated status.


# TODO 12:
# Modify the GameCharacter class so a "defeated" message is printed if health goes to 0 or less


# TODO 13:
# Go back and make it so the player gets a random Power and Toughness between 1 and 20.

# -----------------------------------------