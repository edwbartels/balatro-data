import { useEffect, useState } from 'react'
import useDeckStore, { Deck } from '../../stores/deckStore'
import DeckTile from './DeckTile'
import LineChartComponent from './DeckLineChart'
import { toPercent } from '../../utils/formatting'
import { DECK_NAMES } from '../../utils/constants'

const Decks: React.FC = () => {
	const { decks, getDecks } = useDeckStore((state) => state)
	const [activeDeck, setActiveDeck] = useState<Deck>()
	// decks[DECK_NAMES[Math.floor(Math.random() * DECK_NAMES.length)]]
	console.log(DECK_NAMES[Math.floor(Math.random() * DECK_NAMES.length)])
	useEffect(() => {
		getDecks()
	}, [getDecks])
	useEffect(() => {
		setActiveDeck(
			decks[DECK_NAMES[Math.floor(Math.random() * DECK_NAMES.length)]]
		)
	}, [decks])

	if (!decks) {
		return <>Error: Decks Not Found</>
	}

	if (!activeDeck) {
		return <>Error: Deck Not Found</>
	}

	return (
		// <div className="flex flex-col w-full">
		// 	{decks &&
		// 		Object.values(decks).map((deck) => (
		// 			<DeckTile key={deck.id} deckId={deck.id} />
		// 		))}
		// </div>
		<div className="flex flex-col w-full">
			<div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 p-4">
				{decks &&
					Object.values(decks).map((d) => (
						<div
							className={`border-2 text-md cursor-pointer ${
								activeDeck != d && 'hover:bg-gray-200 hover:rounded-lg'
							} ${activeDeck == d && 'bg-gray-400 rounded-lg'}`}
							key={d.id}
							onClick={() => setActiveDeck(decks[d.id])}
						>
							{d.name.split(' ')[0]}
						</div>
					))}
			</div>

			<div className="text-md">{`${activeDeck.name} - Overall: ${toPercent(
				activeDeck?.win_rate
			)}`}</div>
			{activeDeck && <LineChartComponent deck={activeDeck} />}
		</div>
	)
}

export default Decks
