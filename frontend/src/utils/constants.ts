export const STAKE_NAMES = {
	1: 'White',
	2: 'Red',
	3: 'Green',
	4: 'Black',
	5: 'Blue',
	6: 'Purple',
	7: 'Orange',
	8: 'Gold',
}

export const DECK_NAMES = [
	'b_red',
	'b_blue',
	'b_green',
	'b_nebula',
	'b_abandoned',
	'b_checkered',
	'b_anaglyph',
	'b_plasma',
	'b_erratic',
	'b_magic',
	'b_ghost',
	'b_painted',
	'b_black',
	'b_zodiac',
	'b_yellow',
]

export const RARITY_NAMES = {
	1: 'Common',
	2: 'Uncommon',
	3: 'Rate',
	4: 'Legendary',
}

export type StakeLevel = keyof typeof STAKE_NAMES
export type RarityLevel = keyof typeof RARITY_NAMES
