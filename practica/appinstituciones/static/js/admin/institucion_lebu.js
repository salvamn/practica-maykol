// fetch('http://127.0.0.1:8000/obtener_data_equipos_medicos_lebu/')
// .then(response => response.json())
// .then(data => {
//     const domAnual = document.getElementById('grafico-anual')
//     var myChart = echarts.init(domAnual, null)
//     var option = {
//         tooltip: {
//             trigger: 'item'
//         },
//         legend: {
//             bottom: '2%',
//             left: 'center'
//         },
//         series: [
//             {
//                 name: 'Estado General Total',
//                 type: 'pie',
//                 radius: ['20%', '70%'],
//                 avoidLabelOverlap: false,
//                 bottom: '15%',
//                 label: {
//                     show: true,
//                     position: 'center'
//                 },
//                 emphasis: {
//                     label: {
//                         show: false,
//                         fontSize: 10,
//                         fontWeight: 'bold'
//                     }
//                 },
//                 labelLine: {
//                     show: false
//                 },
//                 data: [
//                     { value: data.bueno, name: 'Bueno' },
//                     { value: data.regular, name: 'Regular' },
//                     { value: data.malo, name: 'Malo' },
//                     { value: data.baja, name: 'Baja' }
//                 ]
//             }
//         ]
//     };


//     myChart.setOption(option);

//     // Agrega la siguiente línea después de setOption para hacer que el gráfico se ajuste al contenedor
//     window.addEventListener('resize', function () {
//     myChart.resize();
//     });
// })

fetch('http://127.0.0.1:8000/obtener_criticidad_medicos_lebu/')
    .then(response => response.json())
    .then(data => {
        const domContenedorMultiplesgraficos = document.getElementById('grafico-barra-criticidad-anual')
        const domContenedorRelevanteBarra = document.getElementById('grafico-barra-relevante-anual')
        var myChart = echarts.init(domContenedorMultiplesgraficos, null)
        var myChart2 = echarts.init(domContenedorRelevanteBarra, null)
        // console.log((data));
        option = {
            grid: {
                left: '2%',
                right: '2%',
                bottom: '3%',
                containLabel: true,
            },
            xAxis: {
                type: 'value'
            },
            yAxis: {
                type: 'category',
                data: ['Criticos']
            },
            series: [
                {
                    name: 'Critico',
                    type: 'bar',
                    stack: 'total',
                    label: {
                        show: true
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: []
                },

            ],
            media: [
                {
                    query: {
                    },
                    option: {
                        grid: {
                            left: '5%',
                            right: '5%',
                            bottom: '1%',
                            width: '100%',
                            height: '100%',
                            containLabel: true
                        }
                    }
                }
            ],
            // resize: true
        };

        myChart.setOption(option);

        option2 = {
            grid: {
                left: '2%',
                right: '2%',
                bottom: '3%',
                containLabel: true,
            },
            xAxis: {
                type: 'value'
            },
            yAxis: {
                type: 'category',
                data: ['Relevantes']
            },
            series: [
                {
                    name: 'Critico',
                    type: 'bar',
                    stack: 'total',
                    label: {
                        show: true
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: []
                },

            ],
            media: [
                {
                    query: {
                    },
                    option: {
                        grid: {
                            left: '5%',
                            right: '5%',
                            bottom: '1%',
                            width: '100%',
                            height: '100%',
                            containLabel: true
                        }
                    }
                }
            ],
            // resize: true
        };
        myChart2.setOption(option2);

    })

// fetch('http://127.0.0.1:8000/get_lebu_medico/')
// .then(response => response.json())
// .then(data => {
//     console.log(data);
// })



const { createApp } = Vue
createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            titulo_primer_grafico: 'Equipos Medicos',
            vida_util: 0,
            opcionSelecionada: 'medico',
            data_tabla: null,
            data_columnas_tabla: null,
            select_lista_instituciones: [
                { valor: 'medico', texto: 'Medico' },
                { valor: 'industrial', texto: 'Industrial' },
                { valor: 'vehiculo', texto: 'Vehiculo' },
            ],
            resultados: [],
            busqueda: null,
            placeholderDinamico: 'n° de inventario'
        }
    },

    methods: {
        actualizarGraficoMedianteSelect() {
            if (this.opcionSelecionada === 'medico') {
                this.placeholderDinamico = 'n° de inventario'
                axios.get('http://127.0.0.1:8000/get_lebu_medico/')
                    .then(response => {
                        // Data Para los graficos
                        // -----------
                        data_grafico = { 'bueno': 0, 'regular': 0, 'malo': 0, 'baja': 0 }
                        data_grafico_barra = { 'critico': 0, 'relevante': 0 }
                        vida_util_residual = 0
                        for (var elemento of response.data.datos) {
                            if (elemento.estado === 'BUENO') {
                                data_grafico.bueno += 1
                            } else if (elemento.estado === 'REGULAR') {
                                data_grafico.regular += 1
                            } else if (elemento.estado === 'MALO') {
                                data_grafico.malo += 1
                            } else if (elemento.estado === 'BAJA') {
                                data_grafico.baja += 1
                            }
                        }
                        for (var crt of response.data.datos) {
                            if (crt.criticidad == 'CRITICO') {
                                data_grafico_barra.critico += 1
                            } else if (crt.criticidad == 'RELEVANTE') {
                                data_grafico_barra.relevante += 1
                            }
                        }
                        for (var vu of response.data.datos) {
                            if (vu.vida_util < 0) {
                                vida_util_residual += 1
                            }
                        }
                        // -----------
                        // Data Para los Graficos


                        // Data Para la Tabla
                        // -----------
                        this.data_columnas_tabla = [
                            'ID', 'Clase', 'Nombre', 'Marca', 'Modelo', 'Serie', 'Anio', 'Vida Util', 'Estado', 'Criticidad', 'Garantia',
                            'Vencimiento Garantia', 'Plan Mantención', 'Tipo Equipo', 'ID Convenio', 'ID Institución', 'Eliminado', 'Año Ingreso',
                            'Costo Anual', 'Nombre Proveedor', 'Numero Inventario', 'Recinto', 'Servicio Clinico', 'Subclase', 'Tipo Mantenimiento',
                            'Vida Util Residual'
                        ]
                        // -----------
                        // Data Para la Tabla

                        this.titulo_primer_grafico = 'Equipos Medicos'
                        this.grafico(data_grafico.bueno, data_grafico.regular, data_grafico.malo, data_grafico.baja)
                        this.grafico_barra_1(data_grafico_barra.critico)
                        this.grafico_barra_2(data_grafico_barra.relevante)
                        this.vida_util = vida_util_residual
                        this.data_tabla = response.data.datos
                        console.log(response.data);
                        console.log(response.data.datos);
                    })
            } else if (this.opcionSelecionada === 'industrial') {
                this.placeholderDinamico = 'n° de inventario'
                axios.get('http://127.0.0.1:8000/get_lebu_industrial/')
                    .then(response => {
                        data_grafico = { 'bueno': 0, 'regular': 0, 'malo': 0, 'baja': 0 }
                        data_grafico_barra = { 'critico': 0, 'relevante': 0 }
                        vida_util_residual = 0
                        for (var elemento of response.data.datos) {
                            if (elemento.estado === 'BUENO') {
                                data_grafico.bueno += 1
                            } else if (elemento.estado === 'REGULAR') {
                                data_grafico.regular += 1
                            } else if (elemento.estado === 'MALO') {
                                data_grafico.malo += 1
                            } else if (elemento.estado === 'BAJA') {
                                data_grafico.baja += 1
                            }
                        }

                        for (var crt of response.data.datos) {
                            if (crt.criticidad == 'CRITICO') {
                                data_grafico_barra.critico += 1
                            } else if (crt.criticidad == 'RELEVANTE') {
                                data_grafico_barra.relevante += 1
                            }
                        }

                        for (var vur of response.data.datos) {
                            if (vur.vida_util_residual <= 0) {
                                vida_util_residual += 1
                            }
                        }

                        // Data Para la Tabla
                        // -----------
                        this.data_columnas_tabla = [
                            'ID', 'Clase', 'Nombre', 'Marca', 'Modelo', 'Serie', 'Anio', 'Vida Util', 'Estado', 'Criticidad', 'Garantia',
                            'Vencimiento Garantia', 'Plan Mantención', 'Tipo Equipo', 'ID Convenio', 'ID Institución', 'Eliminado', 'Año Ingreso',
                            'Costo Anual', 'Nombre Proveedor', 'Numero Inventario', 'Recinto', 'Servicio Clinico', 'Subclase', 'Tipo Mantenimiento',
                            'Vida Util Residual'
                        ]
                        // -----------
                        // Data Para la Tabla

                        this.titulo_primer_grafico = 'Equipos Industriales'
                        this.grafico(data_grafico.bueno, data_grafico.regular, data_grafico.malo, data_grafico.baja)
                        this.grafico_barra_1(data_grafico_barra.critico)
                        this.grafico_barra_2(data_grafico_barra.relevante)
                        this.vida_util = vida_util_residual
                        this.data_tabla = response.data.datos
                        console.log(response.data);
                    })
            } else if (this.opcionSelecionada === 'vehiculo') {
                this.placeholderDinamico = 'patente'
                axios.get('http://127.0.0.1:8000/get_lebu_vehiculos/')
                    .then(response => {
                        data_grafico = { 'bueno': 0, 'regular': 0, 'malo': 0, 'baja': 0 }
                        data_grafico_barra = { 'critico': 0, 'relevante': 0 }
                        vida_util_residual = 0
                        for (var elemento of response.data.datos) {
                            if (elemento.estado === 'BUENO') {
                                data_grafico.bueno += 1
                            } else if (elemento.estado === 'REGULAR') {
                                data_grafico.regular += 1
                            } else if (elemento.estado === 'MALO') {
                                data_grafico.malo += 1
                            } else if (elemento.estado === 'BAJA') {
                                data_grafico.baja += 1
                            }
                        }
                        for (var crt of response.data.datos) {
                            if (crt.criticidad == 'CRITICO' || crt.criticidad == 'CRÍTICO') {
                                data_grafico_barra.critico += 1
                            } else if (crt.criticidad == 'RELEVANTE') {
                                data_grafico_barra.relevante += 1
                            }
                        }
                        for (var vur of response.data.datos) {
                            if (vur.vida_util_residual <= 0) {
                                vida_util_residual += 1
                            }
                        }

                        this.data_columnas_tabla = [
                            'ID', 'Samu', 'Funcion', 'Marca', 'Modelo', 'Patente', 'Numero Motor', 'Kilometraje', 'Estado', 'Año',
                            'Vida Util', 'Criticidad', 'Garantia', 'Vencimiento Garantia', 'Plan Mantención', 'Tipo Equipo', 'ID Institución',
                            'Eliminado', 'Año Ingreso Plan Mantenimiento', 'Clase Ambulancia', 'Costo Anual Mantenimiento', 'Establecimiento',
                            'Estado Situacion', 'ID Convenio Mantenimiento', 'Nombre Proveedor', 'Region', 'Tipo Ambulancia', 'Tipo Carroceria',
                            'Tipo Mantenimiento', 'Vida Util Residual'
                        ]

                        this.titulo_primer_grafico = 'Vehiculos'
                        this.grafico(data_grafico.bueno, data_grafico.regular, data_grafico.malo, data_grafico.baja)
                        this.grafico_barra_1(data_grafico_barra.critico)
                        this.grafico_barra_2(data_grafico_barra.relevante)
                        this.vida_util = vida_util_residual
                        this.data_tabla = response.data.datos
                    })
            }
        },

        data_inicial() {
            axios('http://127.0.0.1:8000/get_lebu_medico/')
                .then(response => {
                    data_grafico = { 'bueno': 0, 'regular': 0, 'malo': 0, 'baja': 0 }
                    data_grafico_barra = { 'critico': 0, 'relevante': 0 }
                    vida_util_residual = 0
                    for (var elemento of response.data.datos) {
                        if (elemento.estado === 'BUENO') {
                            data_grafico.bueno += 1
                        } else if (elemento.estado === 'REGULAR') {
                            data_grafico.regular += 1
                        } else if (elemento.estado === 'MALO') {
                            data_grafico.malo += 1
                        } else if (elemento.estado === 'BAJA') {
                            data_grafico.baja += 1
                        }
                    }

                    for (var crt of response.data.datos) {
                        if (crt.criticidad == 'CRITICO') {
                            data_grafico_barra.critico += 1
                        } else if (crt.criticidad == 'RELEVANTE') {
                            data_grafico_barra.relevante += 1
                        }
                    }

                    for (var vu of response.data.datos) {
                        if (vu.vida_util < 0) {
                            vida_util_residual += 1
                        }
                    }

                    this.data_columnas_tabla = [
                        'ID', 'Clase', 'Nombre', 'Marca', 'Modelo', 'Serie', 'Anio', 'Vida Util', 'Estado', 'Criticidad', 'Garantia',
                        'Vencimiento Garantia', 'Plan Mantención', 'Tipo Equipo', 'ID Convenio', 'ID Institución', 'Eliminado', 'Año Ingreso',
                        'Costo Anual', 'Nombre Proveedor', 'Numero Inventario', 'Recinto', 'Servicio Clinico', 'Subclase', 'Tipo Mantenimiento',
                        'Vida Util Residual'
                    ]

                    this.titulo_primer_grafico = 'Equipos Medicos'
                    this.grafico(data_grafico.bueno, data_grafico.regular, data_grafico.malo, data_grafico.baja)
                    this.grafico_barra_1(data_grafico_barra.critico)
                    this.grafico_barra_2(data_grafico_barra.relevante)
                    this.vida_util = vida_util_residual
                    this.data_tabla = response.data.datos
                })

        },

        grafico(bueno, regular, malo, baja) {
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
                        radius: ['20%', '70%'],
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
                            { value: bueno, name: 'Bueno' },
                            { value: regular, name: 'Regular' },
                            { value: malo, name: 'Malo' },
                            { value: baja, name: 'Baja' }
                        ]
                    }
                ]
            };

            myChart.setOption(option);
            window.addEventListener('resize', function () {
                myChart.resize();
            });
        },

        grafico_barra_1(critico) {
            const domContenedorMultiplesgraficos = document.getElementById('grafico-barra-criticidad-anual')
            var myChart = echarts.init(domContenedorMultiplesgraficos, null)

            option = {
                grid: {
                    left: '2%',
                    right: '2%',
                    bottom: '3%',
                    containLabel: true,
                },
                xAxis: {
                    type: 'value'
                },
                yAxis: {
                    type: 'category',
                    data: ['Criticos']
                },
                series: [
                    {
                        name: 'Bueno',
                        type: 'bar',
                        stack: 'total',
                        label: {
                            show: true
                        },
                        emphasis: {
                            focus: 'series'
                        },
                        data: [critico]
                    },

                ],

                resize: true
            };
            myChart.setOption(option);
        },

        grafico_barra_2(relevante) {
            const domContenedorMultiplesgraficos = document.getElementById('grafico-barra-relevante-anual')
            var myChart = echarts.init(domContenedorMultiplesgraficos, null)

            option = {
                grid: {
                    left: '2%',
                    right: '2%',
                    bottom: '3%',
                    containLabel: true,
                },
                xAxis: {
                    type: 'value'
                },
                yAxis: {
                    type: 'category',
                    data: ['Relevantes']
                },
                series: [
                    {
                        name: 'Bueno',
                        type: 'bar',
                        stack: 'total',
                        label: {
                            show: true
                        },
                        emphasis: {
                            focus: 'series'
                        },
                        data: [relevante]
                    },
                ],
            };
            myChart.setOption(option);
        },











        // Metodo relacionado con la busqueda
        buscar() {
            const data = {
                'id_institucion': 1,
                'tipo_equipo': 'medico',
                'numero_inventario_busqueda': this.busqueda
            }

            if (this.opcionSelecionada === 'medico') {
                data.tipo_equipo = 'medico'
                axios.post('http://127.0.0.1:8000/busqueda_equipos_medicos/', data)
                    .then(response => {
                        console.log(response.data.data);
                        this.resultados = response.data.data

                        // Muestra el modal si hay resultados
                        if (this.resultados.length > 0) {
                            $('#resultado-modal').modal('show');
                        }
                        else {
                            const toast = new Toasts({
                                offsetX: 20, // 20px
                                offsetY: 20, // 20px
                                gap: 40, // The gap size in pixels between toasts
                                width: 450, // 300px
                                timing: 'ease', // See list of available CSS transition timings
                                duration: '.5s', // Transition duration
                                dimOld: true, // Dim old notifications while the newest notification stays highlighted
                                position: 'bottom-left' // top-left | top-center | top-right | bottom-left | bottom-center | bottom-right
                            });
                            toast.push({
                                title: 'No hay resultados',
                                content: 'No existen coincidencias con el numero de serie',
                                style: 'error'
                            })
                        }
                    })
                    .catch(error => {
                        console.log(error);
                        this.cerrarModalResultadosBusqueda()
                    })
            }
            else if (this.opcionSelecionada === 'industrial') {
                data.tipo_equipo = 'industrial'
                axios.post('http://127.0.0.1:8000/busqueda_equipos_industriales/', data)
                    .then(response => {
                        console.log(response.data.data);
                        this.resultados = response.data.data

                        if (this.resultados.length > 0) {
                            $('#resultado-modal').modal('show');
                        }
                        else {
                            const toast = new Toasts({
                                offsetX: 20, // 20px
                                offsetY: 20, // 20px
                                gap: 40, // The gap size in pixels between toasts
                                width: 450, // 300px
                                timing: 'ease', // See list of available CSS transition timings
                                duration: '.5s', // Transition duration
                                dimOld: true, // Dim old notifications while the newest notification stays highlighted
                                position: 'bottom-left' // top-left | top-center | top-right | bottom-left | bottom-center | bottom-right
                            });
                            toast.push({
                                title: 'No hay resultados',
                                content: 'No existen coincidencias con el numero de serie',
                                style: 'error'
                            })
                        }
                    })
                    .catch(error => {
                        console.log(error);
                        this.cerrarModalResultadosBusqueda()
                    })
            }
            else if (this.opcionSelecionada === 'vehiculo') {
                data.tipo_equipo = 'vehiculo'
                axios.post('http://127.0.0.1:8000/busqueda_vehiculos/', data)
                    .then(response => {
                        console.log(response.data.data);
                        this.resultados = response.data.data

                        if (this.resultados.length > 0) {
                            $('#resultado-modal').modal('show');
                        }
                        else {
                            const toast = new Toasts({
                                offsetX: 20, // 20px
                                offsetY: 20, // 20px
                                gap: 40, // The gap size in pixels between toasts
                                width: 450, // 300px
                                timing: 'ease', // See list of available CSS transition timings
                                duration: '.5s', // Transition duration
                                dimOld: true, // Dim old notifications while the newest notification stays highlighted
                                position: 'bottom-left' // top-left | top-center | top-right | bottom-left | bottom-center | bottom-right
                            });
                            toast.push({
                                title: 'No hay resultados',
                                content: 'No existen coincidencias con la patente',
                                style: 'error'
                            })
                        }
                    })
                    .catch(error => {
                        console.log(error);
                        this.cerrarModalResultadosBusqueda()
                    })
            }
        },




        cerrarModalResultadosBusqueda() {
            $('#resultado-modal').modal('hide');
        },

        limpiarCampo() {
            this.busqueda = ''
        }






    },

    mounted() {
        // this.actualizarGraficoMedianteSelect()
        this.data_inicial()
    }

}).mount('#app')
