(define (problem nosliw-7-0)
(:domain nosliw)
(:objects
	 ai - hero
	 nosliw - dragon
	 sarorah - sorceress
	 whitebeard - wizard
	 bard - agent
	 pointy - sword
	 quill - pen
	 amulet - item
	 spellbook - item
	 talisman - item
	 d1 d2 d3 - diamond
	 happydale - town
	 blueforest - location
	 fortwood - location
	 mtkillemall - mountain
	 suntheatre - location
	 lakeoftheclouds - location
	 darkcave - cave

)

(:init (at ai suntheatre)
	(path-from-to happydale blueforest)
	(path-from-to happydale suntheatre)
	(path-from-to blueforest mtkillemall)
	(path-from-to blueforest fortwood)
	(path-from-to suntheatre lakeoftheclouds)
	(path-from-to fortwood happydale)
	(path-from-to lakeoftheclouds blueforest)
	(path-from-to lakeoftheclouds mtkillemall)
	(path-from-to mtkillemall fortwood)
	(path-from-to mtkillemall darkcave)
	(path-from-to darkcave lakeoftheclouds)

 )

(:goal (and (at ai happydale))
))