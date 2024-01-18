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
