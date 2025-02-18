import { useState } from 'react'
import {
	createBrowserRouter,
	RouterProvider,
	Outlet,
	Router,
} from 'react-router-dom'
import './App.css'
import Jokers from './components/Jokers/Jokers'
import Decks from './components/Decks/Decks'
import HomePage from './components/HomePage/HomePage'

const Layout = () => {
	return (
		<div className="flex w-full">
			<Outlet />
		</div>
	)
}
const router = createBrowserRouter([
	{
		element: <Layout />,
		children: [{ path: '/', element: <HomePage /> }],
	},
])
const App = () => {
	return <RouterProvider router={router} />
}

export default App
