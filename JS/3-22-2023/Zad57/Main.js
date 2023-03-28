// Zad 5.7

cart = ["apple", "orange", "banana", "haha"];

function removeFromCart(item){

    ind = cart.indexOf(item);

    cart.splice(ind, 1);

};

console.log(cart);

removeFromCart('banana');

console.log(cart);