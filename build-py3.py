import fontforge
import psMat
import csv
import os

with open('ligatures.csv', 'rb') as file:
    ligatures = csv.reader(file, delimiter=' ')
    glyphs = [glyph for [ligature, glyph] in ligatures]

ricty = fontforge.open('RictyDiminished/RictyDiminished-Regular.ttf')
fira = fontforge.open('FiraCode/distr/otf/FiraCode-Regular.otf')

for glyph in glyphs:
    ricty.createChar(-1, glyph)
    fira.selection.select(glyph)
    fira.copy()
    ricty.selection.select(glyph)
    ricty.paste()

try:
    os.remove('test.ttf')
except OSError:
    pass
ricty.generate('test.ttf')
