$(document).on("click", ".clearcart", function () {
  localStorage.clear();
});
document.getElementById("cart").innerHTML =
  "Cart(" + Object.keys(cart).length + ")";
