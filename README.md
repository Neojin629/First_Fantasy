# First_Fantasy
An "RPG" created as a portfolio project for my bootcamp.  

Portfolio Project - “First Fantasy”

Introduction: 

I decided to make a “pick-your-own” adventure game that would have several outcomes depending on your choices throughout the game.  Essentially a player can choose a character and weapon.  Face against randomized enemies and encounter environmental hazards.  Finally at the end, the character battles a dragon to save the kingdom.  

Design and Implementation:

At first, my idea for my game seemed simple in my head, however, the actual implementation didn’t take place until after our OOP week.  This helped me remove a lot of repetitious code for characters, weapons and hazards I had originally created without OOP.   

I knew I wanted some ASCII art since this was an adventure game so I looked up how I could do this.  Simple art.py file that I could import some variables to print when I needed them. 

I created dictionaries that would print out choices the player could make for characters and weapons.  I could’ve used lists but I wanted to display a numeric value for the characters HP that was chosen.  

I couldn’t figure it out at first but I wanted the game only to randomly throw obstacles at the player for a limited amount of time, otherwise the game would never end.  I decided to start a While Loop for the adventure after character selection.  I also used an input statement to break up every Loop so that the Player can catch up and read what just happened in the game.  Finally I assigned an “adventure” variable a value of zero so that my loop would count down from 5.

Finally, once this Loop ends, a final battle begins with the character battling the dragon. 

Conclusions:

I learned a lot during this project and it was truly fun to do.  The best part was being able to use OOP (which I never have done before in Python) and start to understand how it works.  
I feel the best feature of this game is the fact that no play through should be the same based on the randomization created by the code.  Also, the player’s choices will add additional variety to the game.
Shortcomings really come down to the limitations of the loops I used.  For example, during every encounter, the same “You damaged the [enemy]” message would print.  Making the game repetitious.  
In hindsight, I would research how to minimize the use of so many IF and ELSE statements. It made the code for the game really long, almost 300 lines of code in total.  Definitely the longest block of code I have written.  
For additional features, I feel like a scorekeeper or maybe even like “Tries remaining” feature would be cool.  So that if you lose, you have more tries instead of having to restart the program again.  
