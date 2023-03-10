const Utilities = require('../Utilities');
List = Utilities.filterSoki();

encodedJSON = JSON.stringify(List);

const fs = require('fs');

fs.writeFileSync(`${__dirname}/StringifiedJSON.txt`, encodedJSON);

const { exec } = require("child_process");

exec(`python ${__dirname}/PieChart.py`, (_, stdout) => {
    console.log(stdout);
});