import { useEffect, useState } from 'react'
import useJokerStore from '../../stores/jokerStore'
import JokerTile from './JokerTile'

const Jokers: React.FC = () => {
	const { jokers, getJokers } = useJokerStore((state) => state)

	useEffect(() => {
		getJokers()
	}, [getJokers])

	return (
		<>
			<div className="grid grid-cols-4 md:grid-cols-6 lg: grid-cols-8 gap-2 p-4">
				{jokers &&
					Object.values(jokers).map((joker) => (
						<JokerTile key={joker.id} jokerId={joker.id} />
					))}
			</div>
		</>
	)
}

export default Jokers
