module.exports = {
    
    filterSoki : function(){

        const fs = require('fs');
        const sokiPath = require('path').resolve(__dirname, 'soki.txt');
    
        const Reading = fs.readFileSync(sokiPath, 'UTF-8').trim().split("\n");
        Reading.shift();
    
        let List = new Object();
    
        function Organize(Line){

            const Data = [];
            
            Line.split('\t').forEach((Part) => {

                Data.push(Part.trim());

            });
            
            List[Data[0]] = {
    
                'Date':Data[1],
                'Magazine':Data[2],
                'Size':Data[3]
    
            };
    
        };
    
        Reading.forEach((Line) => {
    
            Organize(Line);
    
        });
    
        return List;

    }

};