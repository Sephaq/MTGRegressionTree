from dataclasses import dataclass

@dataclass
class deckMatchup:
	format: str
	archetype: str
	oponentArchetype: str
	games: int
	victories: int
	victoryPercentage: float

	def __init__(self,format: str, archetype: str, oponentArchetype: str, games: int, victories: int):
		self.format = format
		self.archetype = archetype
		self.oponentArchetype = oponentArchetype
		self.games = games
		self.victories = victories
		self.victoryPercentage = self.victories/self.games

	def winPercentage(self) -> float:
		return self.victoryPercentage

	def addGames(self, games: int):
		self.games += games

	def addVictoties(self, victories: int):
		self.victories += victories

	def deckMatchup(self, archetype: str, oponentArchetype: str) -> bool:
		if self.archetyp == archetype and self.oponentArchetype == oponentArchetype:
			return true
