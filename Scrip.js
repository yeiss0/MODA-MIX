document.addEventListener("DOMContentLoaded", function() {
    const products = document.querySelectorAll(".product");

    products.forEach(product => {
        product.addEventListener("click", () => {
            const productName = product.querySelector("h3").innerText;
            alert(`Has seleccionado el producto: ${productName}`);
        });
    });
});
