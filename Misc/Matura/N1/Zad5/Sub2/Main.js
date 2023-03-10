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

function getLargestInOBJ 

Periods = {};

for (const [_,Data] of Object.entries(List)){

    if (Data.Magazine === 'Ogrodzieniec'){

        Str_To_Date(Data.Date);

    };

};

Dates.sort((a,b) => {

    return a - b;

});

Periods = {};
Previous = null;

currentPeriod = 0;

for (let i = 0; i < Dates.length; i++){

    v = Dates[i];

    if (i == 0){

        Previous = v;
        Periods[currentPeriod] = {};

    };

    sincePassed = (v.getTime() - Previous.getTime()) / 1000;
    isFrequent = (toDays(sincePassed) <= 1);

    if (!isFrequent){

        currentPeriod++;

        Periods[currentPeriod] = {};

    } else {

        Periods[currentPeriod][v] = true;

    };

    Previous = v;

};