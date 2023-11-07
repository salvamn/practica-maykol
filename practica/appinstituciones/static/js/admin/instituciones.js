fetch('http://127.0.0.1:8000/obtener_data_equipos_medicos_lebu/')
.then(response => response.json())
.then(data => {
    console.log(data);

    const domAnual = document.getElementById('grafico-anual')
    var myChart = echarts.init(domAnual, null)

    var option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            bottom: '2%',
            left: 'center'
        },
        series: [
            {
                name: 'Estado General Total',
                type: 'pie',
                radius: ['20%', '50%'],
                avoidLabelOverlap: false,
                bottom: '15%',
                label: {
                    show: true,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: false,
                        fontSize: 10,
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: data.bueno, name: 'Bueno' },
                    { value: data.regular, name: 'Regular' },
                    { value: data.malo, name: 'Malo' },
                    { value: data.baja, name: 'Baja' }
                ]
            }
        ]
    };

    myChart.setOption(option);

    // Agrega la siguiente línea después de setOption para hacer que el gráfico se ajuste al contenedor
    window.addEventListener('resize', function () {
    myChart.resize();
    });
})