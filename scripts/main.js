let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/tictactoe.svg.png') {
        myImage.setAttribute('src', 'images/cat.jpeg');
    } else {
        myImage.setAttribute('src', 'images/tictactoe.svg.png')
    }
}