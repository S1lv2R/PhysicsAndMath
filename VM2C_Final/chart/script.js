var ctx2 = document.getElementById('myChart2').getContext('2d');
var myChart2 = new Chart(ctx2, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17"],
    datasets: [{
      label: 'Tổng số ngày làm việc của công nhân',
      data: [22, 22, 16, 17, 19, 22, 16, 17, 22, 19, 19, 18, 19, 22, 19, 22, 19],
      backgroundColor: "rgba(9, 162, 255,0.6)"
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                min: 6,
                max: 25
            }
        }]
    }
}
});

var ctx = document.getElementById('myChart1').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17"],
    datasets: [{
      label: 'Tổng số ca đêm làm việc của công nhân',
      data: [5, 5, 6, 3,  8,  6 , 8 , 4, 10,  9,  4,  9,  3, 10,  5,  6,  4],
      backgroundColor: "rgba(237, 59, 59,0.6)"
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                max: 15
            }
        }]
    }
}
});