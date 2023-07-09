const { createApp } = Vue;
createApp({
  data() {
    return {
      usuarios: [],
      //  si el backend esta corriendo local  usar localhost 5000(si no lo subieron a pythonanywhere)
      //  url:'http://localhost:5000/usuarios',
      url: "https://mbdev.pythonanywhere.com/usuarios", // si ya lo subieron a pythonanywhere

      error: false,
      cargando: true,

      /*  atributos para el guardar los valores del formulario    */
      id: 0,
      nombre: "",
      apellido: "",
      direccion: "",
    };
  },

  methods: {
    fetchData(url) {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          this.usuarios = data;
          this.cargando = false;
        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    eliminar(usuario) {
      Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta acción no se puede deshacer",
        icon: "warning",
        background: "#6D6D6D",
        color: "white",
        showCancelButton: true,
        confirmButtonText: "Borrar",
        cancelButtonText: "Cancelar",
        reverseButtons: true,
      }).then((result) => {
        if (result.isConfirmed) {
          // Realizar la acción de eliminar o realizar otras operaciones

          const url = this.url + "/" + usuario;
          var options = {
            method: "DELETE",
          };
          fetch(url, options)
            .then((res) => res.text()) // or res.json()
            .then((res) => {
              location.reload();
            });
        }
      });
    },
    grabar() {
      let usuario = {
        nombre: this.nombre,
        apellido: this.apellido,
        direccion: this.direccion,
        foto: this.foto
      };
      var options = {
        body: JSON.stringify(usuario),
        method: "POST",
        headers: { "Content-Type": "application/json" },
        redirect: "follow",
      };
      fetch(this.url, options)
        .then(function () {
          Swal.fire({
            title: "Exito!",
            text: "Registro grabado",
            icon: "success",
            background: "#6D6D6D",
            color: "white",
          }).then(function () {
            window.location.href = "./index.html";
          });
        })
        .catch((err) => {
          console.error(err);
          alert("Error al Grabar");
        });
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount("#app");
