import React from "react";
import "./Square.css";



const Square = (props) => { 
    return (
        <button className="square" onClick={props.onClick} id={props.id}>
            {props.slotState}
        </button>
    );
};


export default Square;
