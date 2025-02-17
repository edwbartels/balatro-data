import React, { useState, useEffect } from 'react'
import useJokerStore, { Joker } from '../../stores/jokerStore'
import { toPercent } from '../../utils/formatting'

interface JokerTileProps {
	jokerId: string
}

const JokerTile: React.FC<JokerTileProps> = ({ jokerId }) => {
	const joker: Joker = useJokerStore((state) => state.jokers[jokerId])

	if (!joker) {
		return <>Error: Joker Not Found</>
	}
	return (
		<div className="flex flex-col items-center p-2 text-center border-2">
			<div className="text-sm border-b-2 cursor-pointer">{joker.name}</div>
			<div className="text-sm font-bold">{toPercent(joker.win_rate)}</div>
		</div>
	)
}

export default JokerTile
