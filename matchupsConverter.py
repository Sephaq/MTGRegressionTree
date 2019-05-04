import csv
from deckMatchup import deckMatchup

decks = []
with open ('decksDatabase.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Colum names are {",".join(row)}')
            line_count += 1
        else:
            deck = row[5]
            # print(deck)
            opponent = row[7]
            # print(opponent)
            matchup = deck+opponent
            opponentMatchup = opponent+deck
            print(matchup)
            victories = int(row[10])
            # print(victories)
            defeats = int(row[11])
            # print(defeats)
            games = victories + defeats
            # print(games)
            winPercentage = victories/games
            opponentWP = defeats/games
            # print(winPercentage)
            gameFormat = row[0]
            # print(gameFormat)
            decks.append(deckMatchup(gameFormat,matchup,deck,opponent,games,victories,defeats,winPercentage))
            decks.append(deckMatchup(gameFormat,opponentMatchup,opponent,deck,games,defeats,victories,opponentWP))
            line_count += 1

print(f'Processed {line_count} lines')

with open('matchupsDatabase.csv',mode='w') as csv_file:
    outfile = csv.writer(csv_file)
    outfile.writerow(['Format','Matchup','Deck', 'OpponentDeck', 'Games', 'Victories', 'Losses', 'WinPercentage'])
    for game in decks:
        # outfile.writerows(game)
        outfile.writerow([game.format,game.matchup,game.archetype,game.oponentArchetype,game.games,game.victories,game.losses,game.winPercentage])
