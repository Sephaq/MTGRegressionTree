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
            # print(f'\t No {row[0]} de {row[1]} jogador: {row[2]}, com baralho {row[3]}, contra baralho: {row[4]} e oponente {row[5]}, com resultado V = {row[6]}, D = {row[7]}.  ')
            deck = row[3]
            print(deck)
            opponent = row[4]
            print(opponent)
            victories = int(row[6])
            print(victories)
            defeats = int(row[7])
            print(defeats)
            games = victories + defeats
            print(games)
            gameFormat = row[0]
            print(gameFormat)
            decks.append(deckMatchup(gameFormat,deck,opponent,games,victories,defeats))
            decks.append(deckMatchup(gameFormat,opponent,deck,games,defeats,victories))
            line_count += 1

print(f'Processed {line_count} lines')
print('Teste')
print(f'Deck: {decks[0].archetype}, Matchup: {decks[0].oponentArchetype}, Games:{decks[0].games}, Victories:{decks[0].victories}, Losses:{decks[0].losses}')

with open('matchupsDatabase.csv',mode='w') as csv_file:
    outfile = csv.writer(csv_file)
    outfile.writerow(['Format', 'Deck', 'Matchup', 'Games', 'Victories', 'Losses'])
    for game in decks:
        # outfile.writerows(game)
        outfile.writerow([game.format,game.archetype,game.oponentArchetype,game.games,game.victories,game.losses])
