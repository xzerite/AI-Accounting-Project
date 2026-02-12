// script.js

// Function to fetch data from an API
async function fetchData(apiUrl) {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Function to render charts using Chart.js
function renderChart(ctx, chartData) {
    const chart = new Chart(ctx, {
        type: 'line', // Change this based on your visualization preference
        data: chartData,
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to handle filter selections
function handleFilters(data) {
    const filters = document.querySelectorAll('.filter');
    filters.forEach(filter => {
        filter.addEventListener('change', () => {
            const selectedFilters = Array.from(filters)
                .filter(f => f.checked)
                .map(f => f.value);
            const filteredData = data.filter(item => selectedFilters.includes(item.category));
            updateChart(filteredData);
        });
    });
}

// Function to update the chart with filtered data
function updateChart(filteredData) {
    const ctx = document.getElementById('myChart').getContext('2d');
    const chartData = { labels: [], datasets: [] };
    // Populate chartData based on filteredData
    renderChart(ctx, chartData);
}

// Main function to initialize the dashboard
async function initDashboard() {
    const apiUrl = 'https://api.example.com/data'; // Replace with your actual data source
    const data = await fetchData(apiUrl);
    const ctx = document.getElementById('myChart').getContext('2d');

    renderChart(ctx, data);
    handleFilters(data);
}

window.onload = initDashboard;