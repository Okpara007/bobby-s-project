// Global variable for the bar chart instance
var barChart;

document.addEventListener('DOMContentLoaded', function () {
    createOrUpdateChart('barchart', 'bar', getInitialChartData());
});

function getInitialChartData() {
    // Retrieve and parse stored chart data or return default data
    var storedChartData = localStorage.getItem('newChartData');
    if (storedChartData) {
        localStorage.removeItem('newChartData'); // Clear stored data after loading
        return JSON.parse(storedChartData);
    }
    return {
        // Provide default data structure if localStorage is empty
        labels: [],
        datasets: [{
            label: '# of Votes',
            data: [],
            backgroundColor: 'rgba(41, 155, 99, 1)',
            borderColor: 'rgba(41, 155, 99, 1)',
            borderWidth: 1,
        }],
    };
}

function createOrUpdateChart(canvasId, chartType, chartData) {
    var ctx = document.getElementById(canvasId).getContext('2d');
    if (barChart) {
        barChart.destroy();
    }
    barChart = new Chart(ctx, {
        type: chartType,
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}

// Define the global functions that will be called by HTML elements
window.changeChartType = function () {
    var newChartType = document.getElementById('chartType').value;
    if (barChart && newChartType !== barChart.config.type) {
        createOrUpdateChart('barchart', newChartType, barChart.data);
    }
};

window.addNewData = function () {
    var dishName = prompt('Enter new dish name:');
    var votes = parseInt(prompt('Enter number of votes:'));
    if (dishName && !isNaN(votes)) {
        chartData.push({ dishName, votes });
        addData(dishName, votes);
    } else {
        alert('Invalid input. Please enter a valid dish name and number of votes.');
    }
};

window.removeLastData = function () {
    if (chartData.length > 0) {
        chartData.pop();
        removeData();
    } else {
        alert('No data to remove.');
    }
};
