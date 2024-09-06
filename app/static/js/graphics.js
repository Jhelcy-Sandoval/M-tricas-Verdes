// Grafico Planta
document.addEventListener('DOMContentLoaded', function() {
  const chartDataElement = document.getElementById('chart-data');

  const labelsRaw = chartDataElement.dataset.labels || '[]';  
  const valuesRaw = chartDataElement.dataset.values || '[]';  

try {
      const labels = JSON.parse(labelsRaw);
      const values = JSON.parse(valuesRaw);

      if (!labels.length || !values.length) {
          console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
          return; 
      }

      const ctx = document.getElementById('myChart').getContext('2d');

      const myChart = new Chart(ctx, {
          data: {
            datasets: [{
                type: 'bar',
                label: 'Bar Dataset',
                data: [10, 20, 30, 40]
            }, {
                type: 'line',
                label: 'Line Dataset',
                data: [50, 50, 50, 50],
            }],
            labels: ['January', 'February', 'March', 'April']
        },
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      });
  } catch (e) {
      console.error('Error al parsear los datos JSON:', e);
  }
});

// Grafico general
document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-dos');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartdos').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

  //Grafica temperatura
  document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-tres');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myCharttres').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                      ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

// Grafico humedad
  document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-cuarto');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartCuarto').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

// Grafico desarrollo 
  document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-quinto');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartQuinto').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

  // Grafico humedad
  document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-cuarto');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartCuarto').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

// estadistica clave 
  document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-seis');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartseis').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });
