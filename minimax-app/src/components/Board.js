import React, { Fragment, useState } from "react";
import "./Styles.css";

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