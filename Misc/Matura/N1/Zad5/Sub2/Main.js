const Utilities = require('../Utilities');
List = Utilities.filterSoki();

Dates = [];

function Str_To_Date(T_Str){

    Split_Date = T_Str.split('.');
    Date_Str = `${Split_Date[1]}/${Split_Date[0]}/${Split_Date[2]}`;

    New_Date = new Date(Date_Str);

    Dates.push(New_Date);

};

function toDays(Seconds){

    return Seconds/86400;

};

function getLargestInDict(tDict){

    let Largest = [[], 0];

    for (const[_,Dates] of Object.entries(tDict)){

        if (Array.isArray(Dates)){

            if (Dates.length > Largest[1]){

                Largest = [Dates, Dates.length]

            };

        };

    };

    return Largest;

};

for (const [_,Data] of Object.entries(List)){

    if (Data.Magazine === 'Ogrodzieniec'){

        Str_To_Date(Data.Date);

    };

};

Dates.sort((a,b) => {

    return a - b;

});

let Periods = {};
let Previous = null;

let currentPeriod = 0;

for (let i = 0; i < Dates.length; i++){

    let v = Dates[i];

    if (i == 0){

        Previous = v;
        Periods[currentPeriod] = [];

    };

    let sincePassed = (v.getTime() - Previous.getTime()) / 1000;
    let isFrequent = (toDays(sincePassed) <= 1);

    if (!isFrequent){

        currentPeriod++;

        Periods[currentPeriod] = [];

    } else {

        Periods[currentPeriod].push(v);

    };

    Previous = v;

};

let largestFound = getLargestInDict(Periods);

console.log(`Najwiekszy okres trwal ${largestFound[1]} dni od ${largestFound[0][0]} do ${largestFound[0][1]}`);