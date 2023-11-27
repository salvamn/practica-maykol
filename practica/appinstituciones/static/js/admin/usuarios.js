





// https://izimodal.marcelodolza.com//#modal-large
$("#modal-opciones-usuario").iziModal({
    title: 'Opciones de usuario',
    headerColor: '#333333'
});

// $(document).on('click', '.trigger', function (event) {
//     event.preventDefault();
//     $('#modal-opciones-usuario').iziModal('open');
// });
    






const { createApp } = Vue
createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            usuario: {
                'id': null,
                'nombre_usuario': null,
                'nombre': null,
                'apellido': null,
                'rut': null,
                'cargo': null,
                'correo': null,
                'institucion': null
            }
        }
    },

    methods: {
        obtenerUsuario(id){
            axios.get(`http://127.0.0.1:8000/obtener_usuario/${id}/`)
            .then(response => {
                this.usuario.id = response.data.id
                this.usuario.nombre_usuario = response.data.username
                this.usuario.nombre = response.data.first_name
                this.usuario.apellido = response.data.last_name
                this.usuario.rut = response.data.rut
                this.usuario.cargo = response.data.cargo
                this.usuario.correo = response.data.email

                console.log(response.data.id);
                console.log(this.usuario.id);

                $('#modal-opciones-usuario').iziModal()
                $('#modal-opciones-usuario').iziModal('open');
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalNombre').text(this.usuario.nombre);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalApellido').text(this.usuario.apellido);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalCorreo').text(this.usuario.correo);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalRut').text(this.usuario.rut);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalNombreUsuario').text(this.usuario.nombre_usuario);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalCargo').text(this.usuario.cargo);
                $('#modal-opciones-usuario .contenedor-informacion-usuario .spanEnModalInstitucion').text(this.usuario.institucion);
                // $('#modal-opciones-usuario .contenedor-informacion-usuario .eliminar-usuario').attr('id', this.usuario.id);
            })
            .catch(error => {
                console.error('Error al obtener el usuario:', error);
            });
        },

        eliminarUsuario(id){
            axios.get(`http://127.0.0.1:8000/eliminar_usuario/${id}/`)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.error('Error al obtener el usuario:', error);
            });
        },

        btnEliminarUsuario(event){
            // console.log('boton presionado');
            // console.log(event.target.id);

            const respuesta = confirm("¿Estás seguro de realizar esta acción?");

            if (respuesta) {
              // Código a ejecutar si el usuario hace clic en "Aceptar"
                console.log("Acción confirmada");
                this.eliminarUsuario(event.target.id)
                location.reload()
            } else {
              // Código a ejecutar si el usuario hace clic en "Cancelar" o cierra el diálogo
              console.log("Acción cancelada");
            }
        },

        abrirModalInformacionUsuario(event){
            const idUsuario = event.target.id
            this.obtenerUsuario(idUsuario)
        },

        cerraModalInformacionUsuario(){
            $(this.$refs.miModal).iziModal("close");
        }
    },

    mounted(){

    }

}).mount('#app')
// }).mount('.contenedor-informacion-usuario')
