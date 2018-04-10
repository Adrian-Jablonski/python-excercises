# Hero RPG V3

This game is a pygame version of my Hero RPG V2 text RPG game. https://github.com/Adrian-Jablonski/python-exercises/tree/master/Hero_RPG_V2

## GamePlay:

### 1. Main Menu:

Start the game from the terminal and then click New Game. Create a new character by typing in a character name.

To load a previous game, click Load Game and then select game to load by typing the game number.

### 2. Characters:
### a. Hero (Player) - Players character.  
	- Special attack - generates 2x damage 20% of the time.
### b. Goblin
	- Special Attack - none
### c. Medic	
	- Special Attack - Heals itself the same amount as that turns attack 20% of the time
### d. Shadow
	- Special Ability - Only takes damage 10% of the time it is attacked
### e. Wizard
	- Special Attack - Freezes Hero for one move 20 % of the time not allowing Hero to run away or drink Tonic
### f. Ranger
	- Special Attack - Shoots two arrows in one move 20 % of the times
### g. Zombie
	- Special Ability - Does not die unless head is chopped off with a special axe
### h. Dragon
	- Special ability - Breathes fire 33% of the time and automatically kills it's enemies that do not have a special shield


### 3. Controls:

The game is played by left clicking on where you want the character to go or which enemy you want the character to attack. 
Hovering over enemies will show you their stats. Hovering over the edge of the map will show you if it is possible to go to another section of the map.

### 4. Fighting:

### a. Combat Stances 
###     i. Aggressive 
        - Trains Power and Health.
        - Adds a bonus to Power at the cost of Defense
###     ii. Defensive 
        - Trains Defense and Health
        - Adds a bonus to Defense at the cost of Power
###     iii. Normal 
        - Trains all three skills
        - Skill levels stay as they are

### b. Long Range Attacking
        - The wizard, ranger, and dragon are able to attack from long range

### c. Auto Attacking
        - Higher level enemies will automatically attack you if you are within their attack range

### 5. Skill Levels:

Skills are leveled up after reaching the next level experience. This game has an exponential leveling system.

### 6. Bounty and enemy death:

After killing an enemy you will receive coins. The amount of coins is based on each enemy character. Each enemy character can drop a range of coin amounts so the drop will not be the same each time the enemy is killed. 

The enemy will respawn in a few seconds based on their respawn timer.

### 7. Moving to another section of the map:

You could move to another section of the map by moving the character to the edge of the map where there is an option to go to another section.

### 8. Store, Inventory, and Equipment:

### a. Store

Items could be bought from the store by typing in the number of the item you would like to buy. Pressing 9 will exit the store.

### b. Inventory

The only inventory item for now is a healing potion which can heal 10 Health. It can be used during or after battles. Using it during battle may cost you a turn in the battle.

### c. Equipment

This is not set up yet but the equipment will give additional bonus's to Power and Defense.

### 9. Hero Death:

Upon hero death, you will lose most of your coins and all your inventory and equipment.