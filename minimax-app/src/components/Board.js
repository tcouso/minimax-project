import React, { Fragment, useState } from "react";
import "./Styles.css";

// components
import Square from './Square';

// urls
const BASE = "http://127.0.0.1:5000/move";

const Board = () => {

	const [slots, setSlots] = useState(["", "", "", "", "", "", "", "", ""]);

	const handleClick = async (event) => {
		try {
			const indexToChange = event.target.id;
			let newSlots = [...slots];
			newSlots[indexToChange] = "x";
			const body = {"board": newSlots};
			const response = await fetch(BASE, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(body)
			});
			const new_board = await response.json()
			setSlots(new_board["new-board"]);
		} catch (err) {
			console.error(err.message);
		}
	};
		
	return (
		<Fragment>
			<div className="board">
				{slots.map((item, index) => {
					return (
						<Fragment>
							<Square
								id={index}
								slotState={item}
								onClick={handleClick}
							/>
						</Fragment>
					)
				})}
			</div>
		</Fragment>
	);
};

export default Board;