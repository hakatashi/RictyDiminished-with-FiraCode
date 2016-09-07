# -*- coding: utf-8 -*-

import fontforge
import psMat
import json
import csv
import os

ricty = fontforge.open('RictyDiminished/RictyDiminished-Regular.ttf')
firacode = fontforge.open('FiraCode/distr/otf/FiraCode-Regular.otf')

# Load ligatures data and create data to generate feature file
with open('ligatures.csv', 'rb') as file:
    ligatures_reader = csv.reader(file, delimiter=' ')

    ligatures = []
    nullable_glyphs = []
    glyphs = []

    for [components, glyph] in ligatures_reader:
        glyphs.append(glyph)
        component_names = list(map(lambda c: ricty[ord(c)].glyphname, list(components)))

        nullable_glyphs.extend(component_names[:-1])

        ligatures.append({
            'glyph': glyph,
            'components': component_names,
            'lookup': '_'.join(map(lambda name: name.upper(), component_names)),
        })

# Unique
nullable_glyphs = list(set(nullable_glyphs))

# Dump data
with open('data.json', 'w') as file:
    file.write(unicode(json.dumps({
        'ligatures': ligatures,
        'nullable_glyphs': nullable_glyphs,
    })))

# Copy needed glyphs from Fira Code font to Ricty
for glyph in glyphs:
    ricty.createChar(-1, glyph)
    firacode.selection.select(glyph)
    firacode.copy()
    ricty.selection.select(glyph)
    ricty.paste()

    ricty.transform(psMat.scale(500 / 600))

# Export
try:
    os.remove('test.ttf')
except OSError:
    pass
ricty.generate('test.ttf')
