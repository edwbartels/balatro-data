import React, { useState, useEffect } from 'react'
import useDeckStore, { Deck } from '../../stores/deckStore'
import { toPercent } from '../../utils/formatting'
import LineChartComponent from './DeckLineChart'

interface DeckTileProps {
	deckId: string
}

const DeckTile: React.FC<DeckTileProps> = ({ deckId }) => {
	const deck: Deck = useDeckStore((state) => state.decks[deckId])

	if (!deck) {
		return <>Error: Deck Not Found</>
	}
	return (
		<div className="flex flex-col items-center p-2 text-center border-2">
			<div className="text-md border-b-2 cursor-pointer">{deck.name}</div>
			<LineChartComponent deck={deck} />
			<div className="text-md font-bold mt-1">{`Overall: ${toPercent(
				deck.win_rate
			)}`}</div>
		</div>
	)
}

export default DeckTile
