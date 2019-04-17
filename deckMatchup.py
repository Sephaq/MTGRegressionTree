
from dataclasses import dataclass

@dataclass
class deckMatchup:
	format: str
	archetype: str
	oponentArchetype: str
	games: int
	victories: int
	losses: int

	def __init__(self,format: str, archetype: str, oponentArchetype: str, games: int, victories: int, losses: int):
		self.format = format
		self.archetype = archetype
		self.oponentArchetype = oponentArchetype
		self.games = games
		self.victories = victories
		self.losses = losses
