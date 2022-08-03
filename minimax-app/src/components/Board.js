import React, { useState, useEffect } from "react";
import "./Styles.css";

// components
import Square from './Square';

// urls
// const BASE = "http://127.0.0.1:5000/move";
const BASE = "https://minimaxapi.herokuapp.com/move";



const Board = () => {

	const [slots, setSlots] = useState(["", "", "", "", "", "", "", "", ""]);
	useEffect(() => {
		checkEndOfGame();
	}, [slots])

	const checkGameState = (board) => {
		if (
			(board[0] === board[1]) && (board[1] === board[2]) && (board[0] !== "")
			) {
				return board[0]
			} else if (
				(board[3] === board[4]) && (board[4] === board[5]) && (board[3] !== "")
			) {
				return board[3]
			} else if(
				(board[6] === board[7]) && (board[7] === board[8]) && (board[6] !== "")
			) {
				return board[6]
			} else if (
				(board[0] === board[3]) && (board[3] === board[6]) && (board[0] !== "")
			) {
				return board[0]
			} else if (
				(board[1] === board[4]) && (board[4] === board[7]) && (board[1] !== "")
			) {
				return board[1]
			} else if (
				(board[2] === board[5]) && (board[5] === board[8]) && (board[2] !== "")
			) {
				return board[2]
			} else if (
				(board[0] === board[4]) && (board[4] === board[8]) && (board[0] !== "")
			) {
				return board[0]
			} else if (
				(board[2] === board[4]) && (board[4] === board[6]) && (board[2] !== "")
			) {
				return board[2]
			} else if (
				board.includes("") === true
			) {
				return ""
			} else {
				return "tie"
			}
			
	}

	const checkEndOfGame = () =>{
		console.log(slots);
		const gameState = checkGameState(slots);
		console.log(gameState);
		if (gameState === "tie") {
			alert("There's been a tie!");
			setSlots(["", "", "", "", "", "", "", "", ""]);
		} else if ((gameState === "x") || (gameState === "o")) {
			alert(`${gameState} has won!`);
			setSlots(["", "", "", "", "", "", "", "", ""]);
		} else {
			// game continues
		}
	}


	const handleClick = async (event) => {
		try {
			const indexToChange = event.target.id;
			let newSlots = [...slots];
			if (slots[indexToChange] === ""){
				// make a move and send it to server
				newSlots[indexToChange] = "x";
				const body = {"board": newSlots};
				const response = await fetch(BASE, {
						method: "POST",
						headers: { "Content-Type": "application/json" },
						body: JSON.stringify(body)
					});
				const new_board = await response.json()
				setSlots(new_board["new-board"]);
						
			} else {
				alert("Invalid move!")
			}
		} catch (err) {
			console.error(err.message);
		}
	};
		
	return (
			<div className="board">
				{slots.map((item, index) => {
					return (
							<Square
								id={index}
								slotState={item}
								onClick={handleClick}
							/>
					)
				})}
			</div>
	);
};

export default Board;