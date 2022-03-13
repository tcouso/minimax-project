let allSlots = document.querySelectorAll(".slot")
let initialBoadState = ['', '', '', '', '', '', '', '']

function placeToken(event) {
    event.target.textContent = "X"
}

for (slot of allSlots) {
    slot.addEventListener("click", placeToken)
}

// make ajax request when slot is clicked: 
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data


// XHR request

let request = new XMLHttpRequest();