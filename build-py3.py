# -*- coding: utf-8 -*-

import fontforge
import textwrap
import argparse
import psMat
import json
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('ricty')
parser.add_argument('firacode')
parser.add_argument('out_font')
options = parser.parse_args(sys.argv[1:])

ricty = fontforge.open(options.ricty)
firacode = fontforge.open(options.firacode)

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

    if glyph.endswith('.svg'):
        ricty[glyph].importOutlines('svg/' + glyph)
        ricty[glyph].width = 500
    else:
        firacode.selection.select(glyph)
        firacode.copy()
        ricty.selection.select(glyph)
        ricty.paste()

        ricty.transform(psMat.scale(500 / 600))

ricty.familyname = 'Ricty Diminished with Fira Code'
ricty.fontname = 'RictyDiminishedWithFiraCode-Regular'
ricty.fullname = 'Ricty Diminished with Fira Code Regular'
ricty.weight = 'Regular'

ricty.copyright = textwrap.dedent('''\
    Copyright (c) 2012-2014 Yasunori Yusa
    Copyright (c) 2006 Raph Levien
    Copyright (c) 2006-2013 itouhiro
    Copyright (c) 2002-2013 M+ FONTS PROJECT
    Copyright (c) 2014 Mozilla Foundation
    Copyright (c) 2014 Telefonica S.A.
    Copyright (c) 2014 Nikita Prokopov
    Copyright (c) 2016 Koki Takahashi
    License:
    SIL Open Font License Version 1.1 (http://scripts.sil.org/ofl)
''')

# Export
try:
    os.remove(options.out_font)
except OSError:
    pass
ricty.generate(options.out_font)
