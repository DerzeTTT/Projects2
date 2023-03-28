// Zad 5.3

let cart = [];

function addToCart(item){

    if (cart.includes(item)) {return};

    cart.push(item);

};

addToCart("haha");
addToCart('bulka');

console.log(cart)