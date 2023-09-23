'''this program has one base class and two sub class'''

#Define the base class "Player"
class Player:
	def play(self):
		print("The player is  playing cricket.")

#Define the derived class "Batsman"
class Batsman(Player):
	def play(self):
		print("The batsman is batting. ")

#Define the derived class "Bowler"
class Bowler(Player):
	def play(self):
		print("The bowler is bowling.")

#Creating objects for tow subclass Batsman & Bowler 
batsman = Batsman()
bowler = Bowler()

#Calling the play() method for both objects
batsman.play()
bowler.play()
