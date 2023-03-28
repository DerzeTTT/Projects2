// Zad 5.1

function checkAge(age){

    return age > 18 || confirm('Did parents allow you?');

};

checkAge(19)

function checkAge(age){

    return age > 18 ? true : confirm('Did parents allow you?');

};

checkAge(17)