import fontforge
import psMat
import csv

with open('ligatures.csv', 'rb') as file:
    ligatures = csv.reader(file)

ricty = fontforge.open('RictyDiminished/RictyDiminished-Regular.ttf')
fira = fontforge.open('FiraCode/distr/otf/FiraCode-Regular.otf')

ricty.createChar(-1, 'equal_greater.liga')
fira.selection.select('equal_greater.liga')
fira.copy()
ricty.selection.select('equal_greater.liga')
ricty.paste()

ricty.generate('test.ttf')
