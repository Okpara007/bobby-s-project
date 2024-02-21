// formHandler.js

function submitForm() {
    var dishName = document.getElementById('dishName').value;
    var votes = parseInt(document.getElementById('votes').value);

    if (dishName && !isNaN(votes)) {
        // Send data to the chart page
        localStorage.setItem('newChartData', JSON.stringify({ dishName, votes }));

        // Redirect to the chart page
        window.location.href = 'charts.html';
    } else {
        alert('Invalid input. Please enter a valid dish name and number of votes.');
    }
}
