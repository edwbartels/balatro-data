import { create } from 'zustand'
import { devtools } from 'zustand/middleware'

export type Deck = {
	id: string
	name: string
	desc: string
	win_rate: number
	win_rate_updated_at: string
	avg_max_ante: number
	stakes: {
		[key: string]: {
			win_rate: number
			win_rate_updated_at: string
			avg_max_ante: number
		}
	}
}

interface DeckStore {
	focus: Deck | null
	decks: {
		[key: string]: Deck
	}
	getFocus: (id: string) => Promise<void>
	getDecks: () => Promise<void>
}

const useDeckStore = create(
	devtools<DeckStore>((set, get) => ({
		focus: null,
		decks: {},
		getFocus: async (id: string) => {
			try {
				const url = `/api/decks/${id}`
				const res = await fetch(url)
				if (!res.ok) {
					throw new Error(`Failed to fetch deck (id: ${id})`)
				}
				const deck = await res.json()
				set({ focus: deck })
			} catch (e) {
				console.error(e)
			}
		},
		getDecks: async () => {
			try {
				const url = `/api/decks`
				const res = await fetch(url)
				if (!res.ok) {
					throw new Error(`Failed to get all decks`)
				}
				const data = await res.json()
				set({ decks: { ...data } })
				return data
			} catch (e) {
				console.error(e)
			}
		},
	}))
)

export default useDeckStore
