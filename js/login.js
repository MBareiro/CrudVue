console.log(location.search); // lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
  data() {
    return {
      data: [],
      email: "",
      password: "",
      url: "https://mbdev.pythonanywhere.com/usuarios"
      // url: "http://localhost:5000/usuarios"
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          this.datos = data
        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    validar() {
      if (!this.email || !this.password) {
        Swal.fire({
          title: "Error!",
          text: "Complete los campos",
          icon: "warning",
          background: "#6D6D6D",
          color: "white",
        })
      } else {
        arreglo  = this.datos.filter(element => element.email= this.email);
        if (arreglo[0].password == this.password) {
            sessionStorage.setItem('login', 'true');
            window.location.href = 'index.html';
        } else {
          Swal.fire({
            title: "Error!",
            text: "Email o password incorrecto",
            icon: "error",
            background: "#6D6D6D",
            color: "white",
          })
        }
      }        
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount("#app");

if(sessionStorage.getItem("login") != "true") {
//  /*  console.log("Login") */
  window.location.href = 'login.html';
}
