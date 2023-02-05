var ctx = document.getElementById('mycanvas1').getContext('2d');
var ctx1 = document.getElementById('mycanvas2').getContext('2d');

var chart1 = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Akshat', 'Sanskar', 'Yash', 'Ranjit'],
    datasets: [{
      label: 'Time ms',
      data: [0.0008613, 0.0010616, 0.0006803, 0.0012585],
      backgroundColor: 'rgba(167, 224, 218, 1)',
      borderColor: 'rgba(167, 224, 218, 1)',
      barThickness: 50,
      borderWidth: 2,
      borderRadius: 20, // This will round the corners
      borderSkipped: false,
    }]
  },
  options: {
    scales: {
      xAxes: [{
        ticks: {
          fontColor: 'white' // Set the font color of the X-axis labels to white
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: 'white'
        },
        scaleLabel: {
          fontColor: 'white' // Set the font color of the scale label to white
        }
      }]
    }
  }
});


var chart2 = new Chart(ctx1, {
  type: 'bar',
  data: {
    labels: ['Akshat', 'Sanskar', 'Yash', 'Ranjit'],
    datasets: [{
      label: 'Space',
      data: [0.15578, 0.16480, 0.16480, 0.16480],
      backgroundColor: 'rgba(167, 224, 218, 1)',
      borderColor: 'rgba(167, 224, 218, 1)',
      barThickness: 50,
      borderWidth: 2,
      borderRadius: 20, // This will round the corners
      borderSkipped: false,
    }]
  },
  options: {
    scales: {
      xAxes: [{
        ticks: {
          fontColor: 'white' // Set the font color of the X-axis labels to white
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontColor: 'white'
        },
        scaleLabel: {
          fontColor: 'white' // Set the font color of the scale label to white
        }
      }]
    }
  }
});
