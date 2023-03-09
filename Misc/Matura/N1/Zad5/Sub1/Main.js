const fs = require('fs');
const sokiPath = require('path').resolve(__dirname, 'soki.txt');

const Reading = fs.readFileSync(sokiPath, 'UTF-8').trim().split("\n");
Reading.shift();

let List = new Object();

function Organize(Line){

    const Data = Line.split('\t');
    
    List[Data[0]] = {

        'Date':Data[1],
        'Magazine':Data[2],
        'Size':Data[3]

    };

};

Reading.forEach((Line) => {

    Organize(Line);

});

Counted = new Object();

for (const [_,Data] of Object.entries(List)){

    if (!Counted[Data.Magazine]) {

        Counted[Data.Magazine] = 1;

    } else {

        Counted[Data.Magazine]++;

    };

};

for (const [Magazine, Count] of Object.entries(Counted)){
    
    console.log(`Magazyn ${Magazine} dostal ${Count} zamowien`);

};