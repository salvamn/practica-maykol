const { createApp } = Vue
createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            data_tabla: null,
            idConvenioEliminar: null
        }
    },




    methods: {
        obtenerConvenios() {
            axios.get('http://127.0.0.1:8000/obtener_convenios_general/')
                .then(response => {
                    this.data_tabla = JSON.parse(response.data.data)
                })
        },

        btnDialogoEliminarConvenio(event) {
            // var idBtn = event.target.id
            // console.log(idBtn);
            // this.mostrarDialogo()

            data = {
                id: this.idConvenioEliminar
            }

            console.log(data);

            axios.post('http://127.0.0.1:8000/eliminar_convenio/', data)
                .then(response => {
                    if (response.data.mensaje === 'ok') {
                        this.ocultarDialogo()
                        var elementoAEliminar = document.getElementById(`fila-${this.idConvenioEliminar}`)
                        elementoAEliminar.classList.add('fadeOut')
                        setTimeout(function () {
                            elementoAEliminar.remove()
                        }, 500)
                    }
                })

        },

        ocultarDialogo() {
            document.getElementById('modal-dialogo').classList.add('hidden')
            document.getElementById('modal-background').classList.add('hidden')
        },

        mostrarDialogo(event) {
            var idBtn = event.target.id
            this.idConvenioEliminar = idBtn
            document.getElementById('modal-dialogo').classList.remove('hidden')
            document.getElementById('modal-background').classList.remove('hidden')
            document.getElementById('modal-dialogo').classList.add('flex')
            document.getElementById('modal-background').classList.add('flex')
        },

        ocultarModalConvenio(event) {
            document.getElementById('modal-editar-convenio').classList.remove('flex')
            document.getElementById('modal-background-convenio').classList.remove('flex')
            document.getElementById('modal-editar-convenio').classList.add('hidden')
            document.getElementById('modal-background-convenio').classList.add('hidden')
        },

        mostrarModalConvenio(event) {
            var idBtn = event.target.id
            this.idConvenioEliminar = idBtn
            document.getElementById('modal-editar-convenio').classList.remove('hidden')
            document.getElementById('modal-background-convenio').classList.remove('hidden')
            document.getElementById('modal-editar-convenio').classList.add('flex')
            document.getElementById('modal-background-convenio').classList.add('flex')
        },


        generarPDFConvenio(event) {
            event.preventDefault()
            data = {
                id: event.target.id
            }

            axios.post('http://127.0.0.1:8000/generar_pdf_convenio/', data, { responseType: 'blob' })
                .then(response => {
                    // Crear un objeto Blob con el contenido del PDF recibido
                    console.log(response);
                    const blob = new Blob([response.data], { type: 'application/pdf' });
                    // Crear una URL del objeto Blob
                    const url = window.URL.createObjectURL(blob);

                    // Crear un enlace temporal para forzar la descarga del PDF
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'archivo.pdf');

                    // Agregar el enlace al DOM y hacer clic en él
                    document.body.appendChild(link);
                    link.click();

                    // Liberar la URL del objeto Blob
                    window.URL.revokeObjectURL(url);
            })
        },


    },


    mounted() {
        this.obtenerConvenios()
    }


}).mount('#app')