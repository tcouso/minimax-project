import React, { Fragment, useState } from "react";
import "./Board.css";

// components
import Square from './Square';




const Board = () => {
    
    const [slots, setSlots] = useState(["","","","","","","","",""]);
    
    const handleClick = (event) => {
        const indexToChange = event.target.id
        let newSlots = [...slots];
        newSlots[indexToChange] = "X";
        setSlots(newSlots);
    }
    return (
        <Fragment>
            <h1>Input Board</h1>
            <div className="board">
                    <Square
                        id={0}
                        slotState={slots[0]}
                        onClick={handleClick}
                    />
                    <Square
                        id={1}
                        slotState={slots[1]}
                        onClick={handleClick}
                    />
                    <Square
                        id={2}
                        slotState={slots[2]}
                        onClick={handleClick}
                    />
                    <Square
                        id={3}
                        slotState={slots[3]}
                        onClick={handleClick}
                    />
                    <Square
                        id={4}
                        slotState={slots[4]}
                        onClick={handleClick}
                    />
                    <Square
                        id={5}
                        slotState={slots[5]}
                        onClick={handleClick}
                    />
                    <Square
                        id={6}
                        slotState={slots[6]}
                        onClick={handleClick}
                    />
                    <Square
                        id={7}
                        slotState={slots[7]}
                        onClick={handleClick}
                    />
                    <Square
                        id={8}
                        slotState={slots[8]}
                        onClick={handleClick}
                    />
                
            </div>
        </Fragment>
    );
};

export default Board;