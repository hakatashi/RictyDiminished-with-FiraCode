# -*- coding: utf-8 -*-

from fontTools import ttLib
from fontTools.feaLib.builder import addOpenTypeFeatures
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('in_font')
parser.add_argument('out_font')
options = parser.parse_args(sys.argv[1:])

# Apply generated feature file to the unlinked font file
ricty = ttLib.TTFont(options.in_font)
addOpenTypeFeatures(ricty, 'ligatures.fea')
ricty.save(options.out_font)
