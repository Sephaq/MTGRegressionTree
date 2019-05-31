
from dataclasses import dataclass

@dataclass
class deckMatchup:
	format: str
	matchup: str
	archetype: str
	oponentArchetype: str
	games: int
	victories: int
	losses: int
	winPercentage: float

	def __init__(self,format: str, matchup: str, archetype: str, oponentArchetype: str, games: int, victories: int, losses: int, winPercentage: float):
		self.format = format
		self.matchup = matchup
		self.archetype = archetype
		self.oponentArchetype = oponentArchetype
		self.games = games
		self.victories = victories
		self.losses = losses
		self.winPercentage = winPercentage
