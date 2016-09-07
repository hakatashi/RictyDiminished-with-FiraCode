from fontTools import ttLib
from fontTools.feaLib.builder import addOpenTypeFeatures

ricty = ttLib.TTFont('test.ttf')
addOpenTypeFeatures(ricty, 'ligatures.fea')
ricty.save('ricty.ttf')
