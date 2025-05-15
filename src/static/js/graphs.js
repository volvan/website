// Set default font size globally for all charts
Chart.defaults.font.size = 22;

// Default configuration values
const default_legend_size = 28;
const default_chart_title_size = 32;
const default_chart_title_color = "#000000"; // fallback if CSS variable is not used

/**
 * Get a color value from a CSS custom property (defined in :root)
 * @param {string} name - The CSS variable name (e.g., '--primary')
 * @returns {string} Trimmed color value
 */
function get_color(name) {
    return getComputedStyle(document.documentElement)
        .getPropertyValue(name)
        .trim();
}

// Colors pulled from CSS
const line1_color = get_color('--line1');
const line2_color = get_color('--line2');

/**
 * Generate a single-line chart
 * @param {Array} labels - X-axis labels
 * @param {Array} values - Y-axis data values
 * @param {string} id - Canvas element ID
 * @param {string} title - Dataset label
 * @param {string} chartTitle - Main chart title
 */
function generate_one_data_graph(labels, values, id, title = "No title given", chartTitle = "Missing Title") {
    const ctx = document.getElementById(id).getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: values,
                fill: false,
                borderColor: line1_color,
                lineTension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: chartTitle,
                    color: default_chart_title_color,
                    font: { size: default_chart_title_size }
                },
                legend: {
                    labels: {
                        color: get_color('--primary')
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: get_color('--primary') }
                },
                y: {
                    ticks: { color: get_color('--primary') }
                }
            }
        }
    });
}

/**
 * Generate a two-line chart
 * @param {Array} labels - X-axis labels
 * @param {Array} values1 - First dataset
 * @param {Array} values2 - Second dataset
 * @param {string} id - Canvas element ID
 * @param {string} label1 - Label for first dataset
 * @param {string} label2 - Label for second dataset
 * @param {string} chartTitle - Main chart title
 */
function generate_two_data_graph(labels, values1, values2, id, label1 = "Label1", label2 = "Label2", chartTitle = "Missing Title") {
    const ctx = document.getElementById(id).getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: label1,
                    data: values1,
                    fill: false,
                    borderColor: "rgb(75, 192, 192)",
                    lineTension: 0.1
                },
                {
                    label: label2,
                    data: values2,
                    fill: false,
                    borderColor: "rgb(75, 192, 12)",
                    lineTension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: chartTitle,
                    color: default_chart_title_color,
                    font: { size: default_chart_title_size }
                },
                legend: {
                    labels: {
                        font: { size: default_legend_size },
                        color: get_color('--secondary')
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: get_color('--secondary') }
                },
                y: {
                    ticks: { color: get_color('--secondary') }
                }
            }
        }
    });
}

/**
 * Generate a two-part doughnut chart
 * @param {number} value1 - First value
 * @param {number} value2 - Second value
 * @param {string} id - Canvas element ID
 * @param {string} label1 - Label for value1
 * @param {string} label2 - Label for value2
 * @param {string} chartTitle - Main chart title
 */
function generate_two_data_doughnut(value1, value2, id, label1 = "Label1", label2 = "Label2", chartTitle = "Missing Title") {
    const doughnutData = {
        labels: [label1, label2],
        datasets: [{
            label: 'Host Status',
            data: [value1, value2],
            backgroundColor: [
                line1_color,
                'rgb(140, 71, 147)'
            ],
            hoverOffset: 4
        }]
    };

    const doughnutConfig = {
        type: 'doughnut',
        data: doughnutData,
        options: {
            responsive: false, // set true if you want it to resize
            plugins: {
                title: {
                    display: true,
                    text: chartTitle,
                    color: default_chart_title_color,
                    font: { size: default_chart_title_size }
                },
                legend: {
                    labels: {
                        font: { size: default_legend_size },
                        color: get_color('--secondary')
                    }
                }
            }
        }
    };

    new Chart(document.getElementById(id), doughnutConfig);
}
