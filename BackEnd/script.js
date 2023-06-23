new Vue({
  el: "#app",
  data: {
    products: [],
    currentProduct: { id: "", name: "", price: "", image: "" },
    editing: false,
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios
        .get("https://mbdev.pythonanywhere.com/productos")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    saveProduct() {
      if (this.editing) {
        // Editar producto existente
        axios
          .put(
            `https://mbdev.pythonanywhere.com/productos/${this.currentProduct.id}`,
            this.currentProduct
          )
          .then((response) => {
            const updatedProduct = response.data;
            const index = this.products.findIndex(
              (product) => product.id === updatedProduct.id
            );
            if (index !== -1) {
              this.products[index] = { ...updatedProduct };
            }
            this.clearForm();
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        // Agregar nuevo producto
        axios
          .post(
            "https://mbdev.pythonanywhere.com/productos",
            this.currentProduct
          )
          .then((response) => {
            const newProduct = response.data;
            this.products.push({ ...newProduct });
            this.clearForm();
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    editProduct(productId) {
      const product = this.products.find((product) => product.id === productId);
      if (product) {
        this.currentProduct = { ...product };
        this.editing = true;
      }
    },
    deleteProduct(productId) {
      if (confirm("¿Estás seguro de que quieres eliminar este producto?")) {
        axios
          .delete(`https://mbdev.pythonanywhere.com/productos/${productId}`)
          .then(() => {
            this.products = this.products.filter(
              (product) => product.id !== productId
            );
            this.clearForm();
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    clearForm() {
      this.currentProduct = { id: "", name: "", price: "", image: "" };
      this.editing = false;
    },
  },
});
