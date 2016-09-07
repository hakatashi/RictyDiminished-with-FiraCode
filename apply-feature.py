# -*- coding: utf-8 -*-

from fontTools import ttLib
from fontTools.feaLib.builder import addOpenTypeFeatures

# Apply generated feature file to the unlinked font file
ricty = ttLib.TTFont('test.ttf')
addOpenTypeFeatures(ricty, 'ligatures.fea')
ricty.save('ricty.ttf')
