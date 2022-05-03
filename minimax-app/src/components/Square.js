import React from "react";
import "./Styles.css";



const Square = (props) => { 
    return (
        <button className="square" onClick={props.onClick} id={props.id}>
            {props.slotState}
        </button>
    );
};


export default Square;
