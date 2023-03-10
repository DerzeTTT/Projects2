const Utilities = require('../Utilities');
List = Utilities.filterSoki();

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