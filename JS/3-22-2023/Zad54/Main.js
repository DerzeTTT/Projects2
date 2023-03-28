// Zad 5.4

function capitalize(passedStr){

    let firstChar = passedStr.substring(0,1);
    let rest = passedStr.substring(1, passedStr.length);

    return firstChar.toUpperCase() + rest;

};

console.log(capitalize('halo'));