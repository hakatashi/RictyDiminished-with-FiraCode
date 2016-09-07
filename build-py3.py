import fontforge
import psMat
import csv

from fonttools import ttLib, feaLib

with open('ligatures.csv', 'rb') as file:
    ligatures = csv.reader(file)

ricty = fontforge.open('RictyDiminished/RictyDiminished-Regular.ttf')
fira = fontforge.open('FiraCode/distr/otf/FiraCode-Regular.otf')

ricty.createChar(-1, 'equal_greater.liga')
fira.selection.select('equal_greater.liga')
fira.copy()
ricty.selection.select('equal_greater.liga')
ricty.paste()

ricty.addLookup('nullify', 'gsub_single', (), (
    ('aalt', (
        ('DFLT', ('dflt')),
        ('cyrl', ('dflt')),
        ('grek', ('dflt')),
        ('hani', ('dflt')),
        ('kana', ('JAN ', 'dflt')),
        ('latn', ('dflt'))
    )),
))

ricty.addLookupSubtable('nullify', 'nullify subtable')

ricty['equal'].addPosSub('nullify subtable', 'asciitilde')

ricty.addLookup('ligatures', 'gsub_contextchain', (), (
    ('calt', (
        ('DFLT', ('dflt')),
        ('cyrl', ('dflt')),
        ('grek', ('dflt')),
        ('hani', ('dflt')),
        ('kana', ('JAN ', 'dflt')),
        ('latn', ('dflt'))
    )),
))

ricty.addLookupSubtable('ligatures', 'ligatures subtable')

ricty.save('test.sfd')
