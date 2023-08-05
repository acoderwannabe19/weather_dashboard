

var prec_list = JSON.parse('{{ prec_list | safe }}');
    var lastFourElements = prec_list.slice(-4);

    var times = JSON.parse('{{ times | safe }}');

    var ctx = document.getElementById('precChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: times,
            datasets: [{
                label: 'Wind speed',
                data: lastFourElements ,
                backgroundColor: 'rgba(54, 50, 235, 0.5)',
                borderColor: 'rgba(54, 162, 25, 1)',
                borderWidth: 1
            }]
        },
        options: {
                responsive: true,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Timestamps'
                        },
                        grid: {
      display: false
    }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Temperature'
                        },
                        border: {
                          dash: [2,4],
                      },
                      },
                      
                    }}
                  
    });