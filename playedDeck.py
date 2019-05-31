
from dataclasses import dataclass

@dataclass
class playedDeck:
	date: str
	gameFormat: str
	playerId: int
	deckId: int

	def __init__(self,gameFormat: str, playerId: int, deckId: int, date: str):
		self.date = date
		self.gameFormat = gameFormat
		self.playerId = playerId
		self.deckId = deckId

	def __eq__(self,othr):
		return (isinstance(othr,type(self))) and (self.date,self.gameFormat,self.playerId,self.deckId) == (othr.date,othr.gameFormat,othr.playerId,othr.deckId)

	def __hash__(self):
		return (hash(self.date) ^ hash(self.gameFormat) ^ hash(self.playerId) ^ hash(self.deckId))
