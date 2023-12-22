var ctx2 = document.getElementById('myChart2').getContext('2d');
var myChart2 = new Chart(ctx2, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V31", "V32", "V33", "V34", "V35", "V36", "V37", "V38", "V39", "V40", "V41", "V42", "V43", "V44", "V45", "V46", "V47", "V48", "V49", "V50", "V51", "V52", "V53", "V54", "V55"],
    datasets: [{
      label: 'Tổng số ca làm việc của công nhân',
      data: [19,21,22,21,20,19,18,18,22,22,21,18,19,21,22,19,20,22,21,19,22,22,21,20,18,21,19,22,19,19,22,18,19,22,17,18,21,20,22,22,20,18,20,20,19,21,20,22,22,20,21,22,19,22,22],
      lineTension: 0,
      backgroundColor: "rgba(9, 162, 255, 0.6)"
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

var ctx1 = document.getElementById('myChart1').getContext('2d');
var myChart1 = new Chart(ctx1, {
  type: 'line',
  data: {
    labels: ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V31", "V32", "V33", "V34", "V35", "V36", "V37", "V38", "V39", "V40", "V41", "V42", "V43", "V44", "V45", "V46", "V47", "V48", "V49", "V50", "V51", "V52", "V53", "V54", "V55"],
    datasets: [{
      label: 'Tổng số ca đêm làm việc của công nhân',
      data: [8,5,4,6,8,8,6,6,8,4,8,5,8,8,7,7,8,7,8,8,6,5,9,6,5,8,7,6,8,8,3,6,7,7,7,7,7,8,6,1,6,8,6,6,7,6,7,2,10,7,9,2,9,7,1],
      lineTension: 0,
      backgroundColor: "rgba(237, 59, 59, 0.6)"
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                min: 0,
                max: 14
            }
        }]
    }
}
});
