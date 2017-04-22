
font = Glyphs.font
fontMaster = font.masters[0]
descender = fontMaster.descender
ascender = fontMaster.ascender




for glyph in font.glyphs:
	layer = glyph.layers[0]
	layer.clear()
	print layer.width
	start = 0
	dis = 10
	aGS = GSNode()
	aGS.type = GSLINE
	aGS.position = (start + dis,descender)
	
	bGS = GSNode()
	bGS.type = GSLINE
	bGS.position = (start + dis,ascender)
	
	cGS = GSNode()
	cGS.type = GSLINE
	cGS.position = (start + layer.width - dis,ascender)
	
	dGS = GSNode()
	dGS.type = GSLINE
	dGS.position = (start + layer.width - dis,descender)
	
	pathGS = GSPath()
	pathGS.nodes.append(aGS)
	pathGS.nodes.append(bGS)
	pathGS.nodes.append(cGS)
	pathGS.nodes.append(dGS)
	pathGS.closed = True
	paths = layer.paths
	

	paths.append(pathGS)


