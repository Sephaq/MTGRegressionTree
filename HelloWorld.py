import csv
from deckMatchup import deckMatchup

with open ('decksDatabase.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Colum names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t No {row[0]} de {row[1]} jogador: {row[2]}, com baralho {row[3]}, contra baralho: {row[4]} e oponente {row[5]}, com resultado V = {row[6]}, D = {row[7]}.  ')
            line_count += 1
print(f'Processed{line_count} lines')

decks = deckMatchup('Modern','UB Combo','UW Control',20,9)
print (decks.winPercentage())
