import csv
from playedDeck import playedDeck

playedDecks = []
with open ('decksDatabase.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Colum names are {",".join(row)}')
            line_count += 1
        else:
            gameFormat = row[0]
            print(gameFormat)
            dateTime = row[1]
            print(dateTime)
            player_1 = int(row[3])
            print(player_1)
            player1Deck = int(row[5])
            print(player1Deck)
            player_2 = int(row[9])
            print(player_2)
            player2Deck = int(row[7])
            print(player2Deck)

            playedDecks.append(playedDeck(gameFormat,player_1,player1Deck,dateTime))
            playedDecks.append(playedDeck(gameFormat,player_2,player2Deck,dateTime))
            # decks.append(deckMatchup(gameFormat,matchup,deck,opponent,games,victories,defeats,winPercentage))
            # decks.append(deckMatchup(gameFormat,opponentMatchup,opponent,deck,games,defeats,victories,opponentWP))
            line_count += 1

playedDecks = list(dict.fromkeys(playedDecks))
for i in playedDecks:
	print(i,end ="\n")

# print(f'Processed {line_count} lines')

with open('deckRepresentativity.csv',mode='w') as csv_file:
    outfile = csv.writer(csv_file)
    outfile.writerow(['Format','Date','Player_ID', 'Deck_ID'])
    for played in playedDecks:
#         # outfile.writerows(game)
        outfile.writerow([played.gameFormat,
        	played.date,
        	played.playerId,
        	played.deckId])
