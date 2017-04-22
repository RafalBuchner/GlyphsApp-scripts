"""
	THIS SCRIPT DOESNT WORK!!!YET
"""
Glyphs.clearLog()
font = Glyphs.font
myLayers = font.selectedLayers
layer = myLayers[0]
currGlyph = layer.parent

# 1 - list contains pairs of nodes' and paths' indexes
###!!!!!!### Jednak należy nie szukać przez node, ale przez segments, które są tuplami( trzeba na hakować trochę)
selectedNodes = []
for path in layer.paths:
	for node in path.nodes:
		if node.selected:
			selectedNodes.append(node)
			del(path.nodes[node.index])

for path in layer.paths:
	for segment in path.segments:
		for node in segment:
			for selectedNode in selectedNodes:
				selectedNode = None
