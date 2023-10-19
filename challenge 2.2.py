
# Define the base class Player
Class Player: 
    Def play(self):
        Print(“The player is playing cricket.”)

# Define the derived class Batsman
Class Batsman (Player):
    Def play(self):
        Print(“The batsman is batting.”)

# Define the derived class Bowler
Class Bowler (Player): 
    Def play(self):
        Print(“The bowler is bowling.”)

# Create objects of Batsman and Bowler classes
Batsman = Batsman()
Bowler = Bowler()

# Call the playt() method for each object
Batsman.play()
Bowler.play()