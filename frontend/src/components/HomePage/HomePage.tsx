import { useEffect, useState } from 'react'
import Decks from '../Decks/Decks'

type Graphs = 'decks' | 'stakes' | null

const HomePage: React.FC = () => {
	const [activeGraph, setActiveGraph] = useState<Graphs>(null)

	const graphOptions = [
		{ label: 'Decks', value: 'decks' },
		{ label: 'Stakes', value: 'stakes' },
	]

	const handleGraphSelect = (option: { label: string; value: string }) => {
		switch (option.value) {
			case 'decks':
				setActiveGraph('decks')
		}
	}

	return (
		<div className="flex flex-col w-full">
			<div className="flex justify-center">
				{graphOptions.map((option) => (
					<div
						className="border-2 p-2 m-2 cursor-pointer hover:rounded-lg hover:bg-gray-200"
						onClick={() => handleGraphSelect(option)}
					>
						{option.label}
					</div>
				))}
			</div>
			{activeGraph === 'decks' && <Decks />}
		</div>
	)
}

export default HomePage
