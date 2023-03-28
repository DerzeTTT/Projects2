// Zad 5.5

function getTotalCartPrice(cart){

    if (!cart) {return null};

    let total = 0;

    for (const item of cart){

        total += item.price;

    };

    return total;

};

console.log(getTotalCartPrice() || "Cart is empty!");
console.log(getTotalCartPrice([]));
console.log(getTotalCartPrice([{'name':'Apple', 'price':50}, {'name':'Orange', 'price':20}]));