import { create } from 'zustand'
import { devtools } from 'zustand/middleware'

export type Joker = {
	id: string
	name: string
	rarity: number
	desc: string
	win_rate: number
	win_rate_updated_at: string
}

interface JokerStore {
	focus: Joker | null
	jokers: {
		[key: string]: Joker
	}
	getFocus: (id: string) => Promise<void>
	getJokers: () => Promise<void>
}

const useJokerStore = create(
	devtools<JokerStore>((set, get) => ({
		focus: null,
		jokers: {},
		getFocus: async (id: string) => {
			try {
				const url = `/api/jokers/${id}`
				const res = await fetch(url)
				if (!res.ok) {
					throw new Error(`Failed to fetch joker (id: ${id})`)
				}
				const joker = await res.json()
				set({ focus: joker })
			} catch (e) {
				console.error(e)
			}
		},
		getJokers: async () => {
			try {
				const url = `/api/jokers`
				const res = await fetch(url)
				if (!res.ok) {
					throw new Error(`Failed to get all jokers`)
				}
				const data = await res.json()
				set({ jokers: { ...data } })
				return data
			} catch (e) {
				console.error(e)
			}
		},
	}))
)

export default useJokerStore
