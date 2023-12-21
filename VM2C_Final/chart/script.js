var ctx2 = document.getElementById('myChart2').getContext('2d');
var myChart2 = new Chart(ctx2, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V31", "V32", "V33", "V34", "V35", "V36", "V37", "V38", "V39", "V40", "V41", "V42", "V43", "V44", "V45", "V46", "V47", "V48", "V49", "V50", "V51", "V52", "V53", "V54", "V55"],
    datasets: [{
      label: 'Tổng số ca làm việc của công nhân',
      data: [17,22,24,22,20,18,16,17,24,24,20,16,16,20,24,17,20,24,20,18,24,24,20,22,16,19,17,24,17,18,24,17,16,24,16,17,22,20,24,24,20,18,20,21,17,22,20,24,20,20,20,24,18,24,24],
      lineTension: 0,
      backgroundColor: "rgba(9, 162, 255,0.6)"
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                min: 10,
                max: 30
            }
        }]
    }
}
});

var ctx = document.getElementById('myChart1').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V31", "V32", "V33", "V34", "V35", "V36", "V37", "V38", "V39", "V40", "V41", "V42", "V43", "V44", "V45", "V46", "V47", "V48", "V49", "V50", "V51", "V52", "V53", "V54", "V55"],
    datasets: [{
      label: 'Tổng số ca đêm làm việc của công nhân',
      data: [10, 5, 2, 3, 13, 5, 11, 10, 1, 0, 8, 6, 16, 16, 1, 8, 7, 1, 10, 7, 1, 1, 4, 4, 11, 12, 12, 1, 10, 9, 1, 9, 11, 6, 10, 2, 10, 3, 2, 4, 10, 7, 3, 13, 11, 7, 6, 2, 12, 5, 7, 1, 9, 0, 1],
      lineTension: 0,
      backgroundColor: "rgba(237, 59, 59,0.6)"
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                max: 20,
            }
        }]
    }
}
});
