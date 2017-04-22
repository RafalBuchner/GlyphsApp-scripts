Glyphs.clearLog()
font = Glyphs.font
myLayers = font.selectedLayers
layer = myLayers[0]
glyph = layer.parent
# kontrolka do tego, czy jest cokolwiek zaznaczone:
thereIsSelection = False ###test

# tu tworzę element dict-a, jeśli jeszcze nie został wcześniej stworzony:
# ma za zadanie on liczyć ilość smartNode'ów
if len(glyph.userData) == 0:
	glyph.userData['smartNodeCount'] = 0

for thisLayer in myLayers:
	print thisLayer.parent ###test
	for path in thisLayer.paths:
		for node in path.nodes:
			# jeśli: node.jest.wybrany oraz node.jest.miękkim oraz node nie jest wewnątrz glyph.userData
			if node.selected and node.smooth and not node in glyph.userData:
				thereIsSelection = True ###test
			###opcja na skrypt
			 	glyph.userData['smartNodeCount'] += 1
			 	glyph.userData['smartNode' + str(glyph.userData['smartNodeCount'])] = node
			else:
				pass

print glyph.userData ###test

###test === sposob na usowanie wszystkiego z userData, lepiej aby był wyłączony
###     === trzeba zrobić osobny skrypt na odznaczanie, usowanie elementów userData
if not thereIsSelection: ###test
	print u"no node selected" ###test
	for data in glyph.userData.keys(): ###test usówa zawartość dict userData
		del glyph.userData[data]

# list(glyph.userData)[2].x = 0 ###test na indeksowanie elementow w dict
