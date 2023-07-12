console.log(location.search); // lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
  data() {
    return {
      id: 0,
      nombre: "",
      apellido: "",
      direccion: "",
      url: "https://mbdev.pythonanywhere.com/usuarios/" + id, 
      //url: "http://localhost:5000/usuarios/" + id,
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.id = data.id;
          this.nombre = data.nombre;
          this.direccion = data.direccion;
          this.apellido = data.apellido;

        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    modificar() {
      let producto = {
        nombre: this.nombre,
        apellido: this.apellido,
        direccion: this.direccion
      };
      var options = {
        body: JSON.stringify(producto),
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        redirect: "follow",
      };
      fetch(this.url, options)
        .then(function () {
          Swal.fire({
            title: "Exito!",
            text: "Registro modificado",
            icon: "success",
            background: "#6D6D6D",
            color: "white",
          }).then(function () {
            window.location.href = "./index.html";
          });
        })
        .catch((err) => {
          console.error(err);
          alert("Error al Modificar");
        });
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount("#app");
