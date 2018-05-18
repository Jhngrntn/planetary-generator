import random

climate = [
	'an arid',
	'a frozen',
	'a lush',
	'a desert',
	'a rocky',
	'a frosty',
	'an ocean',
	'a bare',

]

planet = [
	'moon of a gas giant',
	'mesoplanet',
	'moon around a mini-gaseous planet',
	'dwarf planet',
	'goldilocks planet',
	'exoplanet',

]

star = [
	'a red giant',
	'a red supergiant',
	'a blue giant',
	'a white dwarf',
	'a yellow dwarf',
	'a red dwarf',
	'a brown dwarf',
	'a neutron star',
	'a black hole',
	'a pulsar',
	'a double star',
	'a binary star',
	'an eclipsing binary star',
	'a cepheid variable star',
	'a yellow star',
	'an orange star',

]

quality = [
	'shifting gravity',
	'an uneven rotation',
	'a crater-rittled surface',
	'an adanced insectoid race',
	'ruins of a formerly advanced alien race',
	'poisoness gas in its atmosphere',
	'primitive lifeforms',

]

climate_r = climate[random.randrange(len(climate))]
planet_r = planet[random.randrange(len(planet))]
star_r = star[random.randrange(len(star))]
quality_r = quality[random.randrange(len(quality))]

print(climate_r + " " + planet_r + " orbiting " + star_r + " with " + quality_r)