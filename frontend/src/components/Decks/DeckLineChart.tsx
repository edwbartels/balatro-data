'use-client'
import {
	LineChart,
	Line,
	ResponsiveContainer,
	XAxis,
	YAxis,
	Tooltip,
} from 'recharts'
import { Deck } from '../../stores/deckStore'
import { STAKE_NAMES, StakeLevel } from '../../utils/constants'

interface LineChartComponentProps {
	deck: Deck
}
const LineChartComponent: React.FC<LineChartComponentProps> = ({ deck }) => {
	const chartData = Object.entries(deck.stakes).map(([stake, stats]) => ({
		stake: Number(stake),
		winRate: stats.win_rate,
		stakeName: STAKE_NAMES[Number(stake) as StakeLevel],
	}))

	const stakeColors = {
		1: '#64748b', // gray
		2: '#ef4444', // red
		3: '#22c55e', // green
		4: '#ec4899', // pink
		5: '#3b82f6', // blue
		6: '#a855f7', // purple
		7: '#f97316', // orange
		8: '#eab308', // yellow
	}
	return (
		<ResponsiveContainer width="100%" height={400}>
			<LineChart data={chartData}>
				<defs>
					<linearGradient id="colorGradient" x1="0" y1="0" x2="1" y2="0">
						<stop offset="0%" stopColor="#D3D3D3" />
						<stop offset="14%" stopColor="#ef4444" />
						<stop offset="28%" stopColor="#22c55e" />
						<stop offset="42%" stopColor="#808080" />
						<stop offset="56%" stopColor="#3b82f6" />
						<stop offset="70%" stopColor="#a855f7" />
						<stop offset="84%" stopColor="#f97316" />
						<stop offset="100%" stopColor="#eab308" />
					</linearGradient>
				</defs>
				<XAxis
					dataKey="stake"
					tickFormatter={(value) => STAKE_NAMES[value as StakeLevel]}
				/>
				<YAxis
					domain={[0, 1]}
					ticks={[0, 0.25, 0.5, 0.75, 1]}
					tickFormatter={(value) => `${value * 100}%`}
				/>
				<Tooltip
					formatter={(value) => [
						`${(Number(value) * 100).toFixed(0)}%`,
						'Win Rate',
					]}
					labelFormatter={(stake) => [
						`${STAKE_NAMES[stake as StakeLevel]} Stake`,
					]}
				/>
				{/* {Object.keys(stakeColors).map((stake, index) => {
					if (index === 0) return null

					return (
						<Line
							key={stake}
							type="monotone"
							dataKey="winRate"
							stroke={stakeColors[stake]}
							strokeWidth={2}
							data={chartData.slice(index - 1, index + 1)}
						/>
					)
				})} */}
				<Line
					type="monotone"
					dataKey="winRate"
					stroke="url(#colorGradient)"
					strokeWidth={2}
				/>
			</LineChart>
		</ResponsiveContainer>
	)
}

export default LineChartComponent
