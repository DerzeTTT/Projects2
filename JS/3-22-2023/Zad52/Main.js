// Zad 5.2

function pow(x,n){

    total = x;

    for (let i = 1; i<n; i++){

        total *= x;

    };

    return total;

};

console.log(pow(4,9))