// Zad 5.6

function ask(question, y, n){

    confirm(question) ? y() : n();

};

ask("Are you gay", () => {console.log("Haha you're gay")}, () => {console.log(":C")});