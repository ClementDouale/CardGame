document.addEventListener("DOMContentLoaded", function() {
    let timeLeft = 90;
    const timerElement = document.getElementById('timer');

    const timer = setInterval(function() {
        timeLeft--;
        timerElement.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(timer);
            // Todo : Handle the end of the timer (e.g., submit the form automatically or show a message)
            alert("Time's up!");
        }
    }, 1000);
});

function addCardValueToInput(cardValue, cardName) {
    var inputField = document.getElementById('player-input');
    var selectedCardsField = document.getElementById('selected-cards');
    inputField.value += cardValue + ' '; // Adds the card value and a space
     // Append the card name to the hidden input
     if (selectedCardsField.value) {
        selectedCardsField.value += ','; // Add a comma if it's not the first card
    }
    selectedCardsField.value += cardName;
}

function addOperatorToInput(operator) {
    var inputField = document.getElementById('player-input');
    inputField.value += ' ' + operator + ' '; // Adds space before and after operator
}

document.addEventListener('DOMContentLoaded', function() {
    // Get the modal
    var modal = document.getElementById('rules-modal');

    // Get the button that opens the modal
    var btn = document.getElementById('rules-btn');

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName('close')[0];

    // When the user clicks the button, open the modal 
    btn.onclick = function() {
        modal.style.display = 'block';
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
