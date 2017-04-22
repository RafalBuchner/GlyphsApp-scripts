"""
	this script allows to copy paths stored in masters
	to another glyphs with one click
"""
Glyphs.clearLog()
font = Glyphs.font
myLayers = font.selectedLayers
layer = myLayers[0]
currGlyph = layer.parent

tempLayer = GSLayer()

# print currGlyph.lay

# listing indexes of selected paths

# 1 - list contains pairs of nodes' and paths' indexes
###!!!!!!### Jednak należy nie szukać przez node, ale przez segments, które są tuplami( trzeba na hakować trochę)
nodesAndPathsIndexes = []
for path in layer.paths:
	for node in path.nodes:
		if node.selected:
			nodesAndPathsIndexes.append([
				node.index,
				layer.paths.index(path)
			])


# print selectedPaths

masterLayers = []
for glyph in font.glyphs:

	if glyph.name == currGlyph.name:
		for layer in glyph.layers:
			for master in font.masters:
				if layer.name == master.name:
					masterLayers.append(layer)

for masterLayer in masterLayers:
	for nodeAndPathIndex in nodesAndPathsIndexes:
		nodeIndex = nodeAndPathIndex[1]
		pathIndex = nodeAndPathIndex[2]
		print nodeIndex
		print pathIndex
		print masterLayer.paths[pathIndex].nodes[nodeIndex]
