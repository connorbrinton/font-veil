# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import fontforge

# <codecell>

fontFileName = "../../assets/Georgia.ttf"

# <codecell>

font = fontforge.open(fontFileName)

# <codecell>

font.familyname = font.familyname+"-Blank"
font.fontname = font.fontname+"-Blank"
font.fullname = font.fontname+"-Blank"

# <codecell>

for glyph in font.glyphs():
    if glyph.unicode != -1 and glyph.unicode != 95:
        glyph.layers[0] = fontforge.layer()
        glyph.layers[1] = fontforge.layer()

# <codecell>

#for glyph in font.glyphs():
#    if glyph.unicode != -1 and glyph.unicode != 95:
#        resizedContour = font[95].layers[1][0].dup()
#        # The -5 compensates for underscores hanging 5 pixels to the left of their box
#        rightEdge = glyph.width - 5
#        resizedContour[0].x = rightEdge
#        resizedContour[3].x = rightEdge
#        glyph.layers[1] += resizedContour

# <codecell>

outputFileName = fontFileName[0:fontFileName.rindex(".")] + "-Blank" + fontFileName[fontFileName.rindex("."):len(fontFileName)]
font.generate(outputFileName)

