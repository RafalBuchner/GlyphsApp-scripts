"""
	this script allows to copy paths stored in masters
	to another glyphs with one click
"""
import copy
Glyphs.clearLog()
font = Glyphs.font
myLayers = font.selectedLayers
layer = myLayers[0]
currGlyph = layer.parent

# print currGlyph.layers
destGlyph_name = "y" #USER-input: Glyph of destination


# listing indexes of selected paths

# 1 - list contains paths's indexes from origin-layer
selectedPathsOrginalIndexes = []
print "\n>> >> >> coping from layer: {}\n".format(layer)

for path in layer.paths:
	if path.selected:
		selectedPathsOrginalIndexes.append(layer.paths.index(path))


# 2 - script makes sure that it will add paths only to the masters
masterLayersDestination = []
masterLayersOrigin = []
for glyph in font.glyphs:

	if glyph.name == currGlyph.name:
		for layer in glyph.layers:
			for master in font.masters:
				if layer.name == master.name:
					masterLayersOrigin.append(layer)

	elif glyph.name == destGlyph_name:
		print "\n>> >> >> coping to glyph: {}\n".format(glyph)
		for layer in glyph.layers:
			for master in font.masters:
				if layer.name == master.name:
					masterLayersDestination.append(layer)


# coping selected paths from the origin to the destination
for masterLayerOrg in masterLayersOrigin:
	masterIndex = masterLayersOrigin.index(masterLayerOrg)

	# for each selected path do some actions
	for i in selectedPathsOrginalIndexes:
		copyPath = GSPath()
		copyPath.segments = masterLayerOrg.paths[i].segments
		copyPath.closed = masterLayerOrg.paths[i].closed
		del(copyPath.nodes[0])

		# makes sure that copied smooth nodes stay smooth
		nodes = masterLayerOrg.paths[i].nodes
		for node in nodes:
			if node.smooth:
				 copyPath.nodes[nodes.index(node)].smooth = True

		print "\n>> >> >> from master: {}\n>> >> >> copying path: {}\n>> >> >> to the following master: {}".format(masterLayersOrigin[masterIndex],copyPath,masterLayersDestination[masterIndex])
		masterLayersDestination[masterIndex].paths.append(copyPath)
