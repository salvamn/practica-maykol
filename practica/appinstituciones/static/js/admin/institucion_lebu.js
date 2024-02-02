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
            placeholderDinamico: 'n° de inventario',
            // Variables del formulario editar
            tipoFormularioEditarCatastro: null, // medico, industrial, vehiculo,
            dataObjetoAEditar: null,
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
                            'Vida Util Residual', 'Opciones'
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
                            'Vida Util Residual', 'Opciones'
                        ]
                        // -----------
                        // Data Para la Tabla

                        this.titulo_primer_grafico = 'Equipos Industriales'
                        this.grafico(data_grafico.bueno, data_grafico.regular, data_grafico.malo, data_grafico.baja)
                        this.grafico_barra_1(data_grafico_barra.critico)
                        this.grafico_barra_2(data_grafico_barra.relevante)
                        this.vida_util = vida_util_residual
                        this.data_tabla = response.data.datos
                        // console.log(response.data);
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
                            'Tipo Mantenimiento', 'Vida Util Residual', 'Opciones'
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
                        'Vida Util Residual', 'Opciones'
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
                        this.resultados = response.data.data

                        // Muestra el modal si hay resultados
                        if (this.resultados.length > 0) {
                        // if (this.resultados) {
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
        },


        // Crud Editar y Eliminar
        editarCatastro(id, idInstitucion, tipoEquipo) {
            console.log(id, idInstitucion, tipoEquipo);
            this.tipoFormularioEditarCatastro = tipoEquipo
            const data = {
                'id': id,
                'idInstitucion': idInstitucion,
                'tipoEquipo': tipoEquipo
            }

            if(tipoEquipo === 'medico'){
                axios.post('http://127.0.0.1:8000/obtener_data/', data)
                .then(response => {
                    // console.log(response.data.resultado);
                    this.dataObjetoAEditar = response.data.resultado

                    // Obtenemos las referencias del dom mediante refs
                    const idEquipo = this.$refs.idEquipo
                    const clase = this.$refs.clase
                    const nombre = this.$refs.nombre
                    const marca = this.$refs.marca
                    const modelo = this.$refs.modelo
                    const serie = this.$refs.serie
                    const anio = this.$refs.anio
                    const vida_util = this.$refs.vida_util
                    const estado = this.$refs.estado
                    const criticidad = this.$refs.criticidad
                    const garantia = this.$refs.garantia
                    const vencimiento_garantia = this.$refs.vencimiento_garantia
                    const plan_mantencion = this.$refs.plan_mantencion
                    const tipo_equipo_parrafo = this.$refs.tipo_equipo_parrafo
                    const id_convenio = this.$refs.id_convenio
                    const id_institucion = this.$refs.id_institucion
                    const eliminado = this.$refs.eliminado
                    const anio_ingreso = this.$refs.anio_ingreso
                    const costo_anual = this.$refs.costo_anual
                    const nombre_proveedor = this.$refs.nombre_proveedor
                    const numero_inventario = this.$refs.numero_inventario
                    const recinto = this.$refs.recinto
                    const servicio_clinico = this.$refs.servicio_clinico
                    const sub_clase = this.$refs.sub_clase
                    const tipo_mantenimiento = this.$refs.tipo_mantenimiento
                    const vida_util_residual = this.$refs.vida_util_residual
                    
                    const inputHiddenIdEquipo = document.getElementById('hidden-id-equipo')
                    const ipnutHiddenTipoEquipo = document.getElementById('hidden-tipo-equipo')
                    
                    // Les asignamos texto a las refs
                    idEquipo.innerHTML = `ID: ${this.dataObjetoAEditar.id}`
                    clase.innerHTML = `Clase: ${this.dataObjetoAEditar.clase}`
                    nombre.innerHTML = `Nombre: ${this.dataObjetoAEditar.nombre}`
                    marca.innerHTML = `Marca: ${this.dataObjetoAEditar.marca}`
                    modelo.innerHTML = `Modelo: ${this.dataObjetoAEditar.modelo}`
                    serie.innerHTML = `Serie: ${this.dataObjetoAEditar.serie}`
                    anio.innerHTML = `Año: ${this.dataObjetoAEditar.anio}`
                    vida_util.innerHTML = `Vida util: ${this.dataObjetoAEditar.vida_util}`
                    estado.innerHTML = `Estado: ${this.dataObjetoAEditar.estado}`
                    criticidad.innerHTML = `Criticidad: ${this.dataObjetoAEditar.criticidad}`
                    garantia.innerHTML = `Garantia: ${this.dataObjetoAEditar.garantia}`
                    vencimiento_garantia.innerHTML = `Vencimiento de garantia: ${this.dataObjetoAEditar.vencimiento_garantia}`
                    plan_mantencion.innerHTML = `Plan de mantención: ${this.dataObjetoAEditar.plan_mantencion}`
                    tipo_equipo_parrafo.innerHTML = `Tipo de equipo: ${this.dataObjetoAEditar.tipo_equipo}`
                    id_convenio.innerHTML = `ID de convenio: ${this.dataObjetoAEditar.id_convenio}`
                    id_institucion.innerHTML = `ID de institución: ${this.dataObjetoAEditar.id_institucion}`
                    eliminado.innerHTML = `Eliminado: ${this.dataObjetoAEditar.eliminado}`
                    anio_ingreso.innerHTML = `Año de ingreso: ${this.dataObjetoAEditar.anio_ingreso}`
                    costo_anual.innerHTML = `Costo anual: ${this.dataObjetoAEditar.costo_anual}`
                    nombre_proveedor.innerHTML = `Nombre del proveedor: ${this.dataObjetoAEditar.nombre_proveedor}`
                    numero_inventario.innerHTML = `Numero de inventario: ${this.dataObjetoAEditar.numero_inventario}`
                    recinto.innerHTML = `Recinto: ${this.dataObjetoAEditar.recinto}`
                    servicio_clinico.innerHTML = `Servicio clinico: ${this.dataObjetoAEditar.servicio_clinico}`
                    sub_clase.innerHTML = `SubClase: ${this.dataObjetoAEditar.subclase}`
                    tipo_mantenimiento.innerHTML = `Tipo de mantenimiento: ${this.dataObjetoAEditar.tipo_mantenimiento}`
                    vida_util_residual.innerHTML = `Vida util residual: ${this.dataObjetoAEditar.vida_util_residual}`
                    inputHiddenIdEquipo.value = this.dataObjetoAEditar.id
                    ipnutHiddenTipoEquipo.value = this.dataObjetoAEditar.tipo_equipo


                    // Obtenemos referencia del boton
                    // const btn = this.$refs.btnEnviarFormularioEditarCatastro
                    // Asignamos el metodo correspondiante
                    // btn.addEventListener('click', this.enviarFormularioEditarCatastro)
                    // this.actualizarGraficoMedianteSelect()
                })
            }
            else if(tipoEquipo === 'industrial'){
                axios.post('http://127.0.0.1:8000/obtener_data/', data)
                .then(response => {
                    console.log(response.data.resultado);
                    this.dataObjetoAEditar = response.data.resultado
                    // Obtenemos las referencias del dom mediante refs
                    const idEquipo = this.$refs.idEquipo
                    const clase = this.$refs.clase
                    const nombre = this.$refs.nombre
                    const marca = this.$refs.marca
                    const modelo = this.$refs.modelo
                    const serie = this.$refs.serie
                    const anio = this.$refs.anio
                    const vida_util = this.$refs.vida_util
                    const estado = this.$refs.estado
                    const criticidad = this.$refs.criticidad
                    const garantia = this.$refs.garantia
                    const vencimiento_garantia = this.$refs.vencimiento_garantia
                    const plan_mantencion = this.$refs.plan_mantencion
                    const tipo_equipo_parrafo = this.$refs.tipo_equipo_parrafo
                    const id_convenio = this.$refs.id_convenio
                    const id_institucion = this.$refs.id_institucion
                    const eliminado = this.$refs.eliminado
                    const anio_ingreso = this.$refs.anio_ingreso
                    const costo_anual = this.$refs.costo_anual
                    const nombre_proveedor = this.$refs.nombre_proveedor
                    const numero_inventario = this.$refs.numero_inventario
                    const recinto = this.$refs.recinto
                    const servicio_clinico = this.$refs.servicio_clinico
                    const sub_clase = this.$refs.sub_clase
                    const tipo_mantenimiento = this.$refs.tipo_mantenimiento
                    const vida_util_residual = this.$refs.vida_util_residual
                    
                    const inputHiddenIdEquipo = document.getElementById('hidden-id-equipo')
                    const ipnutHiddenTipoEquipo = document.getElementById('hidden-tipo-equipo')
                    
                    // Les asignamos texto a las refs
                    idEquipo.innerHTML = `ID: ${this.dataObjetoAEditar.id}`
                    clase.innerHTML = `Clase: ${this.dataObjetoAEditar.clase}`
                    sub_clase.innerHTML = `SubClase: ${this.dataObjetoAEditar.subclase}`
                    marca.innerHTML = `Marca: ${this.dataObjetoAEditar.marca}`
                    modelo.innerHTML = `Modelo: ${this.dataObjetoAEditar.modelo}`
                    serie.innerHTML = `Serie: ${this.dataObjetoAEditar.serie}`
                    numero_inventario.innerHTML = `Numero de inventario: ${this.dataObjetoAEditar.numero_inventario}`
                    vida_util.innerHTML = `Vida util: ${this.dataObjetoAEditar.vida_util}`
                    vida_util_residual.innerHTML = `Vida util residual: ${this.dataObjetoAEditar.vida_util_residual}`
                    estado.innerHTML = `Estado: ${this.dataObjetoAEditar.estado}`
                    garantia.innerHTML = `Garantia: ${this.dataObjetoAEditar.garantia}`
                    id_institucion.innerHTML = `ID de institución: ${this.dataObjetoAEditar.id_institucion}`
                    anio.innerHTML = `Año: ${this.dataObjetoAEditar.anio}`
                    anio_ingreso.innerHTML = `Año de ingreso al plan de manteniento: ${this.dataObjetoAEditar.anio_ingreso_plan_mantenimiento}`
                    costo_anual.innerHTML = `Costo anual de mantenimiento: ${this.dataObjetoAEditar.costo_anual_mantenimiento}`
                    criticidad.innerHTML = `Criticidad: ${this.dataObjetoAEditar.criticidad}`
                    eliminado.innerHTML = `Eliminado: ${this.dataObjetoAEditar.eliminado}`
                    id_convenio.innerHTML = `ID de convenio: ${this.dataObjetoAEditar.id_convenio_mantenimiento}`
                    nombre.innerHTML = `Nombre: ${this.dataObjetoAEditar.nombre}`
                    nombre_proveedor.innerHTML = `Nombre del proveedor: ${this.dataObjetoAEditar.nombre_proveedor}`
                    recinto.innerHTML = `Nombre del recinto: ${this.dataObjetoAEditar.nombre_recinto}`
                    plan_mantencion.innerHTML = `Plan de mantención: ${this.dataObjetoAEditar.plan_mantencion}`
                    tipo_equipo_parrafo.innerHTML = `Tipo de equipo: ${this.dataObjetoAEditar.tipo_equipo}`
                    tipo_mantenimiento.innerHTML = `Tipo de mantenimiento: ${this.dataObjetoAEditar.tipo_mantenimiento}`
                    servicio_clinico.innerHTML = `Ubicación: ${this.dataObjetoAEditar.ubicacion}`
                    vencimiento_garantia.innerHTML = `Vencimiento de garantia: ${this.dataObjetoAEditar.vencimiento_garantia}`
                    inputHiddenIdEquipo.value = this.dataObjetoAEditar.id
                    ipnutHiddenTipoEquipo.value = this.dataObjetoAEditar.tipo_equipo
                })
            }
            else if (tipoEquipo === 'vehiculo') {
                axios.post('http://127.0.0.1:8000/obtener_data/', data)
                    .then(response => {
                    console.log(response.data.resultado);

                })
            }
            $('#miModalEditarCatastro').modal('show');
        },

        enviarFormularioEditarCatastro(event){
            event.preventDefault()

            $('#miModalEditarCatastro').modal('hide');




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
                title: 'Exito',
                content: 'Catastro editado exitosamente',
                style: 'success'
            })
        },


        eliminarCatastro(id, idInstitucion, tipoEquipo) {
            // Esta funcion recibe tres argumentos: id, idinstitucion y tipoEquipo, esto nos permite identificar el registro en la base de datos.
            console.log(id, idInstitucion, tipoEquipo);
            const data = {
                'id': id,
                'idInstitucion': idInstitucion,
                'tipoEquipo': tipoEquipo
            }
            axios.post('http://127.0.0.1:8000/eliminar_catastro/', data)
                .then(response => {
                    const index = this.data_tabla.findIndex(item => item.id === id)
                    console.log(index);
                    // JQUERY
                    $('#' + id).addClass('fila-eliminada').fadeOut('slow', function () {
                        $(this).remove(); // Eliminar completamente la fila después de la animación
                        console.log('fila eliminada');
                    });
                    // JQUERY
                    
                    console.log(response);

                    const toast = new Toasts({
                        offsetX: 20, // 20px
                        offsetY: 20, // 20px
                        gap: 20, // The gap size in pixels between toasts
                        width: 300, // 300px
                        timing: 'ease', // See list of available CSS transition timings
                        duration: '.5s', // Transition duration
                        dimOld: true, // Dim old notifications while the newest notification stays highlighted
                        position: 'bottom-left' // top-left | top-center | top-right | bottom-left | bottom-center | bottom-right
                    });
                    toast.push({
                        title: `Información`,
                        content: response.data.mensaje,
                        style: response.data.categoria
                    })
                })
                .catch(error => {
                console.log(error);
            })
        
        }






    },

    mounted() {
        // this.actualizarGraficoMedianteSelect()
        this.data_inicial()
    }

}).mount('#app')
