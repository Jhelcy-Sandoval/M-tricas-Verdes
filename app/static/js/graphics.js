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
